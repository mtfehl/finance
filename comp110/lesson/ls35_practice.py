"""Class practice for classes & objects."""
__author__ = "730321206"

class Frac:
    """A fractional value."""
    n: int
    d: int


def main() -> None:
    a: Frac = Frac()
    a.n = 1
    a.d = 4
    b: Frac = add(a, a)
    print(f"{b.n}/{b.d}")


def add(lhs: Frac, rhs: Frac) -> Frac:
    res: Frac = Frac()
    res.n = lhs.n * rhs.d + rhs.n * lhs.d
    res.d = lhs.d * rhs.d
    return res


if __name__ == "__main__":
    main()