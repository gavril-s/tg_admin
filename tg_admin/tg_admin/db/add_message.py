from __future__ import annotations
import psycopg2
import config
import typing as tp
from dto import Message


async def add_message(message: Message) -> bool:
    if message is None:
        return False
    sql = """
        INSERT INTO messages
            (id, local_id, user_id, from_chat_id, to_chat_id, sending_time)
        VALUES 
            (%s, %s, %s, %s, %s, %s);
    """

    connection = psycopg2.connect(
        dbname=config.db_name,
        user=config.db_user,
        password=config.db_pass,
        host=config.db_host,
        port=config.db_port,
    )
    cursor = connection.cursor()
    cursor.execute(sql, message.to_db())
    connection.commit()
    cursor.close()
    connection.close()
    return True
