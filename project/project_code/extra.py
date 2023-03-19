# Stage 1: given an inputted ticker, we will evaluate the data and spit it out to the user

import yfinance as yf


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
    main()

def tick() -> None:
    ticker: str = input("Enter a ticker: ")
    if ticker != "GOOGL":
        print("This ticker does not exist!")

def build() -> None:
    risk_pref: str = input("What is your risk preference? (low, medium, or high): ")
    # invest_amnt: str = input("How much would you like to invest? ")
    if risk_pref == "low":
        low_risk_port()
        print("low")
    elif risk_pref == "medium":
        medium_risk_port()
        print("medium")
    elif risk_pref == "high":
        high_risk_port()
        print("high")
    else:
        print("Please choose a risk preference of 'low,' 'medium,' or 'high.'")

def low_risk_port() -> None:
    """A diversified portfolio for an individual with a low risk preference"""

def medium_risk_port() -> None:
    """A diversified portfolio for an individual with a medium risk preference"""

def high_risk_port() -> None:
    """A diversified portfolio for an individual with a high risk preference"""

# If ticket DNE, return error
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