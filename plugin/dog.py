import aiohttp
from pyrogram import Client, filters

app = Client("my_bot")  # Replace "my_bot" with your actual bot name or session string

@app.on_message(filters.command("dog", prefixes="."))
async def dog(client, message):
    """Fetches and sends a random dog image."""
    url = "https://dog.ceo/api/breeds/image/random"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                dog_data = await response.json()

            if dog_data['status'] == 'success':
                await message.reply(dog_data['message'])  # Send the dog image URL
            else:
                await message.reply("❌ Could not fetch a dog image.")
        except Exception as e:
            await message.reply(f"❌ Error fetching dog image: {str(e)}")  # Handle any exceptions

if __name__ == "__main__":
    app.run()  # Start the bot
