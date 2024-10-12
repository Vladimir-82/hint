"""Модуль dict kwargs."""

from typing import Union


def foo(**kwargs: Union[int, str]) -> None:
    """kwargs."""
    pass


foo(a=1, b="2")
foo(a=[1])  # type: ignore
