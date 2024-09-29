import random
from telethon import events

# A list of motivational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "You are never too old to set another goal or to dream a new dream.",
    # Add more quotes here if desired
]

@events.register(events.NewMessage(pattern=r'\.quote'))
async def quote(event):
    """Sends a random motivational quote."""
    try:
        quote_text = random.choice(quotes)  # Randomly select a quote
        await event.reply(f"💬 {quote_text}")  # Send the quote
    except Exception as e:
        await event.reply(f"❌ Error fetching quote: {str(e)}")  # Handle errors gracefully
