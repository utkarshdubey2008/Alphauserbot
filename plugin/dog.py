# plugins/dog.py

import requests
from telethon import events

@events.register(events.NewMessage(pattern=r'\.dog'))
async def dog(event):
    """Fetches and sends a random dog image."""
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        dog_data = response.json()  # Get the dog data

        if dog_data['status'] == 'success':
            await event.reply(dog_data['message'])  # Send the dog image URL
        else:
            await event.reply("❌ Could not fetch a dog image.")
    except Exception as e:
        await event.reply(f"❌ Error fetching dog image: {str(e)}")  # Handle any exceptions
