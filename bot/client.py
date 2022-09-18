from typing import Union
from pyromod import listen
from pyrogram import Client as pyClient
from pyrogram.storage import Storage
from configs import Config, LOGGER

class Client(pyClient):
    """ Custom Bot Class """

    def __init__(self, session_name: Union[str, Storage] = "UploadEver-Bot"):
        super().__init__(
            session_name,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(
                root="bot/plugins"
            )
        )

    async def start(self):
        await super().start()
        LOGGER.info("Bot Started!")

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("Bot Stopped!")
