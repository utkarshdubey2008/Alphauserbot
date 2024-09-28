from telethon import events
import requests
from config import GIPHY_API_KEY

@events.register(events.NewMessage(pattern=r'\.gif (.+)'))
async def gif(event):
    search_term = event.pattern_match.group(1)
    url = f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={search_term}&limit=1"
    
    response = requests.get(url)
    data = response.json()
    
    if data['data']:
        gif_url = data['data'][0]['url']
        await event.reply(gif_url)
    else:
        await event.reply("No GIFs found.")
