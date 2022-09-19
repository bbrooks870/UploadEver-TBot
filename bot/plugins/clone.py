#Copyright 2022-present, Author: 5MysterySD

from requests import get as rget
from config import LOGGER, USERS_API
from bot.client import Client
from pyrogram import filters, enums
from pyrogram.types import Message

@Client.on_message(filters.command("clone") & filters.private)
async def clone_handler(c: Client, m: Message):
    ''' Clone File from Server API:

    :param url: The UploadEver.in URL you want to Clone

    OUTPUT:
    {
        "status": 200,
        "result": {
            "url": "https://uploadever.in/r9o25tsq86ru",
            "filecode": "r9o25tsq86ru"
        },
        "msg": "OK",
        "server_time": "2022-03-09 10:49:48"
    }
    '''

    upData = m.split(' ')
    filecode = (upData[1].split("/"))[-1]
    Token = USERS_API.get(m.chat.id, None)
    if Token is None: text_ = "<b>😬 I see, you have not Login, Do <i>/login</i> to Use this Command. </b>"
    else:
        resp = rget(f"https://uploadever.in/api/file/clone?file_code={filecode}&key={Token}")
        jdata = resp.json()
        if jdata['status'] == 200:
            text_ = f"<b>🔗 Generated Cloned URL:</b> <code>{jdata['result']['url']}</code>"
        else: text_ = jdata['msg']

    await m.reply_text(text=text_, parse_mode=enums.ParseMode.HTML, quote=True)
