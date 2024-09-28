from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
SESSION_STRING = os.getenv('SESSION_STRING')

client = TelegramClient('user_bot', API_ID, API_HASH).start(session=SESSION_STRING)

# Import all plugins
for filename in os.listdir('plugin'):
    if filename.endswith('.py'):
        importlib.import_module(f'plugin.{filename[:-3]}')

@client.on(events.NewMessage)
async def handler(event):
    await client.process_event(event)

client.run_until_disconnected()
