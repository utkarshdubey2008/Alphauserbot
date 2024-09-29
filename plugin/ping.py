from telethon import events

@events.register(events.NewMessage(pattern=r'\.ping'))
async def ping(event):
    """Checks the bot's responsiveness."""
    await event.reply("🏓 Pong! The bot is alive and responsive.")
