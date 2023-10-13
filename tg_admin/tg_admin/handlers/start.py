import logging
from dto import User, UserState
from db import get_user, add_user


async def start_handler(client, message):
    logging.info("/start")
    user: User = await get_user(message.from_user.id)
    if user is not None:
        await message.reply("Где-то я тебя уже видел")
    else:
        await message.reply("Что-то я тебя не припомню")

        user_obj = message.from_user
        user = User(
            id=user_obj.id,
            is_bot=user_obj.is_bot,
            first_name=user_obj.first_name,
            last_name=user_obj.last_name,
            username=user_obj.username,
            is_premium=user_obj.is_premium,
            chat_id=None,
            state=UserState.DEFAULT,
        )
        result = await add_user(user)
