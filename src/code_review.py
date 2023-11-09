from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None


def breadth_first_search(root: Node, value: int) -> bool:
    pass
