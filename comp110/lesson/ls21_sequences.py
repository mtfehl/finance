"""Examples of Sequences and notes."""

# Sequence: an abstract data type that is an ordered, 0-indexed set of values
# str - a sequence of character data
# Tuple - a fixed-size sequence of values of any types
# List - a dynamically-sized sequence of values of a specific type
# range - a sequence of integers at intervals between a start and end
# range- first int inclusive, last int exclusive (like a number line)

from typing import Tuple

Point2D = Tuple[float, float]
Color = Tuple[int, int, int]
origin: Point2D = (0.0, 0.0)
gray: Color = (128, 128, 128)


def brighter(a_color: Color) -> Color:
    """Return a new tuple that is slightly brighter!"""
    red: int = int(a_color[0] * 1.1)
    green: int = int(a_color[1] * 1.1)
    blue: int = int(a_color[2] * 1.1)
    return (red, green, blue)


from typing import List


def main() -> None:
    """Some examples of sequences."""
    a_list: List[int] = [110, 210, 211, 301, 311]
    print(a_list)
    print(range_example)

# Access items using subscription notation
    i: int = 0
    while i < len(a_list):
        print(a_list[i])
        i += 1

    names: List[str] = ["Kris", "Kaki", "Ezri"]
    print(names)

    names.append("Marc")
    print(names)

    names.pop(1)
    print(names)

    names.pop()
    print(names)


r = range = range(250, 275, 5)
def range_example(rnge: r) -> r:
    print(rnge)
    print(rnge.start), print(rnge.stop), print(rnge.step)
    print(rnge[0]), print(rnge[1])


if __name__ == "__main__":
    main()