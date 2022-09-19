from requests import get as rget
from config import LOGGER
from bot.client import Client
from pyrogram import filters
from pyrogram.types import Message, ForceReply

@Client.on_message(filters.command("auth") & filters.private)
async def auth_handler(c: Client, m: Message):
    auth_msg = await m.reply_text(text="Auth Your Account to Upload Contents", reply_markup=ForceReply(True, "Enter UploadEver.in API Key"))

    input_msg: Message = await c.listen(m.chat.id)
    Token = input_msg.text
    if Token is None:
        await input_msg.edit("Process Cancelled!")
        return
    else:
        await input_msg.delete()
        resp = rget(f"https://uploadever.in/api/account/info?key={Token}")
        jdata = resp.json()
        LOGGER.info("[UploadEver.in] User Log In")
        await auth_msg.edit_text(text=f"{jdata['result']['email']} Successfully Logged In !!")
