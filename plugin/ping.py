from pyrogram import Client, filters

app = Client("my_bot")  # Replace "my_bot" with your bot's name or session string

@app.on_message(filters.command("ping", prefixes="."))
async def ping(client, message):
    """Checks the bot's responsiveness."""
    await message.reply("🏓 Pong! The bot is alive and responsive.")

if __name__ == "__main__":
    app.run()  # Start the bot
