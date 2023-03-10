import psycopg2
import config
import typing as tp
from dto import User


async def add_user(user: User) -> bool:
    if user is None:
        return False
    sql = """
        INSERT INTO users
            (id, is_bot, first_name, last_name, username, is_premium, chat_id, state)
        VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s);
    """

    connection = psycopg2.connect(
        dbname=config.db_name,
        user=config.db_user,
        password=config.db_pass,
        host=config.db_host,
        port=config.db_port,
    )
    cursor = connection.cursor()
    cursor.execute(sql, user.to_db())
    connection.commit()
    cursor.close()
    connection.close()
    return True
