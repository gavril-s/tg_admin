import psycopg2
import config
import typing as tp
from dto import User


async def add_user(user: User) -> bool:
    connection = psycopg2.connect(
        dbname=config.db_name,
        user=config.db_user,
        password=config.db_pass,
        host=config.db_host,
        port=config.db_port,
    )
    cursor = connection.cursor()
    cursor.execute(
        f"INSERT INTO users\
            (id, is_bot, first_name, last_name, username, is_premium, chat_id)\
            VALUES\
            ({user.id}, {user.is_bot}, '{user.first_name}', '{user.last_name}', '{user.username}', {user.is_premium}, {user.chat_id});"
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True
