
from __future__ import annotations


class Point:
    """Model a 2D Point."""

    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y 

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the point"""
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        print("__mul__ was called!")
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, rhs: Point) -> Point:
        print("__add__ was called!")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __str__(self) -> str:
        """"Produce a str representation of a Point for humans."""
        print("__str__ was called!")
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"
    

#__init__ method call
p0: Point = Point(1.0, 2.0)
# __init__ and scale_by method calls
p1: Point = p0.scale(2.0)
# printing through __str__ method call
print(p0)
p1_as_a_str: str = str(p1)
print(p1_as_a_str)

print(f"p0: ({p0.x}, {p0.y})") 
print(f"p1: ({p1.x}, {p1.y})")

# defining and printing through __repr__ method call
p1_repr: str = repr(p1)
print(p1_repr)

# __mul__ method call example (and __str__)
a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
print(f"a: {a}")
print(f"b: {b}")

# __add__ method call example
c: Point = a + b
print(f"c: {c}")