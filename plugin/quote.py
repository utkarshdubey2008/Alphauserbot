from telethon import events
import requests

@events.register(events.NewMessage(pattern=r'\.quote'))
async def quote(event):
    response = requests.get("https://api.quotable.io/random")
    quote = response.json()
    await event.reply(f"{quote['content']} - {quote['author']}")
