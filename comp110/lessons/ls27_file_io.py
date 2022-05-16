"""Count the letters shakespeare used."""

from typing import Dict, List
from matplotlib import pyplot

READ_MODE = "r"


def main() -> None:
    """Entrypoint into our program."""
    letter_counts: Dict[str, int] = read_character_data("data/shakespeare.txt")
    print(letter_counts)
    print(len(letter_counts))
    chart_data(letter_counts)


def read_character_data(file: str) -> Dict[str, int]:
    """Given a filename, read its contents and count its characters."""
    counts: Dict[str, int] = {}
    file_handle = open(file, READ_MODE)
    # Open is a built in function referring to opening a file
    # We can open a file to read it, write it, etc
    for line in file_handle:
        line = line.lower()
        for char in line:
            if char.isalpha():     
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1
    file_handle.close()     # Done working with file, close it
    return counts


def chart_data(letter_count: Dict[str, int]) -> None:
    """Plot the results of our textual analysis of Shakespeare."""
    pyplot.title("Counts of letters in Shakespeare")
    pyplot.xlabel("Letters")
    pyplot.ylabel("Count")
    labels: List[str] = list(letter_count.keys())
    values: List[int] = list(letter_count.values())
    pyplot.bar(labels, values)
    pyplot.show()


if __name__ == "__main__":
    main()