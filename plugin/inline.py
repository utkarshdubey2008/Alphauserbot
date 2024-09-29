import time
from datetime import datetime
from telethon import Button, events
from telethon.tl.types import InputWebDocument

# Bot Information
OWNER_NAME = "Alphabotz"
SUP_BUTTONS = [
    [Button.url("Repo📦", url="https://github.com/alphauserbot"), 
     Button.url("Support", url="t.me/alphabotzchat")]
]

# Placeholder for an image link
IMAGE_LINK = "https://example.com/sample.jpg"  # Update this with your own image URL

# Create a handler for inline commands
@events.register(events.NewMessage(pattern="/start"))
async def start_handler(event):
    """Handles /start command"""
    await event.respond(
        f"**Hello! Welcome to {OWNER_NAME} UserBot!**\nPress the buttons below for more info.",
        buttons=SUP_BUTTONS
    )

# Create an inline button that sends a message with buttons
@events.register(events.InlineQuery)
async def inline_alive(event):
    """Handles inline queries for bot alive check"""
    MSG = f"• **{OWNER_NAME} Userbot •**"
    WEB0 = InputWebDocument(IMAGE_LINK, 0, "image/jpg", [])
    result = await event.builder.article(
        title=f"{OWNER_NAME} Userbot",
        description="A simple userbot in Telethon Library",
        text=MSG,
        thumb=WEB0,
        buttons=SUP_BUTTONS
    )
    await event.answer([result], private=True, cache_time=300)

# Ping and Uptime Handlers
start_time = time.time()

@events.register(events.CallbackQuery(data="ping"))
async def ping_handler(event):
    """Handles ping"""
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds
    await event.answer(f"Pong! {ms} microseconds", alert=True)

@events.register(events.CallbackQuery(data="uptime"))
async def uptime_handler(event):
    """Handles uptime"""
    uptime = time.time() - start_time
    formatted_uptime = str(datetime.utcfromtimestamp(uptime).strftime('%H:%M:%S'))
    await event.answer(f"Uptime: {formatted_uptime}", alert=True)

# Register a menu for Help
@events.register(events.CallbackQuery(data="help"))
async def help_handler(event):
    """Handles help menu"""
    help_text = f"Hello, I am {OWNER_NAME}'s Userbot! Here are my commands:\n\n/start - Start the bot\n/ping - Check ping\n/uptime - Check bot uptime"
    await event.edit(help_text, buttons=[
        [Button.inline("Ping", data="ping"), Button.inline("Uptime", data="uptime")],
        [Button.url("• Support •", url="t.me/alphabotzchat")]
    ])

# Inline Button Creation
@events.register(events.CallbackQuery(data="open"))
async def open_menu(event):
    """Handles the open menu button"""
    await event.edit(
        f"Welcome to {OWNER_NAME}'s UserBot Menu!",
        buttons=[[Button.inline("Ping", data="ping"), Button.inline("Uptime", data="uptime")],
                 [Button.inline("Help", data="help"), Button.url("• Repo •", url="https://github.com/alphauserbot")]]
    )

# Add the bot to a Telethon client
from telethon.sync import TelegramClient

# Use your own API_ID and API_HASH from https://my.telegram.org
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"

client = TelegramClient('alphabotz', api_id, api_hash).start(bot_token=bot_token)

# Add event handlers to the client
client.add_event_handler(start_handler)
client.add_event_handler(inline_alive)
client.add_event_handler(ping_handler)
client.add_event_handler(uptime_handler)
client.add_event_handler(help_handler)
client.add_event_handler(open_menu)

# Start the bot
client.run_until_disconnected()
