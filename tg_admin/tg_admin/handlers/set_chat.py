from telegram import Update
from telegram.ext import ContextTypes
from dto import User, UserState
from db import get_user


async def set_chat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user: User = await get_user(update.message.from_user["id"])
    user.state = UserState.SETTING_CHAT
    await user.commit()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Перешлите сообщение из чата, в который хотите щитпостить.",
    )
