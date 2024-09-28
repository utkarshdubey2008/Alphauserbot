from telethon import events
from telethon.tl.types import PeerUser
from config import client  # Import the client from your config
import asyncio

# Global variable to track spam tasks
spam_tasks = {}

@client.on(events.NewMessage(pattern=r'\.spam (\d+) (.+)'))
async def spam(event):
    # Extract number of messages and the message to be spammed
    count = int(event.pattern_match.group(1))
    message = event.pattern_match.group(2)
    user_id = event.sender_id

    # Stop any previous spam task for this user
    if user_id in spam_tasks:
        await event.reply("Stopping the previous spam task.")
        spam_tasks[user_id].cancel()
        del spam_tasks[user_id]

    # Start a new spam task
    async def send_spam():
        for _ in range(count):
            await event.respond(message)
            await asyncio.sleep(1)  # Delay to avoid flooding
        del spam_tasks[user_id]

    spam_tasks[user_id] = client.loop.create_task(send_spam())
    await event.reply(f"Spamming {count} times: {message}")

@client.on(events.NewMessage(pattern=r'\.sspam'))
async def stop_spam(event):
    user_id = event.sender_id
    if user_id in spam_tasks:
        spam_tasks[user_id].cancel()
        del spam_tasks[user_id]
        await event.reply("Spam task stopped.")
    else:
        await event.reply("No active spam task to stop.")

@client.on(events.NewMessage(pattern=r'\.purge'))
async def purge(event):
    # Check if the user has admin rights
    if not await event.get_chat().get_permissions(event.sender_id).can_delete_messages:
        await event.reply("You don't have permission to delete messages.")
        return

    # Purge the last 50 messages in the chat
    async for message in event.message.get_chat_history(limit=50):
        try:
            await client.delete_messages(event.chat_id, message.id)
        except Exception as e:
            await event.reply(f"Failed to delete a message: {str(e)}")

    await event.reply("Purged the last 50 messages.")
