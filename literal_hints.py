"""Модуль Literalstring."""

from typing import Literal


def foo(direction: Literal['left', 'right']) -> None:
    """Literal."""
    ...


foo('left')
foo('right')

a = ''.join(['r', 'i', 'g', 'h', 't'])
# foo(a)
