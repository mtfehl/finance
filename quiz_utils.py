"""Responses for Quiz 01."""
__author__ = "730321206"
from typing import List


def strs_to_floats(x: List[str]) -> List[float]:
    """Converts a list of floats in form of string and converts them into float."""
    new_list: List[float] = []
    if x == [""]:
        return []
    for numbers in x:
        new_list.append(float(numbers))
    return new_list


def lookup(x: List[str], y: List[float], z: str) -> float:
    """Returns the assigned float value to a str name when called on.""" 
    if len(x) != len(y):
        raise ValueError("The given lists are inequal lengths.")
    i: int = 0
    new_float: float = 0.0
    x[i] == y[i]
    while i < len(x):
        for str in x:
            if z == str:
                new_float += y[i]
                i += 1
            else:
                i += 1
    if new_float == 0.0:
        raise ValueError("The given string does not exist in the list.")
    return new_float

    
def undelimit(x: str) -> List[str]:
    """The given string will be returned as a list of strings separated by commas."""
    new_list: List[str] = []
    new_str: str = ""
    for letters in x:
        new_str += letters
        if letters == ",":
            new_list.append(new_str)
            new_str = ""
    return new_list


def avg_column(x: List[str], y: str) -> float:
    """Quantifies data of weather in UNC and returns an average of a specified variable."""
    return 0.0