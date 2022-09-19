from requests import get as rget
from config import LOGGER, USERS_API
from bot.client import Client
from pyrogram import filters
from pyrogram.types import Message, ForceReply

@Client.on_message(filters.command("login") & filters.private)
async def login_handler(c: Client, m: Message):
    auth_msg = await m.reply_text(text="Authorization: \n1. Your Account to Upload Contents")

    input_msg: Message = await c.listen(m.chat.id)
    Token = input_msg.text
    if Token is None:
        await auth_msg.delete()
        await m.reply_text("Process Cancelled!")
        return
    elif Token and Token.startswith("/"):
        await auth_msg.edit("Process Cancelled!")
        return await input_msg.continue_propagation()
    else:
        await input_msg.delete()
        await auth_msg.delete()
        resp = rget(f"https://uploadever.in/api/account/info?key={Token}")
        jdata = resp.json()
        if jdata["status"] == 200:
            USERS_API[m.chat.id] = Token
            LOGGER.info(f"[UploadEver.in] User: {m.chat.id} Log In Success")
            txt = f"{jdata['result']['email']} Successfully Logged In !!"
        else:
            LOGGER.info(f"[UploadEver.in] User: {m.chat.id} Log In Unsuccessful")
            txt = jdata['msg']
        await m.reply_text(text=txt)


@Client.on_message(filters.command("logout") & filters.private)
async def logout_handler(c: Client, m: Message):
    try:
        USERS_API.pop(m.chat.id)
        text_ = "Successfully LogOut"
    except KeyError:
        text_ = "Login First /login to LogOut"
    await m.reply_text(text=text_)
