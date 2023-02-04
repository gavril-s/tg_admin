from __future__ import annotations
import psycopg2
import config
import typing as tp
from dto import Message


async def delete_message(message: Message) -> bool:
    if message is None:
        return False
    sql = """
        DELETE FROM messages
        WHERE id=%s;
    """

    connection = psycopg2.connect(
        dbname=config.db_name,
        user=config.db_user,
        password=config.db_pass,
        host=config.db_host,
        port=config.db_port,
    )
    cursor = connection.cursor()
    cursor.execute(sql, [message.id])
    connection.commit()
    cursor.close()
    connection.close()
    return True
