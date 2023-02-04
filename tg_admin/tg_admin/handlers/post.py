import telegram
from telegram import Update
from telegram.ext import ContextTypes
from db import get_user, get_user_messages, delete_message
from dto import User, UserState
from time import sleep

async def post_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user: User = await get_user(update.message.from_user["id"])

    if user.chat_id is not None:
        messages = await get_user_messages(user)
        for message in messages:
            res = await context.bot.copy_message(
                    message.to_chat_id, user.id, message.local_id
                )
            if res is not None:
                await delete_message(message)
            sleep(0.5)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Запостил, проверяй.",
    )
