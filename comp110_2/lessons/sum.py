"""Example of writing a test subject."""


def sum(xs: list[float]) -> float:
    """Compute the sum of a list."""
    final_sum: float = 0.0
    while len(xs) > 0:
        final_sum += xs[len(xs) - 1]
        xs.pop(len(xs) - 1)
    return final_sum

# another soln for the function:

# final_sum: float = 0.0
# i: int = 0
# while i < len(xs):
    # total += xs[i]
    # i += 1
# return total
# probably better since it doesnt amend the list
