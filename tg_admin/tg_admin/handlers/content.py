from telegram import Update
from telegram.ext import ContextTypes
from db import get_user, add_message
from uuid import uuid4


async def content_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id = str(uuid4)
    user_id = update.message.from_user["id"]
    user = await get_user(user_id)
    from_chat_id = update.message.chat_id
    to_chat_id = user.chat_id
    add_message(Message(id, user_id, from_chat_id, to_chat_id))