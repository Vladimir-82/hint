"""Модуль instance var."""

from typing import ClassVar


class Foo:
    """Класс с переменной."""
    bar: int


foo = Foo()
foo.bar = 42
foo.bar = '1'  # type: ignore
