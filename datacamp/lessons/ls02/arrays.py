# To install data packages, type: pip3 install package_name_here

# To import a data package, type: import package_name_here
import numpy as np

# package_name.array() --> we named the numpy function as np when we imported above
my_array = np.array([1, 2, 3, 4])
# Prints out [1, 2, 3, 4]

# Arrays better than lists: faster, can handle bigger data

# Arrays can only handle one data type (strings, ints, float, etc.)
# Lists can handle multiple data types

# Arrays
array_A = np.array([1,2,3])
array_B = np.array([4,5,6])

print(array_A + array_B)
# []

# Lists
list_A = [1,2,3]
list_B = [4,5,6]
print(list_A + list_B)
# [1,2,3,4,5,6]

# Can index and slice arrays just like lists