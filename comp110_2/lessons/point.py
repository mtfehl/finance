
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

    def __str__(self) -> str:
        """"Produce a str representation of a Point for humans."""
        print("__str__ was called!")
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"
    

p0: Point = Point(1.0, 2.0)
p1: Point = p0.scale(2.0)
print(p0)
p1_as_a_str: str = str(p1)
print(p1_as_a_str)
print(f"p0: ({p0.x}, {p0.y})") 
print(f"p1: ({p1.x}, {p1.y})")

p1_repr: str = repr(p1)
print(p1_repr)