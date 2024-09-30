import os
from pyrogram import Client

# Retrieve credentials from environment variables
API_ID = int(os.getenv('API_ID'))  # Replace with your actual API ID
API_HASH = os.getenv('API_HASH')    # Replace with your actual API Hash

# Create the Pyrogram Client instance using in-memory session
app = Client(
    ":memory:",  # Use in-memory session
    api_id=API_ID,
    api_hash=API_HASH
)
