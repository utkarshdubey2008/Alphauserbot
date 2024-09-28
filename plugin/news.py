from telethon import events
import requests

@events.register(events.NewMessage(pattern=r'\.news'))
async def news(event):
    response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_NEWSAPI_KEY")
    articles = response.json()["articles"]
    news_list = [f"{article['title']} - {article['url']}" for article in articles[:5]]
    await event.reply("\n".join(news_list))
