from telethon import events
import random

@events.register(events.NewMessage(pattern=r'\.roll'))
async def roll(event):
    result = random.randint(1, 6)
    await event.reply(f"You rolled a {result}.")
