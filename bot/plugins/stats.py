#Copyright 2022-present, Author: 5MysterySD

from requests import get as rget
from pyrogram import filters, enums
from pyrogram.types import Message

from bot.client import Client
from config import LOGGER, USERS_API
from bot.core.display import convertBytes

@Client.on_message(filters.command("stats") & filters.private)
async def stats_handler(c: Client, m: Message):
    ''' UploadEver Account Stats Fetched from API
    :param token: Your Own API token of UploadEver.in

    OUTPUT:
    
    '''

    Token = USERS_API.get(m.chat.id, None)
    if Token is None:
        text_ = "<b>😬 I see, you have not Login, Do <i>/login</i> to Use this Command. </b>"
    else:
        resp = rget(f"https://uploadever.in/api/account/info?key={Token}")
        jdata = resp.json()
        text_ = f'''<b>🗄 Your Account Info:</b>

• 📮 <b>Email :</b> <i>{jdata['result']['email']}</i>
• 💸 <b>Balance :</b> <code>{jdata['result']['balance']}</code>
• 📭 <b>Storage Left :</b> <code>{'Unlimited' if jdata['result']['storage_left'] == 'inf' else jdata['result']['storage_left']}</code>
• 📬 <b>Storage Used :</b> <code>{0 if jdata['result']['storage_used'] == null else convertBytes(jdata['result']['storage_used'])}</code>
• ⚠️ <b>Premium Expire :</b> <code>{jdata['result']['premium_expire']}</code>

• ♻️ <b>Server Time :</b> <code>{jdata['server_time']}</code>

'''
        resp2 = rget(f"https://uploadever.in/api/account/stats?key={Token}")
        jdata2 = resp2.json()
        if jdata2['msg'] != "OK" :
            text_ += f"<b>🗃 Your Account Stats :</b>\n\n• <b>{jdata2['msg']}</b>"

    await m.reply_text(text=text_, parse_mode=enums.ParseMode.HTML, quote=True)
