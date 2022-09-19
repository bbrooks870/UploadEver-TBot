from requests import get as rget
from config import LOGGER
from bot.client import Client
from pyrogram import filters
from pyrogram.types import Message, ForceReply

USERS_API = {}

@Client.on_message(filters.command("login") & filters.private)
async def login_handler(c: Client, m: Message):
    auth_msg = await m.reply_text(text="Authorization: \n1. Your Account to Upload Contents", reply_markup=ForceReply(True, "Enter UploadEver.in API Key"))

    input_msg: Message = await c.listen(m.chat.id)
    Token = input_msg.text
    if Token is None:
        await auth_msg.delete()
        await m.reply_text("Process Cancelled!")
        return
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

@Client.on_message(filters.command("stats") & filters.private)
async def stats_handler(c: Client, m: Message):
    Token = USERS_API.get(m.chat.id, None)
    if Token is None:
        text_ = "Login First /login"
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
        resp2 = rget(f"https://uploadever.in/api/account/stats?key={Token}")
        jdata2 = resp2.json()
        if jdata2['msg'] != "OK" :
            text_ += f"Account Stats :\n\n• {jdata2['msg']}"
    await m.reply_text(text=text_)

@Client.on_message(filters.command("logout") & filters.private)
async def logout_handler(c: Client, m: Message):
    try:
        USERS_API.pop(m.chat.id)
        text_ = "Successfully LogOut"
    except KeyError:
        text_ = "Login First /login to LogOut"
    await m.reply_text(text=text_)
