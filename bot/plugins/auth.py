#Copyright 2022-present, Author: 5MysterySD

from asyncio import sleep as asleep
from requests import get as rget
from config import LOGGER, USERS_API
from bot.client import Client
from pyrogram import filters, enums
from pyrogram.types import Message, ForceReply

@Client.on_message(filters.command("login") & filters.private)
async def login_handler(c: Client, m: Message):
    ''' Login Into Bot to Use Bot Features
    :param token: Your Own API token of UploadEver.in
    '''

    if m.chat.id in USERS_API.keys():
        await m.reply_text(text="<b>😑 You have Already Login,</b> <i>If you want to Logout, Use /logout</i>", parse_mode=enums.ParseMode.HTML, quote=True)
        return
    auth_msg = await m.reply_text(text="🖨 <b>Bot Authorization:</b> \n\n<i>You can Get/Generate/Copy API Token from https://uploadever.in/?op=my_account</i>", parse_mode=enums.ParseMode.HTML, reply_markup=ForceReply(True, "Enter UploadEver.in API Key"))
    input_msg: Message = await c.listen(m.chat.id)
    Token = input_msg.text
    if Token is None:
        await auth_msg.delete()
        await m.reply_text("<b>👤 Login Process Cancelled!!</b>")
        return await input_msg.continue_propagation()
    elif Token and Token.startswith("/"):
        await auth_msg.delete()
        await m.reply_text("<b>👤 Login Process Cancelled!</b>")
        return await input_msg.continue_propagation()
    else:
        await input_msg.delete()
        await auth_msg.delete()
        await asleep(2)
        resp = rget(f"https://uploadever.in/api/account/info?key={Token}")
        jdata = resp.json()
        if jdata["status"] == 200:
            USERS_API[m.chat.id] = Token
            LOGGER.info(f"[UploadEver.in] User: {m.chat.id} Log In Success")
            txt = f"<i>{jdata['result']['email']} Successfully Logged In ✅️!!</i>"
        else:
            LOGGER.info(f"[UploadEver.in] User: {m.chat.id} Log In Unsuccessful")
            txt = jdata['msg']
        await m.reply_text(text=txt, parse_mode=enums.ParseMode.HTML, quote=True)


@Client.on_message(filters.command("logout") & filters.private)
async def logout_handler(c: Client, m: Message):
    ''' Logout from Bot to Disable Bot Features
    :param token: Your Own API token of UploadEver.in
    '''

    try:
        USERS_API.pop(m.chat.id)
        text_ = "<i>🥲 You Successfully Logout.</i> <b>Do /login to Come Again<b>"
    except KeyError:
        text_ = "<b>😬 I see, you have not Login, Do <i>/login</i> to Use this Command. </b>"
    await m.reply_text(text=text_, parse_mode=enums.ParseMode.HTML, quote=True)
