"""Модуль callanle."""

from typing import Callable


SingleStringInput = Callable[[str], None]


def accept_single_string_input(func: SingleStringInput) -> None:
    """Функция 1."""
    ...


def string_name(name: str) -> None:
    """Функция 2."""
    ...


def string_value(value: str) -> None:
    """Функция 3."""
    ...


def int_value(value: int) -> None:
    """Функция 4."""
    ...


def new_name(name: str) -> str:
    """Функция 5."""
    return name


accept_single_string_input(string_name)
accept_single_string_input(string_value)
# accept_single_string_input(int_value)
# accept_single_string_input(new_name)
