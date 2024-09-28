from telethon import TelegramClient, events
import os
import importlib
from dotenv import load_dotenv

# Load environment variables from a .env file if needed
load_dotenv()

# Use os.environ.get to retrieve environment variables
API_ID = os.environ.get('API_ID', '29264175')  # Default value for local testing
API_HASH = os.environ.get('API_HASH', '0a3e78a4cd29529769faf5fe588f6de7')  # Default value for local testing
SESSION_STRING = os.environ.get('SESSION_STRING', 'your_default_session_string')  # Replace with a valid session string if needed

client = TelegramClient('user_bot', API_ID, API_HASH).start(session=SESSION_STRING)

# Import all plugins
for filename in os.listdir('plugin'):
    if filename.endswith('.py'):
        importlib.import_module(f'plugin.{filename[:-3]}')

@client.on(events.NewMessage)
async def handler(event):
    await client.process_event(event)

client.run_until_disconnected()
