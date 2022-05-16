"""Recursive structures in python."""

from __future__ import annotations
from typing import Optional

# "head" of a linked list = reference to the first node
# singlely-Linked list: Node only references to the Node following it
# Linked list is typically written out in arrows and boxes, used to learn
# None / "null" values, references, and recursive algorithms

class Node:
    data: int = 0
    next: Optional[Node] = None

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next


def count(a_node: Optional[Node]) -> int:

    if a_node == None:
        return 0
    else:
        return 1 + count(a_node.next)



head: Node = Node(210, None)
print(count(head))
head = Node(110, head)
print(count(head))

# When testing a recursive data structure, always check to see if the structure is empty (equal to None),, this is the base case
# Also, make a recursive call on a subpart of the structure (in a singely linked list, this is the next node)

