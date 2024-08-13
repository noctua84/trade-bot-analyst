from telethon import TelegramClient
from telethon.tl.types import User


async def extract_chat_data(client: TelegramClient):
    dialogs = await client.get_dialogs()

    for dialog in dialogs:
        if isinstance(dialog.entity, User):
            print(dialog.entity.username)
