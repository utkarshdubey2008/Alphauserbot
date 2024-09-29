import aiohttp
from telethon import events

@events.register(events.NewMessage(pattern=r'\.joke'))
async def joke(event):
    """Fetches and sends a random joke from a joke API."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://official-joke-api.appspot.com/random_joke") as response:
                joke_data = await response.json()
                setup = joke_data['setup']
                punchline = joke_data['punchline']
                await event.reply(f"😂 {setup} - {punchline}")
    except Exception as e:
        await event.reply(f"❌ Error fetching joke: {str(e)}")
