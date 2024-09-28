from telethon import events
from googletrans import Translator

translator = Translator()

@events.register(events.NewMessage(pattern=r'\.translate (.+) to (.+)'))
async def translate(event):
    text = event.pattern_match.group(1)
    lang = event.pattern_match.group(2)
    translated = translator.translate(text, dest=lang)
    await event.reply(f"Translation: {translated.text}")
