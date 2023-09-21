# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import mysql.connector


myconn =mysql.connector.connect(
    host='localhost',
    port=3307, 
    user='root',                           
    password='bemysql',                          
    database='world')

mycursor = myconn.cursor()

mycursor.execute('SELECT * FROM country')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    
import pandas as pd
    
sql = 'select * from country where continent="Oceania"'
    
df = pd.read_sql_query(sql, myconn)

from sqlalchemy import create_engine

myengine = create_engine("mysql+mysqlconnector://root:bemysql@localhost:3307/world")

df_1=pd.read_sql_table('country', myengine) 




                  
                         


