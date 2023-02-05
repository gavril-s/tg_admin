from telegram import Update
from telegram.ext import ContextTypes
from dto import User, UserState, Message
from db import get_user, add_message
from uuid import uuid4


async def content_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post is not None:
        pass # channel post
    elif update.message is not None:
        user_id: int = update.message.from_user["id"]
        user: User = await get_user(user_id)
        if user is None:
            return

        if user.state == UserState.DEFAULT:
            if user.chat_id is None:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="Сначала установите чат для щитпоста (/set_chat)",
                )
            else:
                id = str(uuid4())
                local_id = update.message.id
                from_chat_id = update.message.chat_id
                to_chat_id = user.chat_id
                message = Message(id, local_id, user_id, from_chat_id, to_chat_id, None)
                await add_message(message)
        elif user.state == UserState.SETTING_CHAT:
            chat = update.message.forward_from_chat
            if chat is not None:
                user.chat_id = chat.id
            else:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="Это сообщение ни от кого не переслано!",
                )
        elif user.state == UserState.ADDING_REGULAR:
            pass
        else:
            pass

        user.state = UserState.DEFAULT
        await user.commit()
