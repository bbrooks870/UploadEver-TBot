from math import floor
from time import time
from asyncio import sleep as asleep
import bot
from bot.core.display import convertBytes, convertTime
from config import LOGGER
from typing import Union
from pyrogram import enums
from pyrogram.types import Message, CallbackQuery
from pyrogram.errors import FloodWait

async def progress_for_pyrogram(current, total, top_msg, message: Union[Message, CallbackQuery], start):
    now = time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = convertTime(round(diff) * 1000)
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = convertTime((round(diff) * 1000) + time_to_completion)

        tmsg = "<code>[{0}{1}]</code>".format(
            ''.join(["▰" for _ in range(floor(percentage / 5))]),
            ''.join(["▱" for _ in range(20 - floor(percentage / 5))])
            )
        
        tmsg += f''' <code>{round(percentage, 2)}%</code>

🛟 <b>Sᴛᴀᴛᴜs:</b> <i>Downloading 📥</i>

🗄 <b>Dᴏᴡɴʟᴏᴀᴅᴇᴅ:</b> <i>{convertBytes(current)} of {convertBytes(total)}</i>
🚀 <b>Sᴘᴇᴇᴅ:</b> <i>{convertBytes(speed)}/s</i>
🚦 <b>Esᴛɪᴍᴀᴛᴇᴅ Tɪᴍᴇ: <i>{estimated_total_time if estimated_total_time != '' else "0 s"}</i>
'''
        try:
            await message.edit_text(
                text=f"{top_msg}\n\n{tmsg}",
                parse_mode=enums.ParseMode.HTML,
                disable_web_page_preview=True
            )
        except FloodWait as e:
            await asleep(e.value)
        except Exception as e:
            LOGGER.info(e)
