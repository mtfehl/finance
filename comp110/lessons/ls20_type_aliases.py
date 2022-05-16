"""Examples of type aliases."""

from typing import Tuple

# Define two type aliases with specific names for more general types
percent = float
point3D = Tuple[float, float, float]


def main() -> None:
    print(ratio(1, 2))
    a_point: point3D = (0.0, 1.0, 2.0)
    print(a_point)


def ratio(Numer: int, Denom: int) -> percent:
    """Calculate a simple percentage."""
    return Numer / Denom


if __name__ == "__main__":
    main()
