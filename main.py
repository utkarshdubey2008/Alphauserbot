from telethon import TelegramClient, events
from telethon.sessions import StringSession  # Import StringSession
import os
import importlib
from config import API_ID, API_HASH, SESSION_STRING

# Initialize the client using StringSession
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    try:
        await client.start()  # No need to pass SESSION_STRING here
        print("Client started successfully.")

        # Import all plugins after the client starts successfully
        for filename in os.listdir('plugin'):
            if filename.endswith('.py'):
                try:
                    importlib.import_module(f'plugin.{filename[:-3]}')
                    print(f"Successfully imported plugin: {filename}")
                except Exception as e:
                    print(f"Failed to import plugin {filename}: {e}")

    except Exception as e:
        print(f"An error occurred while starting the client: {e}")

@client.on(events.NewMessage)
async def handler(event):
    try:
        print(f"Received message: {event.message.text}")
    except Exception as e:
        print(f"An error occurred while processing an event: {e}")

if __name__ == '__main__':
    try:
        client.loop.run_until_complete(main())
    except Exception as e:
        print(f"An error occurred while running the bot: {e}")
    finally:
        client.run_until_disconnected()
