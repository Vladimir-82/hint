"""Модуль tuple_alias."""

from typing import List


Vector = List[float]

def foo(v: Vector) -> None:
    """tuple_alias."""
    pass


foo([1.1, 2])    
foo(1)  # type: ignore
foo(["1"])  # type: ignore
