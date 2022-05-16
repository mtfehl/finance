# Intro to lists
months = ["January, February, March, April, May, June"]
months[0]
    # this will print out to "January," since python is a 0-index language
months[-1]
    # this will print out "June," by using negative indexing

months[2:5]
# ["March", "April", "May"]
# Slicing is a way to subset multiple list items
# subsets March up to (but not including) June
# Before the colon is included, after colon is excluded

months[3:]
# ["April", "May", "June"]
# Begins subset at April, does not end (goes to end of specified list)

months[:3]
# ["January", "February", "March"]
# other way around of previous example

months[0:6:2]
# ["January", "March", "May"]
# months[start:end:step]
# step tells how much to skip over (if not specified, assumed to be 1)

# Create and print list names
names = ["Apple Inc", "Coca-Cola", "Walmart"]
print(names)

# Create and print list prices
prices = [159.54, 37.13, 71.17]
print(prices)

# Print the first item in names
print(names[0])

# Print the second item in names
print(names[1])

# Print the last element in prices
print(prices[-1])