from requests import get as rget
from config import LOGGER, USERS_API
from bot.client import Client
from pyrogram import filters
from pyrogram.types import Message

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
