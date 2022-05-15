"""Creation of list functions for exercise 5 leading up to qz01."""
__author__ = "730321206"

from typing import List


def count(x: List[int], y: int) -> int:
    """Returns the amount of times a specified number appears in a list."""
    int_counter: int = 0
    for numbers in x:
        if numbers == y:
            int_counter += 1
    return int_counter


def all(x: List[int], y: int) -> bool:
    """Determines whether the given int is the same int as all the ints in the given list."""
    # given a list on ints 'x', if they are all the same number as the given int 'y', we should return "true";
    # otherwise, we should return false. This includes empty lists
    i: int = 0
    yeah_true: bool = True
    nah_false: bool = False
    if x == []:
        return nah_false
    for ints in x:
        if ints == y:
            i += 1
        else:
            return nah_false
    if i > 0:
        return yeah_true


def max(input: List[int]) -> int:
    """Returns the largest number in a given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    banana = input[i]
    for numbers in input:
        if numbers > banana:
            banana = numbers
    return banana


def is_equal(x: List[int], y: List[int]) -> bool:
    """Determines if both lists contain the exact same elements."""
    if x == y:
        return True
    else:
        return False
    

def concat(x: List[int], y: List[int]) -> List[int]:
    """Adds the first given list to the second given list."""
    empty_list: List[int] = []
    for numbers in x, y:
        empty_list += numbers
    return empty_list


def sub(x: List[int], y: int, z: int) -> List[int]:
    """Returns a modification of the original list with the given start and stop indexes."""
    new_list: List[int] = []
    if x == new_list:
        return []
    if y > z:
        return []
    for numbers in range(x[y], x[z]):
        new_list.append(numbers)
    return new_list
    # range of ints in the given list x


def splice(x: List[int], y: int, z: List[int]) -> List[int]:
    """Returns the second list inserted into the first list at the given index."""
    new_list: List[int] = []
    i: int = 0
    orange: x[i]
    while i < y:
        for numbers in x, z:
            new_list.append(numbers)
        i += 1
