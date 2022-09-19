from requests import get as rget
from config import LOGGER
from bot.client import Client
from pyrogram import filters
from pyrogram.types import Message, ForceReply

USERS_API = {}

@Client.on_message(filters.command("auth") & filters.private)
async def auth_handler(c: Client, m: Message):
    auth_msg = await m.reply_text(text="Authorization: \n1. Your Account to Upload Contents", reply_markup=ForceReply(True, "Enter UploadEver.in API Key"))

    input_msg: Message = await c.listen(m.chat.id)
    Token = input_msg.text
    if Token is None:
        await input_msg.edit("Process Cancelled!")
        return
    else:
        await input_msg.delete()
        await auth_msg.delete()
        resp = rget(f"https://uploadever.in/api/account/info?key={Token}")
        jdata = resp.json()
        USERS_API[m.chat.id] = Token
        LOGGER.info("[UploadEver.in] User Log In")
        await m.reply_text(text=f"{jdata['result']['email']} Successfully Logged In !!")

@Client.on_message(filters.command("stats") & filters.private)
async def stats_handler(c: Client, m: Message):
    Token = USERS_API.get(m.chat.id, None)
    if Token is None:
        text_ = "Login First /auth"
    else:
        resp = rget(f"https://uploadever.in/api/account/info?key={Token}")
        jdata = resp.json()
        text_ = f'''Stats:

• Email : {jdata['result']['email']}
• Balance : {jdata['result']['balance']}
• Storage Left : {jdata['result']['storage_left']}
• Storage Used : {jdata['result']['storage_used'] or 0}
• Premium Expire : {jdata['result']['premium_expire']}

• Server Time : {jdata['server_time']}

'''
        resp = rget(f"https://uploadever.in/api/account/stats?key={Token}")
        jdata = resp.json()
        if jdata['msg'] != "OK" :
            text_ += f"Account Stats :\n\n• {jdata['msg']}"
    await m.reply_text(text=text_)

