import psycopg2
import config
import typing as tp
from dto import User, Message


async def get_user_messages(user: User) -> tp.List[Message]:
    if user is None:
        return []
    sql = """
        SELECT 
            id, local_id, user_id, from_chat_id, to_chat_id, sending_time
        FROM messages
        WHERE user_id=%s;
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
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return [Message.from_db(msg_tuple) for msg_tuple in result]
