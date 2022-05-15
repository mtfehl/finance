"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730321206"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        """Produce a string representation of a linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> Optional[int]:
    """Returns the last value of a Linked List, or None if the list is empty."""
    return None


def seq(lo: int, hi: int) -> Optional[Node]:
    """Return sequence of nodes between lo and hi, not inclusive of hi."""
    if lo >= hi:
        return None
    else:
        subproblem: int = lo
        rest: Optional[Node] = seq(lo + 1, hi)
        return Node(subproblem, rest)