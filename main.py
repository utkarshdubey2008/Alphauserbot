from telethon import TelegramClient, events
import os
import importlib
from config import API_ID, API_HASH, SESSION_STRING  # Import from config

client = TelegramClient('user_bot', API_ID, API_HASH).start()

# Import all plugins
for filename in os.listdir('plugin'):
    if filename.endswith('.py'):
        importlib.import_module(f'plugin.{filename[:-3]}')

@client.on(events.NewMessage)
async def handler(event):
    await client.process_event(event)

client.run_until_disconnected()
