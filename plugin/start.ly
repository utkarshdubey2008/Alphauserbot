from telethon import events

@events.register(events.NewMessage(pattern=r'\.start'))
async def start(event):
    await event.reply("Welcome to the User Bot! Use .help to see available commands.")
