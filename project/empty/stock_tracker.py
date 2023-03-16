# Stage 1: given an inputted ticker, we will evaluate the data and spit it out to the user
ticker: str = input("Enter a ticker: ")
# If ticket DNE, return error
# Import stock data of all available tickers & their associated data, using CSV readers and jupyter notebook
# We need to determine what information is relevant to a prospective investor
def read_stock_csv


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

