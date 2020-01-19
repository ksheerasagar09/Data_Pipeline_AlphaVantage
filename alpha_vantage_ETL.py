# pull data from AlphaVantage API and insert data into Postgres Tables
import time
import os
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import requests
import alphavantage
from alpha_vantage.alphavantage import AlphaVantage
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange
import psycopg2
from Parameters import Stock_Symbols, Forex_List, Cryptocurrencies , Interval , Connection_Details


# function to load stock data
def load_stock_data_daily(api_key,params):
    print(api_key,params)
    for k, v in Stock_Symbols.items():
        conn = None
        try:
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            ts = TimeSeries(key=api_key)
            data, meta_data = ts.get_intraday(symbol=v, interval=Interval[0], outputsize='full')
            for key, value in data.items():
                Last_Refreshed = key
                open_price = value['1. open']
                high_price = value['2. high']
                low_price = value['3. low']
                close_price = value['4. close']
                volume = value['5. volume']
                cur.execute("Insert into stock_data_intraday values (%s,%s,%s,%s,%s,%s,%s)",
                            (Last_Refreshed, v, open_price, high_price, low_price, close_price, volume))
                conn.commit()
        except ValueError:
            print(
                "Calling Stock Data but execeeded number of calls per min,\nSo will call rest of the symbols after 60 seconds\n")
            time.sleep(60)
        finally:
            if conn is not None:
                conn.close()


# function to currency exchange data
def load_forex_data_intraday(api_key,params):
    for k, v in Forex_List.items():
        conn = None
        try:
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            fx = ForeignExchange(key=api_key)
            data, meta_data = fx.get_currency_exchange_intraday(from_symbol=v, to_symbol="INR", interval=Interval[0])
            for key, value in data.items():
                Last_Refreshed = key
                Time_Zone = meta_data['7. Time Zone']
                open_price = value['1. open']
                high_price = value['2. high']
                low_price = value['3. low']
                close_price = value['4. close']
                cur.execute("Insert into Currency_Exchange_Rate_Intraday values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (Last_Refreshed, Time_Zone, v, k,
                             "INR", "Indian Rupee", open_price, high_price, low_price, close_price)
                            )
                conn.commit()
        except ValueError:
            print(
                "Calling Forex Data but execeeded number of calls per min,\nSo will call rest of the symbols after 60 seconds\n")
            time.sleep(60)
        finally:
            if conn is not None:
                conn.close()


# function to compare cryptocurrencies
def load_cryptocurrency_data(api_key,params):
    for k, v in Cryptocurrencies["From_Currency"].items():
        conn = None
        try:
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cr = CryptoCurrencies(key=api_key)
            data, meta_data = cr.get_digital_currency_daily(symbol=v,
                                                            market=Cryptocurrencies["To_Currency"]["Indian Rupee"])
            for key, value in data.items():
                Last_Refreshed = key,
                Time_Zone = meta_data['7. Time Zone'],
                Digital_Currency_Code = v,
                Digital_Currency_Name = k,
                Market_Code = Cryptocurrencies["To_Currency"]["Indian Rupee"],
                Market_Name = "Indian Rupee",
                Open_INR = value['1a. open (INR)']
                Open_USD = value['1b. open (USD)']
                High_INR = value['2a. high (INR)']
                High_USD = value['2b. high (USD)']
                Low_INR = value['3a. low (INR)']
                Low_USD = value['3b. low (USD)']
                Close_INR = value['4a. close (INR)']
                Close_USD = value['4b. close (USD)']
                Volume = value['5. volume']
                Market_CAP = value['6. market cap (USD)']
                cur.execute(
                    "Insert into Cryptocurrency_Data_Daily values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (Last_Refreshed, Time_Zone, Digital_Currency_Code, Digital_Currency_Name,
                     Market_Code, Market_Name, Open_INR, Open_USD, High_INR, High_USD, Low_INR, Low_USD,
                     Close_INR, Close_USD, Volume, Market_CAP
                     )
                    )
            conn.commit()
        except ValueError:
            print(
                "Calling Cryptocurrency Data but execeeded number of calls per min,\nSo will call rest of the symbols after 60 seconds\n")
            time.sleep(60)
        finally:
            if conn is not None:
                conn.close()

def main():
    """
    Connects to Alphavantage database, creates cursor object, and passes this to the functions
    which load data into the database, before closing database connection.
    """
    api_key = os.environ['API_KEY']
    params = Connection_Details
    try:
        while True:
            load_stock_data_daily(api_key,params)
            load_forex_data_intraday(api_key,params)
            load_cryptocurrency_data(api_key,params)
            time.sleep(60)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()