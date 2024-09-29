from telethon import TelegramClient, events
import os
import importlib
from config import API_ID, API_HASH, SESSION_STRING

client = TelegramClient('user_bot', API_ID, API_HASH)

async def main():
    try:
        await client.start(SESSION_STRING)
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
        # Assuming you have a method to process the event
        print(f"Received message: {event.message.text}")
        # Your event processing logic goes here
    except Exception as e:
        print(f"An error occurred while processing an event: {e}")

if __name__ == '__main__':
    try:
        client.loop.run_until_complete(main())
    except Exception as e:
        print(f"An error occurred while running the bot: {e}")
    finally:
        client.run_until_disconnected()
