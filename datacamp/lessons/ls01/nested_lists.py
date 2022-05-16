months = ["Jan", "Feb", "Mar"]
prices = [238, 157, 190]

cpi = [months, prices]
# An Example of a nested list (list in a list)
print(cpi[1])
# This will return [238, 157, 190]
print(cpi[1][0])
# This will return 238

prices.sort()
# .sort() sorts the list in ascending order, returns None

print(prices)

months.append("Apr")
# This will add April into the list of months in quarter 1
# list.append() increases list element by 1

print(months)

months.extend(["May", "June", "July"])
# list.extend() increases list element by x

months.index("Feb")
# Returns 1
# list.index() function tells us the lowest index where element x appears
# We can now use that index to tell us prices[1]

# To find the month with the minimum price, we can use the min function
min_price = min(prices)
min_index = prices.index(min_price)
min_month = months[min_index]
print(min_month)