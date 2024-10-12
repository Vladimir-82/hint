"""Модуль optional."""


from typing import Optional


def foo(x: Optional[int] = None) -> None:
    """optional."""
    pass


foo(10)
foo(None)
foo()
foo("10")  # type: ignore
