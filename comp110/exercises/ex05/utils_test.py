"""Use of pytests to test the skeleton and finished functions for ex05."""
__author__ = "730321206"
import pytest
from exercises.ex05.utils import count, all, max, is_equal, concat, sub, splice
from typing import List


def test_use_count_multiple_ints() -> None:
    """Tests the count function with more than one int."""
    assert count([1, 0, 1], 1) == 2


def test_use_count_single_int() -> None:
    """Tests the count function for only one single int."""
    assert count([2], 2) == 1


def test_edge_count_empty_list() -> None:
    """Tests the count function when the given list is empty."""
    assert count([], 5) == 0


def test_use_all_true_same_int() -> None:
    """Tests the all function for when all of the ints are the same."""
    assert all([1, 1, 1, 1], 1) is True


def test_use_all_false() -> None:
    """Tests the all function for when the ints are not all the same."""
    assert all([1, 2, 3, 4], 2) is False


def test_edge_all_single_int() -> None:
    """Tests the all function with only one single int in the list."""
    assert all([1], 1) is True


def test_edge_all_empty_list() -> None:
    """Tests the all function when the given list is empty."""
    assert all([], 2) is False


def test_edge_max_of_empty() -> None:
    """Calling the 'max' function with an empty List should raise a Value Error."""
    with pytest.raises(ValueError):
        empty_list: List[int] = []
        max(empty_list)
    

def test_use_max_normal_case() -> None:
    """Tests the max function when the largest int out of multiple ints is found."""
    assert max([1, 10, 100]) == 100


def test_use_max_multiple_int() -> None:
    """Tests the max function with large ints in a large list."""
    assert max([1, 10284, 12383372394, 18, 243, 5665, 1234]) == 12383372394


def test_edge_max_single_int() -> None:
    """Tests the max function when only one int is present."""
    assert max([500]) == 500


def test_use_is_equal_true() -> None:
    """Tests the is equal function when both lists are equal."""
    assert is_equal([1, 2, 3], [1, 2, 3]) is True


def test_use_is_equal_false() -> None:
    """Tests the is equal function when the lists are not equal."""
    assert is_equal([1, 2, 3], [3, 2, 1]) is False


def test_edge_is_equal_both_empty() -> None:
    """Tests the is equal function when both the lists are empty."""
    assert is_equal([], []) is True


def test_edge_is_equal_one_empty() -> None:
    """Tests the is equal function when only one list is empty."""
    assert is_equal([1, 5], []) is False


def test_use_concat_normal() -> None:
    """Tests the concat function when both lists are successfully combined."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_use_concat_same_numbers() -> None:
    """Tests the concat function when larger lists are combined."""
    assert concat([0, 2, 2, 0], [0, 2, 2, 0]) == [0, 2, 2, 0, 0, 2, 2, 0]


def test_edge_concat_empty() -> None:
    """Tests the concat function when both lists are empty."""
    assert concat([], []) == []


def test_use_sub_usual() -> None:
    """Tests the sub function when it works in a normal case and returns the appropriate list."""
    assert sub([1, 2, 3, 4, 5], 1, 3) == [2, 3]


def test_use_sub_two_int() -> None:
    """Tests the sub function when only two ints are present."""
    assert sub([1, 2], 0, 1) == [1]


def test_edge_sub_empty() -> None:
    """Tests the sub function when the given list is empty."""
    assert sub([], 0, 4) == []


def test_use_splice_2_and_2_middle() -> None:
    """Tests the splice function when both lists have two ints, in a typical case."""
    assert splice([1, 1], 2, [0, 0]) == [1, 0, 0, 1]


def test_use_splice_8_number_list_end_of_list() -> None:
    """Tests the splice function with two lists of four int each."""
    assert splice([1, 2, 3, 4], 4, [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_edge_splice_backwards() -> None:
    """Tests the splice function with the second list spliced before the first list."""
    assert splice([1, 2], 0, [4, 8]) == [4, 8, 1, 2]