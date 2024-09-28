from telethon import events
from config import client
import random

abuses = [
    "Teri maa ka bhosda 💦✊🏻",
    # ... other abuses
]

@client.on(events.NewMessage(pattern=r'\.raid (\w+)'))
async def raid(event):
    username = event.pattern_match.group(1)
    if username:
        await event.reply(f"@{username} {random.choice(abuses)}")
    else:
        await event.reply("Please provide a username to raid.")

@client.on(events.NewMessage(pattern=r'\.draid'))
async def stop_raid(event):
    await event.reply("Raid has been stopped.")
