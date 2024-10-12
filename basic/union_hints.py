"""Модуль union."""

from typing import Union


def foo(x: Union[str, int]) -> None:
    """union."""
    pass


foo("foo")
foo(1)
foo([])  # type: ignore
