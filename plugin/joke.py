import requests
from telethon import events

@events.register(events.NewMessage(pattern=r'\.joke'))
async def joke(event):
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    joke = response.json()
    await event.reply(f"{joke['setup']} {joke['punchline']}")
