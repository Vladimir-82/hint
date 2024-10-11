"""Модуль empty_tuple."""


def foo(x: tuple[()]) -> None:
    """Модуль empty_tuple."""
    ...


foo(())
foo((1))  # type: ignore
