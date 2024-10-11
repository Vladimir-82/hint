"""Модуль unpack."""

from typing import TypedDict
from typing_extensions import Unpack


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]) -> None:
    """Распаковка словаря."""
    ...


person: Person = {'name': 'The Meaning of Life', 'age': 1983}
foo(**person)
# foo(**{'name': 'Brian'})

person2: dict[str, object] = {'name': 'Brian', 'age': 20}
# foo(**person2)
# foo(**{'name': 'Brian', 'age': '1979'})
