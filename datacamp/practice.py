import numpy as np

stock_prices = np.array([100, 200, 300])
boolean_array = (stock_prices >= 150)
print(boolean_array)
# Gives us [False True True]
print(stock_prices[boolean_array])
# Gives us [200 300]

my_array = np.array([100, 300, 500])

average_value = np.mean(my_array)
std_value = np.std(my_array)