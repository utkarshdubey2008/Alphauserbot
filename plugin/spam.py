import asyncio
import aiohttp
from pyrogram import Client, filters

# Dictionary to track active spam sessions
spam_sessions = {}

app = Client("my_bot")  # Replace "my_bot" with your bot's name or session string

@app.on_message(filters.command("spam", prefixes=".") & filters.private)
async def spam(client, message):
    """Starts sending a specified number of spam messages.

    Parameters:
    count (int): The number of messages to send.
    message (str): The message content to spam.
    """
    try:
        # Delete the command message
        await message.delete()

        # Parse the command arguments
        args = message.command[1:]
        if len(args) < 2:
            await message.reply("❌ Please provide the number of messages and the message to spam.")
            return

        count = int(args[0])  # Extract the number of messages
        spam_message = " ".join(args[1:])  # Extract the message to spam

        if count <= 0:
            await message.reply("❌ Please enter a positive number of messages.")
            return

        if message.from_user.id in spam_sessions:
            await message.reply("❌ You already have an active spam session. Use `.stop` to stop it first.")
            return

        spam_sessions[message.from_user.id] = (count, spam_message)  # Track the count and message
        await message.reply(f"🔄 Starting to spam: '{spam_message}' for {count} times! 🚀")

        for i in range(count):
            if message.from_user.id not in spam_sessions:
                await message.reply("🛑 The spam session has been stopped. Take a breather! 🌬️")
                break  # Stop if the user has stopped the session
            await message.reply(f"📬 {spam_message}")  # Send the spam message
            await asyncio.sleep(1)  # Adjust the delay as needed

            # Optionally provide progress feedback every 10 messages
            if (i + 1) % 10 == 0:
                await message.reply(f"📢 Sent {i + 1} messages so far... Keep going! 💪")

        if message.from_user.id in spam_sessions:
            spam_sessions.pop(message.from_user.id)  # Clean up after finishing
            await message.reply("✅ Finished sending all spam messages. Hope you enjoyed! 🎉")
    except ValueError:
        await message.reply("❌ Invalid input. Please enter a valid number followed by the message.")
    except Exception as e:
        await message.reply(f"❌ An unexpected error occurred: {str(e)}")  # Handle any other exceptions

@app.on_message(filters.command("stop", prefixes=".") & filters.private)
async def stop(client, message):
    """Stops the active spam session."""
    # Delete the command message
    await message.delete()

    if message.from_user.id in spam_sessions:
        spam_sessions.pop(message.from_user.id)  # Remove the user from active sessions
        await message.reply("🛑 Stopped the spam session. You have the power! ✊")
    else:
        await message.reply("❌ You don't have an active spam session. Relax and enjoy!")

if __name__ == "__main__":
    app.run()  # Start the bot
