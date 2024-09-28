from telethon import events
import requests
from config import OMDB_API_KEY

@events.register(events.NewMessage(pattern=r'\.movie (.+)'))
async def movie(event):
    title = event.pattern_match.group(1)
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    if data["Response"] == "True":
        await event.reply(f"{data['Title']} ({data['Year']}): {data['Plot']}")
    else:
        await event.reply("Movie not found.")
