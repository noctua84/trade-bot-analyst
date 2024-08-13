from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest


async def extract_message_history(client: TelegramClient, chat: str, limit: int) -> list:
    """
    Function to extract message history from a given chat.
    :param client: Telegram client
    :param chat: Chat name
    :param limit: Number of messages to extract
    """

    entity = await client.get_entity(chat)
    offset_id = 0
    chat_history = []

    while len(chat_history) < limit:
        history = await client(GetHistoryRequest(
            peer=entity,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            max_id=0,
            min_id=0,
            hash=0,
            limit=100
        ))

        if not history.messages:
            break

        chat_history.extend(history.messages)
        offset_id = history.messages[-1].id

    return chat_history


async def extract_recent_messages(client: TelegramClient, chat: str, limit: int) -> list:
    """
    Function to extract recent messages
    :param client: Telegram client
    :param chat: Chat name
    :param limit: Number of messages to extract
    :return: list
    """
    entity = await client.get_entity(chat)

    all_messages = await client.get_messages(entity, limit=limit)

    print(len(all_messages))

    return all_messages
