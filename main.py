import os
import importlib
import logging
from pyrogram import Client, filters
from config import API_ID, API_HASH, SESSION_STRING

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the Pyrogram client with the session string
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

def import_plugins():
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
    # Add your message handling logic here.

if __name__ == '__main__':
    try:
        import_plugins()  # Import plugins before running the bot
        app.run()  # Start the Pyrogram client (runs synchronously)
        logger.info("Bot is running...")
    except KeyboardInterrupt:
        logger.info("Bot has been stopped manually.")
    except Exception as e:
        logger.error(f"An error occurred while running the bot: {e}")
    finally:
        logger.info("Cleaning up resources and shutting down.")
