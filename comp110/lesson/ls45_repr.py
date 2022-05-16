"""Demo of __repr__ magic method."""

class Point:
    x: float = 0.0
    y: float = 0.0

    def __repr__(self) -> str:
        """Return a string representation of the object."""
        return f"({self.x}, {self.y})"


# Demo code
p0: Point = Point()
p0.x = 1.0
p1: Point = Point()
print(f"{p0}, - {p1}")