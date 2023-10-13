import logging


async def help_handler(client, message):
    logging.info("/help")
    await message.reply("В разработке...")
