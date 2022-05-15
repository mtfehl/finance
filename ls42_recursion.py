"""Introduction to Recursion."""

def icarus(flaps: int) -> None:
    if flaps > 5:
        print("base case!")
        # Base case is when our recursion terminates
    else:
        print(f"flaps: {flaps}")
        icarus(flaps + 1)
        print(f"coming down {flaps}")
        # Recursive case: when icarus is added onto itself


icarus(0)