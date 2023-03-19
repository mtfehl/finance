"""Main functions & libraries."""


import yfinance as yf
from datetime import datetime

# # CREATE TICKER INSTANCE FOR AMAZON
amzn = yf.Ticker("AMZN")

# # GET TODAYS DATE AND CONVERT IT TO A STRING WITH YYYY-MM-DD FORMAT (YFINANCE EXPECTS THAT FORMAT)
end_date = datetime.now().strftime('%Y-%m-%d')
amzn_hist = amzn.history(start='2022-01-01',end=end_date)
print(amzn_hist)

# Set the start and end date
start_date = '2020-01-01'
end_date = '2022-01-01'

# Set the ticker
ticker = 'GOOGL'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print the last 5 rows
print(data.tail())

tickers = ['AAPL', 'GOOGL', 'AMZN']
stock_data = yf.download(tickers, start='2021-01-02', end="2021-01-31", group_by='ticker')
print(stock_data)

# could use pandas tabular form to create the corr between multiple tickers (step3)
import pandas
data = [['E(R)', 24, 12], 
        ['SD', 19, 14],
        ['SHARPE', 15, 19]]
headers=["AMZN", "AAPL", "MSFT"]
print(pandas.DataFrame(data, headers, headers))


# use this to display tickers with their default values (step2)
from tabulate import tabulate
data = [['AAPL', 24, 12],
['MSFT', 19, 14],
['AMZN', 15, 19],
['GOOGL', 10, 20]]
print (tabulate(data, headers=["TICKER", "E(R)", "SD"]))


# helper function from comp110
def undelimit(x: str) -> list[str]:
    """The given string will be returned as a list of strings separated by commas."""
    new_list: list[str] = []
    new_str: str = ""
    if x == "":
        return new_list
    for i in range(0, len(x)):
        if x[i] != ",":
            new_str += x[i]
        else:
            new_list.append(new_str.strip())
            new_str = ""
    new_list.append(new_str.strip())
    return new_list


def tick_tester(given_tick: str) -> bool:
    i = 0
    start_date = '2022-03-14'
    end_date = '2023-03-14'
    list_of_tickers = undelimit(given_tick)
    bool_list: list[bool] = []
    for tickers in list_of_tickers:
        try:
            ticker = yf.Ticker(tickers)
            df = ticker.history(start=start_date, end=end_date)
            true = not df.empty
            bool_list.append(true)
        except:
            false = False
            bool_list.append(false)
    while i < len(bool_list):
        if bool_list[i] == True:
            i += 1
        else:
            return False
    return True

import pandas as pd
import pandas_datareader as web
import datetime as dt
import numpy as np
 
import datetime as dt
import yfinance as yf
import seaborn





# REFERENCES
# https://algotrading101.com/learn/yfinance-guide/
# https://stackoverflow.com/questions/66306802/how-to-check-if-a-ticker-is-yfinance-library
# https://www.makeuseof.com/stock-price-data-using-python/
# https://www.qmr.ai/yfinance-library-the-definitive-guide/#Installing_yfinance
# https://appdividend.com/2022/09/14/python-zip-list-of-lists/
# https://towardsdatascience.com/how-to-use-variable-number-of-arguments-in-python-functions-d3a49a9b7db6
