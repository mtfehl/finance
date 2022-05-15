"""Tests for linked list utils."""


from exercises.ex06.linked_lists import Node, last

__author__ = "730321206"


def test_last_empty() -> None:
    """Last of an empty List should be the empty list."""
    assert last(None) == None


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3