# Stage 1: given an inputted ticker, we will evaluate the data and spit it out to the user

# API KEY: ZXTJ0OB2VZKPA2RK

import yfinance as yf
from project.project_code.helper_code import undelimit
from tabulate import tabulate
import numpy as np
from datetime import datetime as dt
import pandas_datareader as pdr
import pandas as pd
import matplotlib as plt
from alpha_vantage.timeseries import TimeSeries
from typing import Optional
from yahooquery import Ticker

app = TimeSeries("ZXTJ0OB2VZKPA2RK", output_format='pandas')



def main():
    print("Hello!")
    print("For info about the program, type: 'info'")
    print("To look up different assets' information, type: 'tick'")
    print("To build a diversifed portfolio, type: 'build'")
    print("To exit at any time, type: 'exit'")

    while True:
        program_info = input()
        if program_info == "info":
            info()
        elif program_info == "tick":
            tick()
        elif program_info == "build":
            build()
        elif program_info == "exit":
            print("Have a great day!")
            return False
        
def info() -> None:
    print("This program will allow you to do the following: ")
    print("- See different assets, their relevant statistics, and accompanying graphs")
    print("- Cross compare multiple tickers & see their (approximated) correlation")
    print("- Based on an inputted risk preference of 'low,' 'medium,', or 'high,' and a given $ amount, this program will auto-generate you a diversified portfolio.")

def tick() -> None:
    ticker: str = input("Enter 1 or more tickers, separated by a comma: ")
    if tick_tester(ticker) == True:
        tickers = undelimit(ticker)
        statistics(tickers)
        stock_data(tickers)
    else:
        print(f"'{ticker}' is not a valid ticker symbol.")

def tick_tester(given_tick: str) -> bool:
    start_date = '2022-03-14'
    end_date = '2023-03-14'
    list_of_tickers = undelimit(given_tick)
    for ticker_symbol in list_of_tickers:
        try:
            ticker = yf.Ticker(ticker_symbol.strip())
            df = ticker.history(start=start_date, end=end_date)
            if df.empty:
                return False
        except:
            return False
    return True

def list_of_lists(*args):
    return [list(item) for item in zip(*args)]

def statistics(x: list[str]) -> None:
    """Given tickers, create default statistics displayed in a table."""
    data_pool = []
    end_date = dt.now().strftime('%Y-%m-%d')
    for ticker in x:
        try:
            ticker_info = Ticker(ticker).summary_detail
            # print(ticker_info)
            dividend_rate = ticker_info[ticker]['dividendRate'] if 'dividendRate' in ticker_info[ticker] else '-'
            dividend_amount = ticker_info[ticker]['dividendYield'] if 'dividendYield' in ticker_info[ticker] else '-'
            pe_ratio = ticker_info[ticker]['trailingPE'] if 'trailingPE' in ticker_info[ticker] else '-'
            volume = ticker_info[ticker]['volume'] if 'volume' in ticker_info[ticker] else '-'
            beta = ticker_info[ticker]['beta'] if 'beta' in ticker_info[ticker] else '-'
            market_cap = ticker_info[ticker]['marketCap'] if 'marketCap' in ticker_info[ticker] else '-'
            expected_r = expected_return(ticker)
            sd = standard_deviation(ticker)
            sharpe = sharpe_ratio(ticker)
            data_pool.append([ticker, dividend_rate, dividend_amount, pe_ratio, volume, beta, market_cap, expected_r, sd, sharpe])
            # print(data_pool)
        except ValueError:
            print(f"{ticker} is not a valid ticker symbol")
            continue
    headers = ["TICKER", "DIVIDEND RATE", "DIVIDEND YIELD", "P/E RATIO", "VOLUME", "BETA", "MARKET CAP", "E(R)", "STANDARD DEVIATION", "SHARPE RATIO"]
    print(tabulate(data_pool, headers=headers))


def stock_data(tickers: list[str]) -> None:
    """Creates a correlation table for all the different securities."""
    correlations_df = pd.DataFrame(columns = tickers)
    end_date = dt.now().strftime('%Y-%m-%d')
    # fetch the historical stock price data for each ticker symbol and store it in a DataFrame
    stock_data = pd.DataFrame()
    for ticker in tickers:
        try:
            ticker_data = yf.download(ticker, start='2020-01-01', end=end_date, progress=False)
            stock_data[ticker] = ticker_data['Close']
        except ValueError:
            print(f"{ticker} is not a valid ticker symbol")

    # calculate the correlations for each pair of tickers and store them in the DataFrame
    for i in range(len(tickers)):
        for j in range(i+1, len(tickers)):
            ticker1 = tickers[i]
            ticker2 = tickers[j]
            corr = pearson_correlation(stock_data[ticker1], stock_data[ticker2])
            correlations_df.at[ticker1, ticker2] = corr
            correlations_df.at[ticker2, ticker1] = corr


    # display the DataFrame
    print("CORRELATION BETWEEN THE SECURITES")
    print("---------------------------------")
    print(correlations_df)
    
