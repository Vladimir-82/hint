"""Модуль dict hints."""

from typing import TypedDict


class Student(TypedDict):
    """Класс студент."""

    name: str
    age: int
    school: str


example_1: Student = {'name': 'Tom', 'age': 2, 'school': 'Minsk'}
# example_2: Student = {'name': 1, 'age': 'Tom', 'school': 'Minsk'}
# example_3: Student = {'name': 'Tom', 'age': (2,), 'school': 'Minsk'}
# example_4: Student = {'name': 'Tom', 'age': '2', 'school': 'Minsk'}
# example_5: Student = {'name': 'Tom', 'age': 2}

assert Student(name='Tom', age=2, school='Minsk') == {'name': 'Tom', 'age': 2, 'school': 'Minsk'}
