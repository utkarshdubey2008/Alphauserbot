from telethon import events

@events.register(events.NewMessage(pattern=r'\.help'))
async def help_command(event):
    help_text = (
        "Available commands:\n"
        ".start - Welcome message\n"
        ".help - List of commands\n"
        ".echo <text> - Repeat your text\n"
        ".weather <city> - Get weather information\n"
        ".joke - Receive a random joke\n"
        ".quote - Get an inspirational quote\n"
        ".roll <number> - Roll a dice\n"
        ".gif <search term> - Search for GIFs\n"
        ".image <search term> - Search for images\n"
        ".poll <question> - Create a poll\n"
        ".fact - Share an interesting fact\n"
        ".music <title> - Search for music\n"
        ".movie <title> - Search for movie info\n"
        ".remindme <time> <message> - Set a reminder\n"
        ".meme <topic> - Send a random meme\n"
        ".ban <user> - Ban a user (admin only)\n"
        ".kick <user> - Kick a user (admin only)\n"
        ".mute <user> - Mute a user (admin only)\n"
        ".unmute <user> - Unmute a user (admin only)\n"
        ".tag <user> - Tag a user\n"
        ".save <link> - Save a link\n"
        ".report <issue> - Report an issue\n"
        ".settings - Manage bot settings"
    )
    await event.reply(help_text)
