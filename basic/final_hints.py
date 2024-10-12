"""Модуль dict final."""

from typing import Final, List


my_list: Final[List[int]] = []

my_list.append(1)
my_list = []  # type: ignore
my_list = "something else"  # type: ignore
