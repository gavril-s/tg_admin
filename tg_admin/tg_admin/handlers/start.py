from telegram import Update
from telegram.ext import ContextTypes
from dto import User
from db import get_user, add_user


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user: User = await get_user(update.message.from_user["id"])
    if user is not None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Я тебя уже где-то видел, антихайп",
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Чот я тебя не припомню, антихайп",
        )

        user_dict = update.message.from_user

        user = User(
            id=user_dict["id"],
            is_bot=user_dict["is_bot"],
            first_name=user_dict["first_name"],
            last_name=user_dict["last_name"],
            username=user_dict["username"],
            is_premium=user_dict["is_premium"],
        )
        result = await add_user(user)
        print(result)
