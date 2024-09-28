from telethon import events

@events.register(events.NewMessage(pattern=r'\.poll (.+)'))
async def poll(event):
    question = event.pattern_match.group(1)
    await event.reply(f"Poll created: {question}")
    # Further implementation for creating a poll can be added.
