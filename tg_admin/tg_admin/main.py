import logging
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from config import api_id, api_hash
import handlers

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

app = Client("tg_admin", api_id=api_id, api_hash=api_hash)

app.add_handler(
    MessageHandler(handlers.start, filters.private & filters.command("start"))
)
app.add_handler(
    MessageHandler(
        handlers.set_chat, filters.private & filters.command("set_chat")
    )
)
app.add_handler(
    MessageHandler(
        handlers.help, filters.private & filters.command("help")
    )
)

logging.info("Starting...")
app.run()
logging.info("Finished")