def build() -> None:
    risk_pref: str = input("What is your risk preference? (low, medium, or high): ")
    # invest_amnt: str = input("How much would you like to invest? ")


    # for all portfolios: create a function that is first called that would group only very low corr stocks together (less than 0.3)
    # 

    # we need to build a weight calculator for each individual risk function. We would use Markowitz portfolio optimization so we can differentiate
    # might be easier to start with a basic portfolio with any given risk preference, then adjust it based on risk.
    # Step 1: build a function that creates a minimum variance port
    # Step 2: build a function that calculates the optimal complete portfolio
    # Step 3: build a function that constructs the complete portfolio

    if risk_pref == "low":
        low_risk_port()
    elif risk_pref == "medium":
        medium_risk_port()
    elif risk_pref == "high":
        high_risk_port()
    else:
        print("Please choose a risk preference of 'low,' 'medium,' or 'high.'")


def expected_return(x) -> float:
    """Calculates the expected return on a stock given its Beta value."""
    risk_free_rate = 0.0441
    expected_market_return_estimate = 0.08
    ticker_info = Ticker(x).summary_detail
    beta = ticker_info[x]['beta']
    return risk_free_rate + beta * (expected_market_return_estimate - risk_free_rate)

def standard_deviation(x) -> float:
    end_date = dt.now().strftime('%Y-%m-%d')
    ticker_data = yf.download(x, start='2020-01-01', end=end_date, progress=False)
    sd = np.std(ticker_data['Close'])
    return sd

def sharpe_ratio(x) -> float:
    """Calculates the sharpe ratio of a stock (or a portfolio) given its SD and E(R)."""
    er = expected_return(x)
    risk_free_rate = 0.0441
    sd = standard_deviation(x)/100
    return (er - risk_free_rate)/sd

def pearson_correlation(x, y):
    """Calculate Pearson correlation coefficient between two variables."""
    x = np.array(x).astype(float)
    y = np.array(y).astype(float)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    std_x = np.std(x)
    std_y = np.std(y)
    num = np.sum((x - mean_x) * (y - mean_y))
    denom = (len(x) - 1) * std_x * std_y
    return num / denom

def covariance(x, y) -> float:
    """Calculates the covariance of two securities given their standard deviation."""
    corr = pearson_correlation(x, y)
    cov = corr * (standard_deviation(x) * standard_deviation(y))
    return cov
    

    




def low_risk_port() -> None:
    """A diversified portfolio for an individual with a low risk preference"""

def medium_risk_port() -> None:
    """A diversified portfolio for an individual with a medium risk preference"""

def high_risk_port() -> None:
    """A diversified portfolio for an individual with a high risk preference"""

# Import stock data of all available tickers & their associated data, using yfinance and jupyter notebook
# We need to determine what information/stats is relevant to a prospective investor


# Stage 2: given multiple inputted tickets, we can evaluate them side-by-side and determine which is better
# Pull up both their relevant statistics & say which has "better" values (relatively higher or lower),
# then have the code spit out an analysis of which is better for what kind of investor, etc.


# Stage 3: given 2 tickers, we can test to see if they are correlated & how strongly

# Likely accomplish this by cross-comparing two tickers under the same time frame using their d2d prices
## Likely that the larger the time frame, the better we can get an accurate corr value
## For example, we use Price Changes % day-to-day for AAPL compared to MSFT. If we see they both increase with each other,
## then we can say they are correlated. How closely in % they move and how often will determine the magnitude.


# Stage 4: given a ticker, the user can pull up graphs and relevant data/charts
# Using matplotlib, perhaps plotting two on the same graph is warranted


# Stage 5: given a user's risk preference & amount willing to invest, we create a portfolio builder
# User inputs amount they want to spend
# We need to figure out how to measure someone's risk preference -- do we just ask "low", "medium", and "high" risks?
## If so, then we could just use ranges (low 0-0.3 S.D, med 0.3-0.6 SD, high 0.6-1.0, for example)

if __name__ == "__main__":
    main()