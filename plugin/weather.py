from telethon import events
import requests
from config import OPENWEATHER_API_KEY

@events.register(events.NewMessage(pattern=r'\.weather (.+)'))
async def weather(event):
    city = event.pattern_match.group(1)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        await event.reply(f"Weather in {city}:\nTemperature: {temp}°C\nDescription: {description}")
    else:
        await event.reply("City not found.")
