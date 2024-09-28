from telethon import events
import asyncio

@events.register(events.NewMessage(pattern=r'\.remindme (\d+) (.+)'))
async def remindme(event):
    time = int(event.pattern_match.group(1))
    message = event.pattern_match.group(2)
    await asyncio.sleep(time * 60)  # time in minutes
    await event.reply(f"Reminder: {message}")
