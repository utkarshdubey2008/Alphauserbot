from telethon import events
import requests

@events.register(events.NewMessage(pattern=r'\.fact'))
async def fact(event):
    response = requests.get("https://api.fungenerators.com/fact/random")
    fact = response.json()["data"]["fact"]
    await event.reply(f"Did you know? {fact}")
