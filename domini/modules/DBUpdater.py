
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
    if item.is_event == 'yes':
        event = 'Y'
    else :
        event = 'N'
    
    if ' ~ ' in item.period: 
        start_date, end_date = item.행사기간.split(sep=' ~ ')
    else:
        start_date = None
        end_date = None

with conn.cursor() as curs:
    sql = f"REPLACE INTO airline_events VALUES ('{index}', '{item.airline}', '{item.credit_card}', '{item.mobile_carrier}', '{item.pay_application}', '{item.min_cost}', '{item.discount}' , '{item.is_weekend}', '{item.is_oneway}', '{event}', '{item.discount_type}', '{item.duplicate}', '{item.option}', '{start_date}', '{end_date}')"
    curs.execute(sql)
    conn.commit()