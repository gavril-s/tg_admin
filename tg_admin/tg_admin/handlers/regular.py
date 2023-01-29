from telegram import Update
from telegram.ext import ContextTypes


async def regular_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="В разработке...",
    )
