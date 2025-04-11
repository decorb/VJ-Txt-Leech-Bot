# main_updated.py — Customized for @A_S_9162 Channel

import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = -1002359983884  # Your channel ID

bot = Client(
    "pw_leech_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("upload") & filters.private)
async def upload_file(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply("📎 Reply to a document to upload.")
        return

    file = await message.reply_to_message.download()
    file_name = message.reply_to_message.document.file_name or "PW_Class.mp4"

    caption = (
        "✦✦ 𝗖𝗟𝗔𝗦𝗦 𝗜𝗡𝗙𝗢 ✦✦\n\n"
        f"🎞️ VID_ID: 003\n"
        f"🎬 LEC NAME: {file_name}\n\n"
        "📚 BATCH NAME: Yakeen NEET 2025\n\n"
        "📥 DOWNLOAD BY PW Leech Bot\n\n"
        "✯ ━━━━━━ ✿ SAMEER BHYYA ✿ ━━━━━━ ✯"
    )

    await bot.send_document(chat_id=CHANNEL_ID, document=file, caption=caption)
    await message.reply("✅ File uploaded to channel!")

bot.run()



bot.run()
