# vars.py — Configuration Variables

import os

API_ID = int(os.getenv("API_ID", 17950436))  # Replace with your actual API ID
API_HASH = os.getenv("API_HASH", "9d8ae4d35b1106df910b94dcaf73d346")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7955197951:AAHBPLN4CrbX4t502WhMiq1WttR0nXVk5n0")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", -1002359983884))  # Your channel ID

# Optional: Admins list
SUDO_USERS = [123456789, 987654321]  # Telegram user IDs

# Download directory (temporary)
DOWNLOAD_DIR = "downloads
