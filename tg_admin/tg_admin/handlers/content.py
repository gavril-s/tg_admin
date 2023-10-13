import logging
from dto import User, UserState, Message
from db import get_user, add_message
from uuid import uuid4


async def content_handler(client, message):
    logging.info("content")

    user_id: int = message.from_user.id
    user: User = await get_user(user_id)
    if user is None:
        return

    if user.state == UserState.DEFAULT:
        if user.chat_id is None:
            await message.reply(
                "Сначала установите чат для щитпоста (/set_chat)"
            )
        else:
            id = str(uuid4())
            local_id = message.id
            from_chat_id = message.chat.id
            to_chat_id = user.chat_id
            message = Message(
                id, local_id, user_id, from_chat_id, to_chat_id, None
            )
            await add_message(message)
    elif user.state == UserState.SETTING_CHAT:
        chat = message.forward_from_chat
        if chat is not None:
            # rights = chat.admin_rights
            if True:  # rights.post_messages:
                user.chat_id = chat.id
                await message.reply("Принято.")
            else:
                await message.reply("Вы не админ в этом чате!")
        else:
            await message.reply("Это сообщение ни от кого не переслано!")
    elif user.state == UserState.ADDING_REGULAR:
        pass
    else:
        pass

    user.state = UserState.DEFAULT
    await user.commit()
