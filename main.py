from utils.downloader import download_file
from utils.uploader import upload_to_telegram
from config import BOT_TOKEN, CHANNEL_ID
from pyrogram import Client, filters
import os

app = Client("leech-bot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("leech") & filters.private)
async def leech_handler(client, message):
    if len(message.command) < 2:
        await message.reply("Send a valid link to leech.")
        return

    url = message.command[1]
    await message.reply("📥 Downloading started...")

    file_path = download_file(url)
    if not file_path:
        await message.reply("❌ Failed to download.")
        return

    await message.reply("📤 Uploading to Telegram...")
    await upload_to_telegram(client, file_path, CHANNEL_ID)

    os.remove(file_path)

    await message.reply("✅ Done!")

app.run()
