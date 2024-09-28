@events.register(events.NewMessage(pattern=r'\.draid'))
async def stop_raid(event):
    await event.reply("Raid stopped!")
    # Logic to stop the raid if implemented
