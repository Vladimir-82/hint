"""Модуль generic."""

from typing import List, TypeVar
from typing_extensions import assert_type


T = TypeVar('T')


def add(a: T, b: T) -> T:
    """Generic."""
    return a


assert_type(add(1, 2), int)
assert_type(add('1', '2'), str)
assert_type(add(['1'], ['2']), List[str])
# assert_type(add(1, '2'), int)
