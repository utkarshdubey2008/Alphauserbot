import os
import importlib
import logging
from pyrogram import Client, filters
from config import API_ID, API_HASH, SESSION_STRING

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the client
app = Client(SESSION_STRING, api_id=API_ID, api_hash=API_HASH)

async def start_client():
    """Start the Pyrogram client and import plugins."""
    await app.start()
    logger.info("Client started successfully.")

    await import_plugins()  # Import all plugins after the client starts successfully

async def import_plugins():
    """Import all plugin modules from the 'plugin' directory."""
    plugin_dir = 'plugin'
    
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py'):
            try:
                importlib.import_module(f'{plugin_dir}.{filename[:-3]}')
                logger.info(f"Successfully imported plugin: {filename}")
            except Exception as e:
                logger.error(f"Failed to import plugin {filename}: {e}")

@app.on_message(filters.text)
async def handler(client, message):
    """Handle new incoming messages."""
    logger.info(f"Received message: {message.text}")
    # Additional handling logic can be added here if needed.

if __name__ == '__main__':
    try:
        app.run()  # Start the Pyrogram client
        logger.info("Bot is running...")
    except KeyboardInterrupt:
        logger.info("Bot has been stopped manually.")
    except Exception as e:
        logger.error(f"An error occurred while running the bot: {e}")
