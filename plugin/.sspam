from telethon import events
from config import client

spam_tasks = {}  # Ensure this is the same global variable used in spam.py

@client.on(events.NewMessage(pattern=r'\.sspam'))
async def stop_spam(event):
    user_id = event.sender_id
    if user_id in spam_tasks:
        spam_tasks[user_id].cancel()
        del spam_tasks[user_id]
        await event.reply("Spam task stopped.")
    else:
        await event.reply("No active spam task to stop.")
