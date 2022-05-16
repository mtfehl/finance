"""A redo for a sad attempt at my first quiz in comp110."""
__author__ = "730321206"


def is_tar(tar: str) -> bool:
    """Is the input tar or not?"""
    correct: bool = True
    incorrect: bool = False
    i: int = 0
    if tar == "":
        return incorrect
    if tar[0] == "t":
        i += 1
        while i < (len(tar) - 1):
            if tar[i] == "a":
                i += 1
            else:
                return incorrect
        if tar[len(tar) - 1] == "r":
            return correct
        else:
            return incorrect
    else:
        return incorrect


def boot(x: str, one: int, two: int) -> str:
    """Removes characters between the range of the two ints."""
    new_str: str = ""
    i: int = 0
    while i < len(x):
        if i < one:
            new_str += x[i]
        if i > two:
            new_str += x[i]
        i += 1
    return new_str


def sum_inputs() -> str:
    """Puts out summation of numbers inputted."""
    true: bool = True
    sum: int = 0
    sum_return_statement = ("Sum is " + str(sum))
    while true:
        put = int(input("Enter an int, -1 to sum: "))
        if put == -1:
            return ("Sum is " + str(sum))
        if put != -1:
            sum += put
    return sum_return_statement
        
 
def strip(x: str, LorR: str) -> str:
    """Moves the given string to the left or the right."""
    new_str: str = ""
    i: int = 0
    while i < len(x):
        if x[i] == " ":
            new_str = new_str
        if ord(x[i]) >= 65:
            new_str = new_str + x[i]
        if i == (len(x) - 1):
            if LorR == "left":
                new_str = new_str + "    "
            if LorR == "right":
                new_str = "     " + new_str
        i += 1
    return new_str