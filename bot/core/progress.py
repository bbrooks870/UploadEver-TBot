from math import floor
from time import time
from asyncio import sleep as asleep
import bot
from bot.core.display import convertBytes, convertTime
from config import LOGGER
from typing import Union
from pyrogram.types import Message, CallbackQuery
from pyrogram.errors import FloodWait


async def progress_for_pyrogram(current, total, ud_type, message: Union[Message, CallbackQuery], start):
    now = time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = convertTime(round(diff) * 1000)
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = convertTime((round(diff) * 1000) + time_to_completion)

        tmsg = "[{0}{1}] \n".format(
            ''.join(["●" for _ in range(floor(percentage / 5))]),
            ''.join(["○" for _ in range(20 - floor(percentage / 5))])
            )
        tmsg += f'''
⏳ **Percentage:** `{round(percentage, 2)}%`
✅ **Done:** `{convertBytes(current)}`
💠 **Total:** `{convertBytes(total)}`
📶 **Speed:** `{convertBytes(speed)}/s`
🕰 **ETA:** `{estimated_total_time if estimated_total_time != '' else "0 s"}`
'''
        LOGGER.info("Jelp dykgzjfjfzjgxjjzfxkg kg,kgxkg kg kg ")
        try:
            await message.edit_text(
                text=f"{ud_type}\n\n{tmp}",
                parse_mode=enums.ParseMode.MARKDOWN
            )
        except FloodWait as e:
            await asleep(e.value)
        except Exception:
            pass
