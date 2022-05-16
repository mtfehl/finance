"""An example Python module."""

from typing import List

#STEP1: implement the function skeleton:
def total(xs: List[float]) -> float:
    """Compute the sum of a list of floats."""
    result: float = 0.0
    # For each x float in xs, add it to result
    for x in xs:
        result += x
    return result


#STEP2: set up a pytest test module
#to test the definitions of a module, first creating a sibling
#module with the same name, but ending in '_test"
#just because you pass your test, doesnt mean your function is fully
#and correctly operational; it needs to test a range of conditions
#ex: if we change return value to '0.0' it will pass, but still
#will be incorrect overall

#Pytest wont load if there is a syntax error in python code
#to check for this; open terminal and type "python -m pytest"
#or open "test" icon on sidebar and try to refresh for tests

#Before you implement a function, focus on concrete examples of how
# the function should behave as if it were already implemented
#Key questions to ask:
#   What are some usual arguments? (use cases)
#   What are some valid but unusual arguments? (edge cases)
#   Given those arguments, what is your expected return value for each set of inputs?


def join(xs: List[int], delimiter: str) -> str:
    """Produce a string where subsequent items are separated by delim."""
    generated_str: str = ""
    for item in xs:
        if generated_str == "":     #Don't put delimiter before first item.
            generated_str = str(item)
        else:
            generated_str += delimiter + str(item)
    return generated_str
    



"""Practice of skeleton functions before quiz01."""

from typing import List

def fill_range(low: int, high: int) -> List[int]:
    """Returns a list of consecutive integers between the two ints, in order, inclusively."""
    #input two integers, return numbers in between in order
    new_list: List[int] = []
    if low > high:
        return []
    if low == high:
        return [low]
    for numbers in range(low, high + 1):
        new_list.append(numbers)
    return new_list

#Use cases
# Usage:            Expected Result:
#fill_range(1, 3) ->  [1, 2, 3]
#fill_range(100, 101) -> [100, 101]
#
# Edge Cases
# fill_range(3, 1)      ->  []
# fill_range(1, 1)      ->  [1]