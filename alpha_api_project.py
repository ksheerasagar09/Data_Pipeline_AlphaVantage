#!/usr/bin/env python
# coding: utf-8

import os
import time as t
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import requests
import alphavantage
from alpha_vantage.alphavantage import AlphaVantage
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange
from flask import Flask, Response, stream_with_context
api_key = os.environ['API_KEY']

from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key=api_key)
data, meta_data = ts.get_intraday('GOOGL')


meta_data

ts = TimeSeries(key=api_key)
data, meta_data = ts.get_intraday('GOOGL')

cur = conn.cursor()
cur.execute("""
   CREATE TABLE IF NOT EXISTS Stock_Data_Daily (Symbol varchar(255),
       period_date date,
       open_price real,
       high_price real,
       low_price real,
       close_price real,
       volume int
  )
""")
cur.execute("""
   CREATE TABLE IF NOT EXISTS Stock_Data_Weekly (Symbol varchar(255),
       period_date date,
       open_price real,
       high_price real,
       low_price real,
       close_price real,
       volume int
  )
""")
cur.execute("""
   CREATE TABLE IF NOT EXISTS Stock_Data_Monthly (Symbol varchar(255),
       period_date date,
       open_price real,
       high_price real,
       low_price real,
       close_price real,
       volume int
  )
""")
conn.commit()


import time
while True:
    ts = TimeSeries(key=api_key)
    data, meta_data = ts.get_intraday('GOOGL')
    try:
        if data["Time Series (Daily)"]:
            for key,value in data.items():
                period_date = key
                open_price = value['1. open']
                high_price = value['2. high']
                low_price = value['3. low']
                close_price = value['4. close']
                volume = value['5. volume']
                cur.execute("Insert into Stock_Data_Daily values (%s,%s,%s,%s,%s,%s,%s)",(symbol,period_date,open_price,high_price,low_price,close_price,volume))
                conn.commit()
                db_data = cur.fetchone()
                print(db_data)
        except KeyError:
        if data['Note']:
            print("sleeping for 60 seconds because execeeded number of calls per min ")
            time.sleep(60)


#  Main 
import psycopg2
conn = psycopg2.connect(dbname = 'ksheerasagar' , user = 'postgres', password = 'postgres')
cur = conn.cursor()
# cur.execute("Truncate table Stock_Data")
cur.execute("select count(*) from Stock_Data")
conn.commit()
count2 = cur.fetchone()
print(count2)

