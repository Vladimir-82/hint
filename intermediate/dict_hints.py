"""Модуль dict hints."""

from typing import TypedDict


class Student(TypedDict):
    """Класс студент."""

    name: str
    age: int
    school: str


example_1: Student = {'name': 'Tom', 'age': 2, 'school': 'Minsk'}
example_2: Student = {'name': 1, 'age': 'Tom', 'school': 'Minsk'}  # type: ignore
example_3: Student = {'name': 'Tom', 'age': (2,), 'school': 'Minsk'}  # type: ignore
example_4: Student = {'name': 'Tom', 'age': '2', 'school': 'Minsk'}  # type: ignore
example_5: Student = {'name': 'Tom', 'age': 2}  # type: ignore

assert Student(name='Tom', age=2, school='Minsk') == {'name': 'Tom', 'age': 2, 'school': 'Minsk'}
