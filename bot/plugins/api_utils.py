from bot.client import Client
from pyrogram import filters
from pyrogram.types import Message, ForceReply

@Client.on_message(filters.command("login") & filters.private)
async def login_handler(c: Client, m: Message):
    await m.reply_text(text="haha", reply_markup=ForceReply(True, "Enter API Key"))
    
