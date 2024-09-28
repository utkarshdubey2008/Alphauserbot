from telethon import events
from telethon.tl.functions.messages import CreateDiscussion
from telethon.tl.functions.stickers import CreateStickerSetRequest
from telethon.tl.types import InputStickerSetItem
import requests

@client.on(events.NewMessage(pattern=r'\.kang (.+)'))
async def kang(event):
    pack_name = event.pattern_match.group(1)
    user_id = event.sender_id

    # Creating a new sticker pack
    await event.reply(f"Creating sticker pack '{pack_name}'...")

    # Specify your sticker file IDs or URLs (ensure you have rights to them)
    sticker_ids = ["sticker_id1", "sticker_id2"]  # Replace with actual IDs
    
    # Prepare the stickers for the pack
    stickers = []
    for sticker_id in sticker_ids:
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
