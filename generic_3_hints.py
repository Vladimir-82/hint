"""Модуль generic3."""

from typing import TypeVar
from typing_extensions import assert_type


T = TypeVar('T', bound=int)


class MyInt(int):
    pass


def add(a: T) -> T:
    """Generic3."""
    return a


assert_type(add(1), int)
assert_type(add(MyInt(1)), MyInt)
# assert_type(add('1'), str)
# add(['1'], ['2'])
# add(['1', 2])
