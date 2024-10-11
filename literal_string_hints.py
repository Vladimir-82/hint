"""Модуль Literalstring."""

from typing import Iterable
from typing_extensions import LiteralString


def execute_query(sql: LiteralString, parameters: Iterable[str]) -> None:
    """Literalstring."""


def query_user(user_id: str) -> None:
    """"""
    query = f'SELECT * FROM users WHERE user_id = {user_id}'
    # execute_query(query)


def query_data(user_id: str, limit: bool) -> None:
    query = """SELECT * FROM data WHERE user_id = """
    if limit:
        query += "LIMIT 1"

    execute_query(query, (user_id,))
