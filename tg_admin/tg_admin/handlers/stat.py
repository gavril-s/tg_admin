import logging
import datetime
import dateutil.relativedelta
from dto import User, UserState, ChannelStat
from db import get_user


async def stat_handler(client, message):
    logging.info("/stat")

    user: User = await get_user(message.from_user.id)
    if user is not None and user.chat_id is not None:
        stat = ChannelStat()
        target_date = (
            datetime.datetime.today()
            - dateutil.relativedelta.relativedelta(months=1)
        )
        async for msg in client.get_chat_history(user.chat_id):
            #if msg.date < target_date:
            #    break
            stat.add(msg)

        res = stat.in_chunks()
        for chunk in res:
            await message.reply(chunk, disable_web_page_preview=True)
