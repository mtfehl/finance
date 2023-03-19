"""Examples of optional parameters and Union types."""

from typing import Union

def hello(name: Union[str, int] = "World") -> str:
    """A function that says hello to the inputted name."""
    # greeting = f"Hello, {name}" (easy one line to do this)
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    else:
        greeting += f"Student Number #{name}"
    return greeting 

# Non-default arguments (x: int, for example) must come BEFORE
# 'default' arguments (such as name = "World")

# Single-argument
print(hello("Sally"))

# No arguments!
print(hello())

# int Argument works too!
print(hello(110)) 