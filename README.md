# Data_Pipeline_AlphaVantage

Objectiive - To create an ETL pipeline in Python for the Stock Market data using Alphavantage API

Steps:
  1. Create tables in postgres database to store data
  2. Extract data from Alphavantage API using API key
  3. Parse JSON data returned during the API calls 
  4. Store parsed data in postgres tables
  
 Database Design : A database connection is established with postgres using psycopg2 library and a cursor is created to execute the SQL queries need to create three tables in the database "Alphavantage_db". One for Stock Market data, one for Forex
 currency and one for crypotocurrency.
 Data is loaded in all tables in real time in an interval every 1 min.
 
 Data Extraction : Three functions are written in Alphavantage_ETL file to parse data into the database. Python wrapper built by 
 rommes is used to extract data from the end points. Parameters are configured in parameters file to pull the stocks and currencies that we are interested in.
 
 After inserting data into the tables, data is read into Pandas DataFrame using SQL queries. 

USE Airflow DAGS for workflow management and orchestration
