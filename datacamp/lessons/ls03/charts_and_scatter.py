# Matplotlib has lots of good data plotting functions 

import matplotlib.pyplot as plt

plt.plot()
# takes arguments (lists or arrays) that describe the data to be plotted

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
prices = [240, 241, 239, 244, 245, 250, 243, 221, 228, 230, 233, 240]
plt.plot(months, prices, color = 'red', linestyle = '--')
# can customize colors (red, blue, green), linestyles of charts (-, --, -., :)

# Adding an addt line
prices_new = [240, 241, 240, 242, 243, 243, 244, 244, 244, 245, 245, 246]
plt.plot(months, prices_new, color = "green", linestyle = "--")

# Add labels
plt.xlabel("Months")
plt.ylabel("Consumer Price Indexes, $")
plt.title("Avg. Monthly Consumer Price Index")

plt.show()
# displays plot to screen

# Scatterplots
plt.scatter(x = months, y = prices, color = "red", label = "example")
plt.xlabel("Months")
plt.ylabel("Prices")
plt.legend()
plt.show()
# Can change size of markets using command ' s = number_value ' after color

