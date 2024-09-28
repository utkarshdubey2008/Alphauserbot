from telethon import events

@events.register(events.NewMessage(pattern=r'\.echo (.+)'))
async def echo(event):
    text = event.pattern_match.group(1)
    await event.reply(text)
