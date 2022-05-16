"""Linked list utility functions."""
from __future__ import annotations
from typing import Optional


class Node:
    """A simple link in a linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Constructor initializes a Node."""
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        """Produce a string representation of a linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def includes(haystack: Optional[Node], needle: int) -> bool:
    """Is needle in the haystack?"""
    print(f"{haystack}")
    if haystack == None:
        return False
    elif haystack.data == needle:
        return True
    else:
        return includes(haystack.next, needle)


courses = Node(110, Node(210, None))
print(courses)
print(includes(None, 210))
print(includes(courses, 210)) 