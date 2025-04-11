# main.py — Universal Leech Bot (PW + Others)

import os
import time
import asyncio
import logging
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = -1002359983884  # Your Telegram channel ID

bot = Client("allinone_leech_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

user_data = {}
logging.basicConfig(level=logging.INFO)

SUPPORTED_EXTS = [".pdf", ".mp4", ".mkv", ".zip", ".jpg", ".jpeg", ".png"]

@bot.on_message(filters.command("leech") & filters.private)
async def start_leech(client, message: Message):
    user_data[message.chat.id] = {}
    await message.reply_text("🔢 Enter VID ID:")

@bot.on_message(filters.private & filters.text)
async def get_meta_inputs(client, message: Message):
    user_id = message.chat.id
    if user_id not in user_data:
        return

    u = user_data[user_id]

    if "vid_id" not in u:
        u["vid_id"] = message.text.strip()
        await message.reply_text("📚 Enter Batch Name:")
        return

    if "batch" not in u:
        u["batch"] = message.text.strip()
        await message.reply_text("📝 Enter Downloaded By (your tag):")
        return

    if "by" not in u:
        u["by"] = message.text.strip()
        await message.reply_text("📺 Enter Quality (e.g., 360p, 720p):")
        return

    if "quality" not in u:
        u["quality"] = message.text.strip()
        await message.reply_text("📎 Now send the Lecture/PDF/ZIP/Image file or direct link.")
        return

    if message.document or message.video:
        await handle_file_upload(client, message)
        return

    if "http" in message.text:
        url = message.text.strip()
        name = f"PW_{int(time.time())}"
        ext = ".mp4" if ".mpd" in url or "m3u8" in url else ".pdf"

        file_name = name + ext
        await message.reply_chat_action(ChatAction.UPLOAD_DOCUMENT)

        try:
            with open(file_name, "wb") as f:
                f.write(requests.get(url).content)
        except Exception as e:
            await message.reply_text(f"❌ Failed to download file: {e}")
            return

        await send_to_channel(client, message, file_name)
        os.remove(file_name)

async def handle_file_upload(client, message: Message):
    doc = message.document or message.video
    file_name = doc.file_name or "file.pdf"
    file_path = await doc.download()
    await send_to_channel(client, message, file_path)
    os.remove(file_path)

async def send_to_channel(client, message, file_path):
    u = user_data[message.chat.id]
    file_name = os.path.basename(file_path)

    caption = f"**➖➖➖➖➖➖➖**\n"
    caption += f"**◆➤ VID_ID:** {u['vid_id']}\n"
    caption += f"**📜 Title:** {file_name}\n"
    caption += f"**🗂️ Batch:** {u['batch']}\n"
    caption += f"**📁 Ext:** {os.path.splitext(file_name)[1]}\n"
    caption += f"**📺 Quality:** {u['quality']}\n\n"
    caption += f"📥 **Downloaded By:** @{u['by'].strip('@')}\n"
    caption += f"✯ ━━━━━━ ✿ SAMEER BHYYA ✿ ━━━━━━ ✯"

    await client.send_document(
        chat_id=CHANNEL_ID,
        document=file_path,
        caption=caption
    )
    await message.reply_text("✅ Uploaded successfully!")
    user_data.pop(message.chat.id)

bot.run()
