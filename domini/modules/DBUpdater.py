
import pymysql
import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import configparser as parser

properties = parser.ConfigParser()
properties.read('./config.ini')
host = properties['DB_INFO']['host']
pwd = properties['DB_INFO']['pwd']
user = properties['DB_INFO']['user']
database = properties['DB_INFO']['database']
        
conn = pymysql.connect(host=host, user=user, password=pwd, db=database, charset='utf8')

with conn.cursor() as curs :
    sql = """
            CREATE TABLE IF NOT EXISTS airline_events (
                id INT(20),
                airline VARCHAR(10),
                credit_card VARCHAR(10),
                mobile_carrier VARCHAR(10),
                pay_application VARCHAR(10),
                min_cost INT(20),
                discount INT(20),
                is_weekend VARCHAR(1),
                is_oneway VARCHAR(1),
                is_event VARCHAR(1),
                discount_type VARCHAR(10),
                duplicate VARCHAR(1),
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
    if item.이벤트참여여부 == 'yes':
        event = 'Y'
    else :
        event = 'N'
    
    if ' ~ ' in item.행사기간: 
        start_date, end_date = item.행사기간.split(sep=' ~ ')
    else:
        start_date = None
        end_date = None

with conn.cursor() as curs:
    sql = f"REPLACE INTO airline_events VALUES ('{index}', '{item.항공사}', '{item.카드사}', '{item.통신사}', '{item.페이앱}', '{item.최소비용}', '{item.할인금액}' , '{item.주중/주말}', '{item.편도/왕복}', '{event}', '{item.할인방식}', '{item.중복가능여부}', '{item.특이사항}', '{start_date}', '{end_date}')"
    curs.execute(sql)
    conn.commit()