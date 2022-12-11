from typing import List

import mypy


def add_numbers(a: int, b: int, c: int) -> int:
    return a + b + c

# mypy filename.py
print(add_numbers(1, 2, 3))

x: List[List[int]] = []

