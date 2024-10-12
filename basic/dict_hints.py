"""Модуль dict hints."""

from typing import Dict


def foo(x: Dict[str, str]):
    """dict hints."""
    pass


foo({"foo": "bar"})
foo({"foo": 1})  # type: ignore
