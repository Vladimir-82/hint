"""Модуль any hints."""

from typing import Any


def foo(x: Any):
    """any hints."""
    pass


foo(1)
foo("10")
foo(1, 2)  # type: ignore
