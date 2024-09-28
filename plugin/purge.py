from telethon import events
from config import client

@client.on(events.NewMessage(pattern=r'\.purge'))
async def purge(event):
    if not await event.get_chat().get_permissions(event.sender_id).can_delete_messages:
        await event.reply("You don't have permission to delete messages.")
        return

    async for message in event.message.get_chat_history(limit=50):
        try:
            await client.delete_messages(event.chat_id, message.id)
        except Exception as e:
            await event.reply(f"Failed to delete a message: {str(e)}")

    await event.reply("Purged the last 50 messages.")
