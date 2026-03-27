import requests
from telethon import TelegramClient

api_id = 33370509
api_hash = "669af6caebf2aca264b16cf8b40d37b2"

client = TelegramClient("scrape", api_id, api_hash)

async def main():
    await client.start()

    users = []

    async for u in client.iter_participants(-1001492325666):
        if not u.bot and not u.deleted:
            users.append({
                "id": u.id,
                "name": u.first_name or "User"
            })

    print(f"Total user keambil: {len(users)}")

    requests.post("http://127.0.0.1:5000/save", json={
        "chat_id": "-1001492325666",
        "users": users
    })

    print("✅ berhasil kirim ke API")

with client:
    client.loop.run_until_complete(main())
