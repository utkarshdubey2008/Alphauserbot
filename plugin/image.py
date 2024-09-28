from telethon import events
import requests
from config import UNSPLASH_ACCESS_KEY

@events.register(events.NewMessage(pattern=r'\.image (.+)'))
async def image(event):
    search_term = event.pattern_match.group(1)
    url = f"https://api.unsplash.com/search/photos?query={search_term}&client_id={UNSPLASH_ACCESS_KEY}"
    
    response = requests.get(url)
    data = response.json()

    if data['results']:
        img_url = data['results'][0]['urls']['regular']
        await event.reply(img_url)
    else:
        await event.reply("No images found.")
