from telethon import events

@events.register(events.NewMessage(pattern=r'\.music (.+)'))
async def music(event):
    search_term = event.pattern_match.group(1)
    await event.reply(f"Searching for music related to '{search_term}'...")
    # Further implementation for music search can be added.
