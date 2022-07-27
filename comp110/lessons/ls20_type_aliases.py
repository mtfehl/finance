"""Examples of type aliases."""

Percent = float

def main() -> None:
    print(ratio(1, 2))


def ratio(numer: int, denom: int) -> Percent:
    """Calculate a simple percentage."""
    return numer / denom


if __name__ == "__main__":
    main()