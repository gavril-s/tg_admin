import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import handlers
import config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    application = ApplicationBuilder().token(config.bot_token).build()

    start_handler = CommandHandler("start", handlers.start)
    help_handler = CommandHandler("help", handlers.help)
    application.add_handler(start_handler)
    application.add_handler(help_handler)

    application.run_polling()
