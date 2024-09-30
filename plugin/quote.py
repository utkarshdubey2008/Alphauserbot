import aiohttp
from pyrogram import Client, filters

app = Client("my_bot")  # Replace "my_bot" with your bot's name or session string

@app.on_message(filters.command("quote", prefixes="."))
async def quote(client, message):
    """Fetches and sends a random quote from a quote API."""
    url = "https://api.quotable.io/random"  # A public API for random quotes

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    quote_data = await response.json()
                    quote = quote_data['content']
                    author = quote_data['author']
                    await message.reply(f"✨ \"{quote}\" \n\n— {author}")
                else:
                    await message.reply("❌ Could not fetch a quote.")
        except Exception as e:
            await message.reply(f"❌ Error fetching quote: {str(e)}")

if __name__ == "__main__":
    app.run()  # Start the bot
