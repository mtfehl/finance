"""An Example function definition"""
__author__ = "Michael Fehl"

def my_max(a: int, b: int) -> int:
    """Returns the largest argument"""
    if a >= b:
        print(f"The highest number is {a}")
        return a
    else:
        print(f"The highest number is {b}")
        return b

print(my_max(10 + 1, 10))
result: int = my_max(-50, 100)
print(result)


x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)