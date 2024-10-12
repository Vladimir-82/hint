"""Модуль list kwargs."""

from typing import List


def foo(x: List[str]) -> None:
    """kwargs."""
    pass


foo(["foo", "bar"])
foo(["foo", 1])  # type: ignore
