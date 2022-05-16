"""Tracking of weather patterns over JFK International Airport in New York City."""
__author__ = "730321206"

import sys

from csv import DictReader

from typing import List, Dict

read_mode: str = "r"


def main() -> None:
    """Entrypoint of our program."""
    arguments: Dict[str, str] = read_args()
    print(arguments)
    results_list: List[float] = search_weather(arguments["file_path"], arguments["column"], arguments["operation"])
    print(results_list)


def read_args() -> Dict[str, str]:
    """Returns the given arguments if correctly inputted, otherwise tells what arguments are accepted."""
    if len(sys.argv) != 4:
        print("Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]")
        exit()
    return {
        "file_path": sys.argv[1],
        "column": sys.argv[2],
        "operation": sys.argv[3]
    }


def search_weather(file_path: str, column: str, operation: str) -> List[float]:
    """Cycles through the weather data to find the daily summaries."""
    i: int = 0
    data_list: List[float] = []
    dates: List[str] = []
    file_handle = open(file_path, read_mode, encoding="utf8")
    csv_reader = DictReader(file_handle)
    for line in csv_reader:
        if column not in line:
            print("Invalid column: " + column)
            exit()
        if line["REPORT_TYPE"] == "SOD  ":
            try: 
                data_list.append(float(line[column]))
                dates.append((line["DATE"])[6:10])
            except ValueError:
                ...
        else:
            line[column].strip()
    file_handle.close()
    print(dates)
    if operation == "chart":
        chart_data(data_list, column, dates)
    elif operation == "list":
        return data_list
    elif operation == "max":
        single_list: List[float] = []
        single_list.append(max(data_list))
        return single_list
    elif operation == "min":
        single_list: List[float] = []
        single_list.append(min(data_list))
        return single_list
    elif operation == "avg":
        single_float: float = 0.0
        single_list: List[float] = []
        while i < len(data_list):
            single_float += data_list[i]
            i += 1
        single_float /= len(data_list)
        single_list.append(single_float)
        return single_list
    else:
        print("Invalid operation: " + operation)
        exit()
    return data_list


def chart_data(data: List[float], column: str, dates: List[str]) -> None:
    """Creates a ... graph of the weather data collected."""
    import matplotlib.pyplot as plt
    plt.plot(dates, data)
    plt.xlabel("Dates")
    plt.ylabel(column)
    plt.show()


if __name__ == "__main__":
    main()