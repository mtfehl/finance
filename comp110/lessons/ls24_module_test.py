"""An example of a test module in Pytest."""

from lessons.ls24_module import total, join, fill_range
from typing import List
#next, add tests which are procedures whose names begin
# with 'test_'; ex: test_total_empty

def test_total_empty() -> None:
    """Total of empty list should be 0.0."""
    assert total([]) == 0.0
    # to make a boolean condition apart of a test, we use "assert"
    #whatever boolean expression comes after is true and we pass
    #if it is false, the test will fail, where we receive errors


def test_total_single_item() -> None:
    """Total of a single item list should be the first item's value."""
    assert total([110.0]) == 110.0


def test_total_many_items() -> None:
    """Total of a list with many items should be their sum."""
    assert total([1.0, 2.0, 3.0]) == 6.0

# We are writing these multiple test functions to pass our original
# function and see that it is correctly doing its job;
# The more tests it can pass, the more confidence we can have in the function.
#To run our test in terminal for this example, we would type:
#"python -m pytest lessons/ls24_module_test.py"


def test_join_use_case() -> None:
    assert join([1, 2, 3], ", ") == "1, 2, 3"


def test_join_edge_single_item() -> None:
    assert join ([1], ", ") == "1"


def test_join_edge_empty_delimiter() -> None:
    assert join([1, 2, 3], "") == "123"

# Testing is no substitute for critical thinking!
#   Passing your own tests doesn't ensure your function is correct.
#       Your tests must cover a useful range of cases.

#Rule of thumb: test 2+ use cases and 1+ edge cases
#When a function has if-else statements, try to write a test that reaches each branch.


def test_fill_range_use_multiple_ints() -> None:
    low: int = 1
    high: int = 5
    expected_result: List[int] = [1, 2, 3, 4, 5]
    assert fill_range(low, high) == expected_result
    #This is also an acceptable way to make a pytest


def test_fill_range_use_two_ints() -> None:
    assert fill_range(0, 1) == [0, 1]


def test_fill_range_edge_same_int() -> None:
    assert fill_range(0, 0) == [0]


def test_fill_range_edge_descending_int() -> None:
    assert fill_range(3, 1) == []


