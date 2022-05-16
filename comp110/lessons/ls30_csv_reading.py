from csv import DictReader

from typing import List, Dict


file_handle = open("data/weather.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
table: List[Dict[str, float]] = []

for row in csv_reader:  # Reading each line of our CSV into a dictionary "row"
    float_row: Dict[str, float] = {}    # Setting up a new Dict w/ a row of str to float
    for column in row:  # Loop through each column in our given input row
        float_row[column] = float(row[column])  # Take given value in that row point, and store value in new Dict
    table.append(float_row) # Appending our Dict to a table
    # Here we converted a str to str dict into a str to float dict so we can utilize the inputs for computation
print(table)

high_sum: float = 0.0
for row in table: 
    high_sum += row["high"]
print("High temp average: " + str(high_sum / len(table)))

file_handle.close()