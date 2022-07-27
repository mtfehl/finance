import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict = {
    "country": names, "drives_right": dr, "cars_per_cap": cpc
}

cars = pd.DataFrame(my_dict)

# this returns a 3D NumPy array with row labels of integers
# to fix this, we set cars.index equal to a specificed row labels

row_labels = ["USA", "AUS", "JAP", "IND", "RUS", "MOR", "EGY"]

cars.index = row_labels
print(cars)

pd.read_csv("csv_name", index_col = 0)