#Copyright 2022-present, Author: 5MysterySD

from bot.client import Client
from pyrogram import filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(c: Client, m: Message):
    ''' Start Message of the Bot !!'''

    await m.reply_photo(photo='https://te.legra.ph/file/fff361f8f1019fa5162f9.jpg',
        caption='''<b>🔰 Hello, I am UploadEver.in Uploader Bot! 🔰</b>

☃️  <i>Here you can Upload Files via Forwarding Telegram Files/ Sending Telegram File/Send UploadEver Links/ Direct Download Links to this Bot!</i>

<u>Look Like you haven't logged in yet hit /login to logged in and Use Bot Features!</u>
<code>Want to know bot features hit /help</code>

<b>💯 Bot Created By ♥️ @MysterySD ♥️ & Powered By ⚡️ UploadEver ⚡️</b>
<i>If you face any kind of Problem/Error or Feature Request, Message to @MysterySD</i>''',
        quote=True,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("🗓 Join Channel", url="https://t.me/uploadever"),
        InlineKeyboardButton("📇 Website", url="https://uploadever.in")]
        ])
    )
