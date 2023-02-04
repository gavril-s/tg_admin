from __future__ import annotations
import psycopg2
import config
import typing as tp
import dto


async def get_user(id: int) -> tp.Optional[dto.User]:
    sql = """
        SELECT 
            id, is_bot, first_name, last_name, username, is_premium, chat_id, state
        FROM users
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
    cursor.execute(sql, [id])
    result = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    try:
        return dto.User.from_db(result)
    except:
        return None
