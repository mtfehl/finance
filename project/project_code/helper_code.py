import yfinance as yf
from typing import Optional
from alpha_vantage.timeseries import TimeSeries

app = TimeSeries("ZXTJ0OB2VZKPA2RK", output_format='pandas')
# helper functions

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


def total_return(x: float, y: float, z: float) -> float:
    final_value = ((x - y + z)/y)
    return final_value




# # replace 'AAPL' with the desired ticker symbol
# ticker = yf.Ticker('AAPL')

# # fetch historical stock data
# hist = ticker.history(period='max')

# # calculate daily returns
# daily_returns = (hist['Close'] - hist['Close'].shift(1)) / hist['Close'].shift(1)

# # calculate expected return using average daily returns
# expected_return = daily_returns.mean()

# print(f"Expected return of {ticker}: {expected_return:.2%}")

