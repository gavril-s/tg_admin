import psycopg2
import config
import typing as tp
from dto import User


async def delete_user(user: User) -> bool:
    if user is None:
        return False
    sql = """
        DELETE FROM users
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
    cursor.execute(sql, [user.id])
    connection.commit()
    cursor.close()
    connection.close()
    return True
