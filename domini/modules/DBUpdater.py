
import configparser as parser
import pymysql
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

properties = parser.ConfigParser()
properties.read('./config.ini')
host = properties['DB_INFO']['host']
pwd = properties['DB_INFO']['pwd']
user = properties['DB_INFO']['user']
database = properties['DB_INFO']['database']

conn = pymysql.connect(host=host, user=user, password=pwd,
                       db=database, charset='utf8')

with conn.cursor() as curs:
    sql = """
            CREATE TABLE IF NOT EXISTS airline_events (
                id INT(20),
                airline VARCHAR(10),
                
                card_samsung VARCHAR(15),
                card_shinhan VARCHAR(5),
                card_kb  VARCHAR(5),
                card_bc VARCHAR(5),
                card_hyundai VARCHAR(5),
                card_nh VARCHAR(5),
                card_lotte VARCHAR(5),
                card_woori VARCHAR(5),

                mc_skt VARCHAR(5),
                mc_kt VARCHAR(5),
                mc_lgu  VARCHAR(5),
                mc_vip  VARCHAR(5),

                pay_kakao VARCHAR(5),
                mc_naver VARCHAR(5),
                mc_smile VARCHAR(5),
                mc_payco VARCHAR(5),

                min_cost INT(20),
                discount INT(20),
                is_weekend VARCHAR(10),
                is_oneway VARCHAR(10),
                is_event VARCHAR(10),
                discount_type VARCHAR(10),
                duplicate VARCHAR(10),
                option VARCHAR(100),
                start_date DATE,
                end_date DATE,
                PRIMARY KEY (id)      
            )
            """
    curs.execute(sql)
    conn.commit()

data = pd.read_csv('./discount_220506.csv')
print(data)

for index, item in enumerate(data.itertuples()):
    card_samsung = 'N'
    card_shinhan = 'N'
    card_kb = 'N'
    card_bc = 'N'
    card_hyundai = 'N'
    card_nh = 'N'
    card_lotte = 'N'
    card_woori = 'N'

    mc_skt = 'N'
    mc_kt = 'N'
    mc_lgu = 'N'
    mc_vip = 'N'

    pay_kakao = 'N'
    pay_naver = 'N'
    pay_payco = 'N'
    pay_smile = 'N'

    if item.is_event == 'yes':
        event = 'Y'
    else :
        event = 'N'
        
    if '삼성' in item.credit_card :
        card_samsung = 'Y'
    if '신한' in item.credit_card :
        card_shinhan = 'Y'
    if '국민' in item.credit_card :
        card_kb = 'Y'
    if '비씨' in item.credit_card :
        card_bc = 'Y'
    if '현대' in item.credit_card :
        card_hyundai = 'Y'
    if '농협' in item.credit_card :
        card_nh = 'Y'
    if '롯데' in item.credit_card :
        card_lotte = 'Y'
    if '우리' in item.credit_card :
        card_woori = 'Y'


    if 'SK' in item.mobile_carrier :
        mc_skt = 'Y'
    if 'KT' in item.mobile_carrier :
        mc_kt = 'Y'
    if 'LG' in item.mobile_carrier :
        mc_lgu = 'Y'
    if 'VIP' in item.mobile_carrier :
        mc_vip = 'Y'

    if '카카오' in item.pay_application :
        pay_kakao = 'Y'
    if '네이버' in item.pay_application :
        pay_naver = 'Y'
    if '스마일' in item.pay_application :
        pay_smile = 'Y'
    if '페이코' in item.pay_application :
        mc_payco = 'Y'
    if ' ~ ' in item.period:
        start_date, end_date = item.period.split(sep=' ~ ')
    else:
        start_date = '0000-00-00'
        end_date = '0000-00-00'

    with conn.cursor() as curs:
        sql = f"REPLACE INTO airline_events VALUES ('{index}', '{item.airline}', '{card_samsung}', '{card_shinhan}', '{card_kb}','{card_bc}', '{card_hyundai}', '{card_nh}', '{card_lotte}', '{card_woori}', '{mc_skt}', {mc_kt}',{mc_lgu}',{mc_vip}','{pay_kakao}', '{pay_naver}','{pay_smile}','{pay_payco}','{item.min_cost}', '{item.discount}' , '{item.is_weekend}', '{item.is_oneway}', '{event}', '{item.discount_type}', '{item.duplicate}', '{item.option}', '{start_date}', '{end_date}')"
        curs.execute(sql)
        conn.commit()
