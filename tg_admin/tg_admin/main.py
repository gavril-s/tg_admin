import config
import handlers
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    application = ApplicationBuilder().token(config.bot_token).build()

    start_handler = CommandHandler("start", handlers.start)
    application.add_handler(start_handler)

    application.run_polling()
