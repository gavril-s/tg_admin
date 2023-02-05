import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

import handlers
import config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    application = ApplicationBuilder().token(config.bot_token).build()

    start_handler = CommandHandler("start", handlers.start)
    help_handler = CommandHandler("help", handlers.help)
    post_handler = CommandHandler("post", handlers.post)
    regular_handler = CommandHandler("regular", handlers.regular)
    set_chat_handler = CommandHandler("set_chat", handlers.set_chat)
    stat_handler = CommandHandler("stat", handlers.stat)
    content_handler = MessageHandler(~filters.COMMAND, handlers.content)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(post_handler)
    application.add_handler(regular_handler)
    application.add_handler(set_chat_handler)
    application.add_handler(stat_handler)
    application.add_handler(content_handler)
    
    application.run_polling()
