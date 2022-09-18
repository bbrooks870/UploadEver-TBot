from bot.client import Client
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(c: Client, m: Message):
    await m.reply_text(
        text="Hi, I am UploadEver.in Uploader Bot!"
        quote=True,
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Join Channel", url="https://t.me/uploadever")]
        ])
    )
