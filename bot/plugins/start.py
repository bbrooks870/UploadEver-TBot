from bot.client import Client
from pyrogram import filters
from pyrogram.types import Message

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(c: Client, m: Message):
    await m.reply_message(
        text="Hi, I am UploadEver.in Uploader Bot!"
    )