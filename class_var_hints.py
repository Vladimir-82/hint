"""Модуль class_var."""

from typing import ClassVar


class Foo:

    """Модуль class_var."""
    bar: ClassVar[int]


Foo.bar = 1
# Foo.bar = '1'
# Foo().bar = 2
