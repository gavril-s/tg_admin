import psycopg2
import config
import typing as tp
from dto import Message


async def add_message(message: Message) -> bool:
    connection = psycopg2.connect(
        dbname=config.db_name,
        user=config.db_user,
        password=config.db_pass,
        host=config.db_host,
        port=config.db_port,
    )
    cursor = connection.cursor()
    cursor.execute(
        f"INSERT INTO messages\
            (id, user_id, from_chat_id, to_chat_id, sending_time)\
            VALUES\
            ({message.id}, {message.user_id}, '{message.from_chat_id}', '{message.to_chat_id}', NULL);"
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True