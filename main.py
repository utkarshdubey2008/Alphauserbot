from telethon import TelegramClient, events
import os
import importlib
from config import API_ID, API_HASH, SESSION_STRING  # Import from config

client = TelegramClient('user_bot', API_ID, API_HASH)

async def main():
    try:
        await client.start(session=SESSION_STRING)
    except Exception as e:
        print(f"An error occurred while starting the client: {e}")

# Import all plugins
for filename in os.listdir('plugin'):
    if filename.endswith('.py'):
        try:
            importlib.import_module(f'plugin.{filename[:-3]}')
        except Exception as e:
            print(f"Failed to import plugin {filename}: {e}")

@client.on(events.NewMessage)
async def handler(event):
    try:
        await client.process_event(event)  # Ensure this method exists
    except Exception as e:
        print(f"An error occurred while processing an event: {e}")

if __name__ == '__main__':
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
