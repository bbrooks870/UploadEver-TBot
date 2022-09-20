#Copyright 2022-present, Author: 5MysterySD

from pathlib import Path
from requests import get as rget
from config import LOGGER, USERS_API
from bot.client import Client
from pyrogram import filters, enums
from pyrogram.types import Message

@Client.on_message(filters.command("upload") & filters.private)
async def upload_file_handler(c: Client, m: Message):
    ''' Upload Telegram Files Directly to the UploadEver Server upto 4GB '''

    rpy_media = m.reply_to_message
    media = [rpy_media.document, rpy_media.video, rpy_media.audio]
    file_name = [md for md in media if md is not None][0].file_name
    __fileName = str(Path("./").resolve()) + "/"
    try:
        __downLocation = await c.download_media(message=rpy_media, file_name=__fileName)
    except Exception as err:
        await m.reply_text(f"⛔️ Error : {err}")
        LOGGER.error(err)
    await m.reply_text(__downLocation)
