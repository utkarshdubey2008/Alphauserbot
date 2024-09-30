import aiohttp
from pyrogram import Client, filters

app = Client("my_bot")  # Replace "my_bot" with your bot's name or session string

@app.on_message(filters.command("joke", prefixes="."))
async def joke(client, message):
    """Fetches and sends a random joke from a joke API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    joke_data = await response.json()
                    setup = joke_data['setup']
                    punchline = joke_data['punchline']
                    await message.reply(f"😂 {setup} - {punchline}")
                else:
                    await message.reply("❌ Could not fetch a joke.")
        except Exception as e:
            await message.reply(f"❌ Error fetching joke: {str(e)}")

if __name__ == "__main__":
    app.run()  # Start the bot
