from telethon import events
from config import client
import asyncio

spam_tasks = {}

@client.on(events.NewMessage(pattern=r'\.spam (\d+) (.+)'))
async def spam(event):
    count = int(event.pattern_match.group(1))
    message = event.pattern_match.group(2)
    user_id = event.sender_id

    if user_id in spam_tasks:
        await event.reply("Stopping the previous spam task.")
        spam_tasks[user_id].cancel()
        del spam_tasks[user_id]

    async def send_spam():
        for _ in range(count):
            await event.respond(message)
            await asyncio.sleep(1)
        del spam_tasks[user_id]

    spam_tasks[user_id] = client.loop.create_task(send_spam())
    await event.reply(f"Spamming {count} times: {message}")
