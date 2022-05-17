import matplotlib.pyplot as plt
prices = [240, 241, 239, 244, 245, 250, 243, 221, 228, 230, 233, 240]
prices_new = [240, 241, 240, 242, 243, 243, 244, 244, 244, 245, 245, 246]
# We can turn a histogram into a density function adding the density condition
plt.hist(x=prices, bins=6, density=True, alpha=0.5, label="Prices 1")
# Alpha argument adjusts transparency of each histogram plot
plt.hist(x=prices_new, bins=6, density=True, alpha=0.5, label="Prices New")
plt.legend()
plt.show()