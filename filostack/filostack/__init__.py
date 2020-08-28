"""
Module information
"""
from typing import Any


class Filostack:
    def __init__(self) -> None:
        self.items: list = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        return self.items.pop()

    def length(self) -> int:
        return len(self.items)
