#Copyright 2022-present, Author: 5MysterySD

from pathlib import Path
from subprocess import check_output
from requests import get as rget
from config import LOGGER, USERS_API, Config
from bot.client import Client
from pyrogram import filters, enums
from pyrogram.types import Message

@Client.on_message(filters.command("upload") & filters.private)
async def upload_file_handler(c: Client, m: Message):
    ''' Upload Telegram Files Directly to the UploadEver Server upto 4GB '''

    Token = USERS_API.get(m.chat.id, None)
    if Token is None: 
        await m.reply_text("<b>😬 I see, you have not Login, Do <i>/login</i> to Use this Command. </b>")
        return
    rpy_media = m.reply_to_message
    if not rpy_media:
        await m.reply_text("Reply to a Telegram File to Upload to UploadEver Server !!")
        return
    downMSG = await m.reply_text("Starting Downloading ...")
    media = [rpy_media.document, rpy_media.video, rpy_media.audio]
    file_name = [md for md in media if md is not None][0].file_name
    __fileName = f"{Path('./').resolve()}/{Config.DIRECTORY}"
    try:
        __downLocation = await c.download_media(message=rpy_media, file_name=__fileName)
        await downMSG.edit("Downloading ...")
    except Exception as err:
        await downMSG.edit(f"⛔️ Error : {err}")
        LOGGER.error(err)
    LOGGER.info(__downLocation)
    await downMSG.edit("Downloaded, Checking Upload Server ...")
    
    resp = rget(f"https://uploadever.in/api/upload/server?key={Token}")
    jdata = resp.json()
    if jdata['status'] == 200:
        SESS_ID = jdata['sess_id']
        UP_SER_URL = jdata['result']
    #else: Do Something 
    Data = check_output(f"curl -F 'sess_id={SESS_ID}' -F 'utype=free' -F 'file_0=@{__downLocation}' {UP_SER_URL}", shell=True).decode('utf-8')
    await m.reply_text(Data)
    
        
