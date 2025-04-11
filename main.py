# main.py with Styled Caption for PDF Uploads

import os
from pyrogram import Client, filters
from pyrogram.types import Message, InputMediaDocument
from pyrogram.enums import ChatAction

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = -1002359983884

bot = Client("styled_caption_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Store user input states
user_data = {}

@bot.on_message(filters.command("upload") & filters.private)
async def ask_vid_id(client, message):
    user_data[message.from_user.id] = {}
    await message.reply_text("🔢 Enter VID ID:")
    return

@bot.on_message(filters.private & filters.text)
async def handle_inputs(client, message: Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        return

    user_state = user_data[user_id]

    if "vid_id" not in user_state:
        user_state["vid_id"] = message.text
        await message.reply_text("📚 Enter Batch Name:")
        return

    if "batch" not in user_state:
        user_state["batch"] = message.text
        await message.reply_text("📥 Enter Downloaded by (tag or name):")
        return

    if "by" not in user_state:
        user_state["by"] = message.text
        await message.reply_text("🧾 Enter Quality (360p/720p etc):")
        return

    if "quality" not in user_state:
        user_state["quality"] = message.text
        await message.reply_text("📎 Now send the PDF or file to upload.")
        return

    if message.document:
        await message.reply_chat_action(ChatAction.UPLOAD_DOCUMENT)

        caption = f"➖➖➖➖➖➖➖\n"
        caption += f"◆➤ **{user_state['vid_id']}** ➤◆\n\n"
        caption += f"📜 **Title:** {message.document.file_name}\n"
        caption += f"🗂️ **Batch Name:** {user_state['batch']}\n"
        caption += f"📁 **Extention:** .pdf\n\n"
        caption += f"📥 **Extracted By:**\n\n✨───────➤\n@{user_state['by'].strip('@')}\n➤───────✨\n\n"
        caption += f"▣ **{user_state['by']}** ▣"

        await bot.send_document(
            chat_id=CHANNEL_ID,
            document=message.document.file_id,
            caption=caption
        )

        await message.reply_text("✅ Uploaded with styled caption!")
        user_data.pop(user_id)

bot.run()

    await bot.send_document(chat_id=CHANNEL_ID, document=file, caption=caption)
    await message.reply("✅ File uploaded to channel!")

bot.run()
