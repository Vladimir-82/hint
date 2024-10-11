"""Модуль self hints."""

from typing import TypeVar

T = TypeVar('T', bound='Foo')


class Foo:
    """Класс."""

    def return_self(self: T) -> T:
        """Возврачает self."""
        return self


class SubFoo(Foo):
    pass


foo_1: Foo = Foo().return_self()
foo_2: SubFoo = SubFoo().return_self()

# foo_3: SubFoo = Foo.return_self()
