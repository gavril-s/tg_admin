import logging
from dto import User, UserState
from db import get_user


async def set_chat_handler(client, message):
    logging.info("/set_chat")
    user: User = await get_user(message.from_user.id)
    if user is None:
        return

    user.state = UserState.SETTING_CHAT
    await user.commit()
    await message.reply(
        "Перешлите сообщение из чата, в который хотите щитпостить"
    )
