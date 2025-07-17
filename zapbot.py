from telethon import TelegramClient, events
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
source = os.getenv("SOURCE_CHATS").split(",")
destination = os.getenv("DESTINATION_CHAT")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source))
async def handler(event):
    if event.message.media:
        await client.send_file(destination, event.message.media)
    else:
        await client.send_message(destination, event.message.message)

client.start()
client.run_until_disconnected()
