"""Модуль dict hints 2."""

from typing import TypedDict
from typing_extensions import Required


class Person(TypedDict, total=False):
    """Класс Person."""

    name: Required[str]
    age: int
    gender: str
    address: str
    email: str


example_1: Person = {
    'name': 'Capy',
    'age': 1,
    'gender': 'Male',
    'address': 'earth',
    'email': 'capy@bara.com',
}
example_2: Person = {'name': 'Capy'}

example_3: Person = {'age': 1, 'gender': "'Male", 'address': '', 'email': ''}  # type: ignore
