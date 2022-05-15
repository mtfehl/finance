from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        # Self parameter is bound to new point object when the object is called

    def add(self, other: Point) -> Point:
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)


def main() -> None:
    a: Point = Point(1.0, 2.0)
    b: Point = Point(3.0, 4.0)
    c: Point = a.add(b)
    print(f"({c.x}, {c.y})")


if __name__ == "__main__":
    main()