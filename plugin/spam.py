# plugins/spam.py

from telethon import events
import asyncio

# Dictionary to track active spam sessions
spam_sessions = {}

@events.register(events.NewMessage(pattern=r'\.spam (\d+) (.+)'))
async def spam(event):
    """Starts sending a specified number of spam messages.

    Parameters:
    count (int): The number of messages to send.
    message (str): The message content to spam.
    """
    try:
        # Delete the command message
        await event.delete()

        count = int(event.pattern_match.group(1))  # Extract the number of messages
        message = event.pattern_match.group(2)  # Extract the message to spam

        if count <= 0:
            await event.reply("❌ Please enter a positive number of messages.")
            return

        if event.sender_id in spam_sessions:
            await event.reply("❌ You already have an active spam session. Use .stop to stop it first.")
            return

        spam_sessions[event.sender_id] = (count, message)  # Track the count and message
        await event.reply(f"🔄 Starting to spam: '{message}' for {count} times! 🚀")

        for i in range(count):
            if event.sender_id not in spam_sessions:
                await event.reply("🛑 The spam session has been stopped. Take a breather! 🌬️")
                break  # Stop if the user has stopped the session
            await event.reply(f"📬 {message}")  # Send the spam message
            await asyncio.sleep(1)  # Adjust the delay as needed

            # Optionally provide progress feedback
            if (i + 1) % 10 == 0:
                await event.reply(f"📢 Sent {i + 1} messages so far... Keep going! 💪")

        if event.sender_id in spam_sessions:
            spam_sessions.pop(event.sender_id)  # Clean up after finishing
            await event.reply("✅ Finished sending all spam messages. Hope you enjoyed! 🎉")
    except ValueError:
        await event.reply("❌ Invalid input. Please enter a valid number followed by the message.")

@events.register(events.NewMessage(pattern=r'\.stop'))
async def stop(event):
    """Stops the active spam session."""
    # Delete the command message
    await event.delete()

    if event.sender_id in spam_sessions:
        spam_sessions.pop(event.sender_id)  # Remove the user from active sessions
        await event.reply("🛑 Stopped the spam session. You have the power! ✊")
    else:
        await event.reply("❌ You don't have an active spam session. Relax and enjoy! 🌈")
