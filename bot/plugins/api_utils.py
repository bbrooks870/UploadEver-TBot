import json
from requests import get as rget

from bot.client import Client
from pyrogram import filters
from pyrogram.types import Message, ForceReply

@Client.on_message(filters.command("login") & filters.private)
async def login_handler(c: Client, m: Message):
    await m.reply_text(text="Auth Your Account to Upload Contents", reply_markup=ForceReply(True, "Enter UploadEver API Key"))

    input_msg = await c.listen(m.chat.id)
    Token = input_msg.text
    if Token is None:
        await editable.edit("Process Cancelled!")
        return
    else:
        resp = rget(f"https://uploadever.in/api/account/info?key={Token}")
        jdata = resp.json()
        m.reply_text(json)
