#Parameters for configuration
import psycopg2

Stock_Symbols = {
    "Microsoft" : "MSFT",
    "Amazon" : "AMZN",
    "Apple" : "AAPL",
    "Google" : "GOOGL",
    "FaceBook" : "FB",
    "AT&T" : "T",
    "CISCO" : "CSCO",
    "Intel" : "INTC",
    "Oracle" : "ORCL",
    "IBM":"IBM"
}
Forex_List = {
    "Kuwaiti Dinar" : "KWD" ,
    "Bahraini Dinar" : "BHD" ,
    "Omani Rial" : "OMR" ,
    "Jordanian Dinar" : "JOD",
    "Great Britain Pound" : "GBP",
    "Gibraltar Pound" : "GIP" ,
    "Caymanian Dollar" : "KYD" ,
    "Euro" : "EUR" ,
    "Swiss Franc" : "CHF",
    "US Dollar" : "USD",
    "Indian Ruppee" : "INR"}
Cryptocurrencies = {
    "From_Currency" : {"Bitcoin" : "BTC",
                    "Ethereum (ETH)" : "ETH",
                    "Zcash" : "ZEC",
                    "DASH" : "DASH",
                     "Ripple" : "XRP",
                    "Monero" : "XMR",
                    "BitcoinCash" : "BCH",
                    "NEO" : "NEO",
                    "CARDANO" : "ADA",
                     "EOS" : "EOS"
                    },
    "To_Currency" : {"Indian Rupee": "INR"}
}
Interval = ['1min']

Connection_Details = {"dbname" : "alphavantage_db", "user" : "postgres", "password" : "postgres"}

