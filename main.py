import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


def build_caption(vid_id, title, uploader_username, extension, resolution, batch_name, tag_line):
    return f"""➖➖➖✦{vid_id}✦➖➖➖

📝 Title: {title}
╰┈➤ Extention : @{uploader_username} 🖤.{extension}
╰┈➤ Resolution : [{resolution}]

📦 Batch Name: {batch_name}

📤 Extracted By :  
╭───────⋆⋅✦⋅⋆───────╮  
@{uploader_username}  
╰───────⋆⋅✦⋅⋆───────╯

⫷━❖{tag_line}❖━⫸"""


@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    await m.reply_text(f"<b>💙 Hello! {m.from_user.mention} \n\n Send me a TXT file with PW links, and I will download and send the lectures here.\n\n ➠ 𝐔𝐬𝐞 /sameerji 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐫𝐨𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥e..\n\n ➠ 𝐔𝐬𝐞 /stop 𝐓𝐨 𝐬𝐭𝐨𝐩 𝐀𝐧𝐲 𝐎𝐧𝐠𝐨𝐢𝐧𝐠 𝐓𝐚𝐬𝐤 \n\n ➠ 𝐌𝐚𝐝𝐞 𝐁𝐲:- @DOCTOR_ASP </b>")

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**​🇸​​🇹​​🇴​​🇵​​🇵​​🇪​​🇩​**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["sameerji"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('🗣𝗦𝗘𝗡𝗗 𝗠𝗘 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 ⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("**Invalid file input.**")
        os.remove(x)
        return

    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n**𝕊ᴇɴᴅ 𝔽ʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)

    await editable.edit("*📸 𝗘𝗻𝘁𝗲𝗿 𝗥𝗲𝘀𝗼𝗹𝘂𝘁𝗶𝗼𝗻 📸**\n➸ `144`\n➸ `240`\n➸ `360`\n➸ `480`\n➸ `720`\n➸ `1080`")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    if raw_text2 == "144": res = "256x144"
    elif raw_text2 == "240": res = "426x240"
    elif raw_text2 == "360": res = "640x360"
    elif raw_text2 == "480": res = "854x480"
    elif raw_text2 == "720": res = "1280x720"
    elif raw_text2 == "1080": res = "1920x1080"
    else: res = "UN"

    await editable.edit("𝐄𝐗𝐓𝐑𝐀𝐂𝐓𝐄𝐃 𝐁𝐘➻ \n\n𝗘𝗴 » `🧡𝗦𝗔𝗠𝗘𝗘𝗥 𝗝𝗜🧡`")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)

    await editable.edit("👤 Enter Your Telegram @username")
    inputU: Message = await bot.listen(editable.chat.id)
    uploader = inputU.text.replace("@", "").strip()
    await inputU.delete(True)

    await editable.edit("❤️ Send your tag line (e.g. ANKIT❤️)")
    inputTag: Message = await bot.listen(editable.chat.id)
    tag_line = inputTag.text.strip()
    await inputTag.delete(True)

    await editable.edit("Now send the Thumb URL or type 'no'")
    input6 = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = raw_text6
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    for i in range(count - 1, len(links)):
        name1 = links[i][0].strip().replace(" ", "_")[:60]
        filename = f"{str(count).zfill(3)}) {name1}"
        extension = "mkv"
        caption = build_caption(str(count).zfill(3), name1, uploader, extension, res, raw_text0, tag_line)
        dummy_path = f"/path/to/{filename}.{extension}"

        await bot.send_document(chat_id=m.chat.id, document=dummy_path, caption=caption)
        count += 1


bot.run()

