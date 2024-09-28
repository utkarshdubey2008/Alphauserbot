from telethon import events
import asyncio

@events.register(events.NewMessage(pattern=r'\.spam (\d+) (.+)'))
async def spam(event):
    count = int(event.pattern_match.group(1))
    message = event.pattern_match.group(2)
    
    await event.reply(f"Starting to spam {count} times!")
    
    for _ in range(count):
        await event.reply(message)
        await asyncio.sleep(1)  # Adjust delay as needed
