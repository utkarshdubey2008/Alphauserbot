import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, SESSION_STRING  # Import configuration

# Dictionary to track active spam sessions
spam_sessions = {}

# Create the Pyrogram Client instance
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

@app.on_message(filters.command("spam", prefixes=".") & filters.private)
async def spam(client, message):
    """Starts sending a specified number of spam messages."""
    try:
        await message.delete()
        args = message.command[1:]

        if len(args) < 2:
            await message.reply("❌ Please provide the number of messages and the message to spam.")
            return

        count = int(args[0])
        spam_message = " ".join(args[1:])

        if count <= 0:
            await message.reply("❌ Please enter a positive number of messages.")
            return

        if message.from_user.id in spam_sessions:
            await message.reply("❌ You already have an active spam session. Use `.stop` to stop it first.")
            return

        spam_sessions[message.from_user.id] = (count, spam_message)
        await message.reply(f"🔄 Starting to spam: '{spam_message}' for {count} times! 🚀")

        for i in range(count):
            if message.from_user.id not in spam_sessions:
                await message.reply("🛑 The spam session has been stopped. Take a breather! 🌬️")
                break

            await message.reply(f"📬 {spam_message}")
            await asyncio.sleep(1)

            if (i + 1) % 10 == 0:
                await message.reply(f"📢 Sent {i + 1} messages so far... Keep going! 💪")

        if message.from_user.id in spam_sessions:
            spam_sessions.pop(message.from_user.id)
            await message.reply("✅ Finished sending all spam messages. Hope you enjoyed! 🎉")
    except ValueError:
        await message.reply("❌ Invalid input. Please enter a valid number followed by the message.")
    except Exception as e:
        await message.reply(f"❌ An unexpected error occurred: {str(e)}")

@app.on_message(filters.command("stop", prefixes=".") & filters.private)
async def stop(client, message):
    """Stops the active spam session."""
    await message.delete()

    if message.from_user.id in spam_sessions:
        spam_sessions.pop(message.from_user.id)
        await message.reply("🛑 Stopped the spam session. You have the power! ✊")
    else:
        await message.reply("❌ You don't have an active spam session. Relax and enjoy!")

if __name__ == "__main__":
    app.run()  # Start the bot
