from telethon import events, Button
from telethon.tl.functions.messages import CreateDiscussion
from telethon.tl.functions.stickers import CreateStickerSetRequest
from telethon.tl.types import InputStickerSetItem, InputFile
import requests

@events.register(events.NewMessage(pattern=r'\.kang (.+)'))
async def kang(event):
    pack_name = event.pattern_match.group(1)
    user_id = event.sender_id

    # Creating a new sticker pack
    await event.reply(f"Creating sticker pack '{pack_name}'...")

    # You can specify stickers you want to add to the pack here
    sticker_ids = ["sticker_id1", "sticker_id2"]  # Replace with actual sticker file IDs or URLs
    
    # Use your own logic to fetch and prepare stickers
    stickers = []
    for sticker_id in sticker_ids:
        # Assuming you have the stickers' file_ids or URLs
        # You can fetch them from your own storage or an API
        stickers.append(InputStickerSetItem(sticker_id=sticker_id, emoji='🚀'))  # Use appropriate emojis

    try:
        await event.client(CreateStickerSetRequest(
            user_id=user_id,
            title=pack_name,
            short_name=pack_name.lower().replace(" ", "_"),
            stickers=stickers
        ))
        await event.reply(f"Sticker pack '{pack_name}' created successfully!")
    except Exception as e:
        await event.reply(f"Failed to create sticker pack: {str(e)}")
