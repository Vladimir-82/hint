"""Модуль await."""

from collections.abc import Awaitable
from asyncio import Queue


queue: Queue[int] = Queue()
queue2: Queue[str] = Queue()


def run_async(function: Awaitable[int]) -> None:
    """Модуль await."""
    ...


async def async_function() -> int:
    """Функция 1."""
    return await queue.get()


async def async_function2() -> str:
    """Функция 2."""
    return await queue2.get()


run_async(async_function())
run_async(11)  # type: ignore
run_async(async_function2())  # type: ignore
