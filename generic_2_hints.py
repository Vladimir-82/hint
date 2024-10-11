"""Модуль generic2."""

from typing import TypeVar
from typing_extensions import assert_type


T = TypeVar('T', int, str)


def add(a: T, b: T) -> T:
    """Generic2."""
    return a + b


assert_type(add(1, 2), int)
assert_type(add('1', '2'), str)

# add(['1'], ['2'])
# add('1', 2)#