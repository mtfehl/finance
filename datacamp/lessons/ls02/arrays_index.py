import numpy as np

months_array = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
indexing_array = np.array([1, 3, 5])

months_subset = months_array[indexing_array]
print(months_subset)
# returns ["Feb", "Apr", "Jun"]

boolean_array = np.array([True, True, True, False, False, False])
print(months_array[boolean_array])
# returns only true values: ["Jan", "Feb", "Mar"]

prices_array = np.array([238, 237, 239])
boolean_array_2 = (prices_array > 238)
print(boolean_array_2)
# returns [False False True]

print(prices_array[boolean_array_2])
# returns [239]