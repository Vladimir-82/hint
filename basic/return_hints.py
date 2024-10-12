"""Модуль return."""

from typing_extensions import assert_type


def foo() -> int:
    """return."""
    return 1


assert_type(foo(), int)
assert_type(foo(), str)  # type: ignore
