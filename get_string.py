from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 33370509 
api_hash = "669af6caebf2aca264b16cf8b40d37b2"

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
