from telethon import events
import requests

@events.register(events.NewMessage(pattern=r'\.joke'))
async def joke(event):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = response.json()
    await event.reply(f"{joke['setup']}\n{joke['punchline']}")
