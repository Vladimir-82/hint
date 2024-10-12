"""Модуль tuple."""


def foo(x: tuple[str, int]):
    """tuple."""
    pass


foo(("foo", 1))
foo((1, 2))  # type: ignore
foo(("foo", "bar"))  # type: ignore
foo((1, "foo"))  # type: ignore
