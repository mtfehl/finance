import numpy as np

months = [1, 2, 3]
prices = [238, 237, 239]

cpi_array = np.array([months, prices])
print(cpi_array)
# Prints out as [[1    2    3]
#                [238 237 239]]

print(cpi_array.shape)
# returns (2,3), indicating the array is 2 rows & 3 columns

print(cpi_array.size)
# return 6, the number of total elements in the array

array_prices = np.array(prices)
print(np.mean(array_prices))
# calculates the mean
# np.mean(array)

print(np.std(array_prices))
# calculates standard deviation
# np.std(array)

one_to_twenty = np.arange(1, 21, 1)
print(one_to_twenty)
# creates an array with a start, end, step

odds_thru_twenty = np.arange(1, 21, 2)
print(odds_thru_twenty)

cpi_transposed = np.transpose(cpi_array)
print(cpi_transposed)
# switches rows & columns of a numpy array
# np.transpose(2D_array)

print(cpi_array[1, 2])
# array indexing for 2D arrays
# row index 1, column index 2 (gives 239)

print(cpi_array[:, 2])
# array slicing
# all row slice, third column ([3, 239])