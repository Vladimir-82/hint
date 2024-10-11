"""Модуль decorator."""

from typing import Callable, TypeVar


T = TypeVar("T", bound=Callable)


def decorator(func: T) -> T:
    """Декоратор."""
    return func


@decorator
def foo(a: int, *, b: str) -> None:
    """Функция 1."""
    ...


@decorator
def bar(c: int, d: str) -> None:
    """Функция 2."""
    ...


foo(1, b='2')
bar(c=1, d='2')

# foo(1, '2')
# foo(a=1, e='2')
# decorator(10)
