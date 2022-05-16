"""Tester functions for Quiz 01."""
__author__ = "730321206"
import pytest
from typing import List
from quiz.qz01.quiz_utils import strs_to_floats, lookup, undelimit, avg_column


def test_use_strs_to_floats_normal_case() -> None:
    """Tests the strs_to_floats function to see if it functions properly in a normal case."""
    assert strs_to_floats(["10.0", "5.0"]) == [10.0, 5.0]


def test_use_strs_to_floats_single_float() -> None:
    """Tests the str_to_float function when only one value is given."""
    assert strs_to_floats(["10.0"]) == [10.0]


def test_edge_strs_to_floats_empty_function() -> None:
    """Asserts that an empty given list returns an empty list as a result."""
    assert strs_to_floats([""]) == []


def test_use_lookup_normal_case() -> None:
    """Tests a normal scenario when all floats and strs are assigned and a given str is called upon."""
    assert lookup(["A", "B", "C"], [1.0, 2.0, 3.0], "B") == 2.0


def test_use_lookup_undefined_z_value_Value_Error() -> None:
    """Calling the 'lookup' function with an undefined string should raise a Value Error."""
    with pytest.raises(ValueError):
        example_list_a: List[str] = ["red", "blue", "orange", "green"]
        example_list_b: List[float] = [10, 20]
        z_value: str = "red"
        lookup(example_list_a, example_list_b, z_value)
    

def test_edge_lookup_list_inequal_lengths() -> None:
    """Raises a value error when the given lists of the lookup function are not equal lengths."""
    with pytest.raises(ValueError):
        example_list_a: List[str] = ["red", "blue", "orange", "green"]
        example_list_b: List[float] = [10, 20, 30, 40]
        z_value: str = "purple"
        lookup(example_list_a, example_list_b, z_value)


def test_use_undelimit_normal_case_no_spaces() -> None:
    """Tests the undelimit function when it correctly works with a given str with no spaces."""
    assert undelimit("hi,hello,hey") == ["hi", "hello", "hey"]


def test_use_undelimit_with_ints() -> None:
    """Tests the delimiter works with int values."""
    assert undelimit("4, 85, 92, 22") == [" 4 ", " 85 ", " 92 ", " 22 "]


def test_use_avg_column_normal() -> None:
    """Tests the avg_column function to make sure it correctly returns an average value."""
    assert avg_column(["high,low,precipitation", "70.0,20.0,0.1", "75.5,22.2,0.2", "68.9,21.1,0.3"], "precipitation") == 0.2


def test_use_avg_column_normal_2() -> None:
    """Tests the avg_column function to make sure it correctly returns an average value in a second example."""
    assert avg_column(["high,low,precipitation", "70.0,20.0,0.1", "75.5,20.2,0.2", "68.9,20.1,0.3"], "low") == 20.1