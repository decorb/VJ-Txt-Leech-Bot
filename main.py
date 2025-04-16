import os
import time
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InputFile
from pwn import *

bot = Client(
    "Sameer-Ji-Leech-Bot",
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    bot_token=os.environ.get("BOT_TOKEN")
)

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002359983884"))

@bot.on_message(filters.command("sameerji") & filters.private)
async def sameerji_handler(bot: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply_text("📎 Reply to a .txt file containing links or IDs.")
        return

    file_path = await message.reply_to_message.download()
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines or len(lines) < 5:
        await message.reply_text("⚠️ The file must have at least 5 lines: batch, auth, quality, credit, then links.")
        return

    raw_text0 = lines[0]  # Batch
    raw_text1 = lines[1]  # Auth token
    raw_text2 = lines[2]  # Output folder or quality
    raw_text3 = lines[3]  # Extracted by
    links = lines[4:]

    await message.reply_text(f"✅ Download started for {len(links)} items. Sit tight...")

    count = 1
    for url in links:
        try:
            name = None
            if "pdf" in url.lower() or url.endswith(".pdf"):
                show_msg = f"**⥥ ​🇩​​🇴​​🇼​​🇳​​🇱​​🇴​​🇦​​🇩​​🇮​​🇳​​🇬​⬇️⬇️... »**\n\n**📝Name »** `{url}`\n❄**Quality » PDF**\n\n**🔗URL »** `{url}`\n\n**𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ➺ 𝗗𝗢𝗖𝗧𝗢𝗥 𝗦𝗔𝗛𝗔𝗕**"
                prog = await message.reply_text(show_msg)

                os.system(f"pwg pdf --auth \"{raw_text1}\" --output \"{raw_text2}\" {url}")
                pdf_files = [f for f in os.listdir(raw_text2) if f.endswith(".pdf")]
                if not pdf_files:
                    await prog.edit(f"❌ PDF not found for: {url}")
                    continue
                pdf_path = os.path.join(raw_text2, pdf_files[-1])
                name = os.path.splitext(os.path.basename(pdf_path))[0]

                caption = f'''**📁 𝙋𝙙𝙛_𝙄𝘿 ➠** `{str(count).zfill(3)}`\n
**📄 𝙋𝙙𝙛 𝙉𝙖𝙢𝙚 ➠** `{name}`\n
**🎯 𝘽𝙖𝙩𝙘𝙝 ➠** `{raw_text0}`\n
**📥 𝙀𝙭𝙩𝙧𝙖𝙘𝙩𝙚𝙙 𝘽𝙮 ➠** {raw_text3}\n
**💙𝙎𝘼𝙈𝙀𝙀𝙍 𝙅𝙄 𝘽𝙊𝙏💙**'''
                await bot.send_document(
                    chat_id=message.chat.id,
                    document=InputFile(pdf_path),
                    caption=caption
                )
                await prog.delete()
                os.remove(pdf_path)

            else:
                show_msg = f"**⥥ ​🇩​​🇴​​🇼​​🇳​​🇱​​🇴​​🇦​​🇩​​🇮​​🇳​​🇬​⬇️⬇️... »**\n\n**📝Name »** `{url}`\n❄**Quality » {raw_text2}``\n\n**🔗URL »** `{url}`\n\n**𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ➺ 𝗗𝗢𝗖𝗧𝗢𝗥 𝗦𝗔𝗛𝗔𝗕**"
                prog = await message.reply_text(show_msg)

                os.system(f"pwg video --auth \"{raw_text1}\" --output \"{raw_text2}\" --quality 480 {url}")
                mp4_files = [f for f in os.listdir(raw_text2) if f.endswith(".mp4")]
                if not mp4_files:
                    await prog.edit(f"❌ Video not found for: {url}")
                    continue
                video_path = os.path.join(raw_text2, mp4_files[-1])
                name = os.path.splitext(os.path.basename(video_path))[0]

                caption = f'''**📽️ 𝙑𝙞𝙙_𝙄𝘿 ➠** `{str(count).zfill(3)}`\n
**🌸 𝙇𝙚𝙘 𝙉𝙖𝙢𝙚 ➠** `{name}`\n
**🎯 𝘽𝙖𝙩𝙘𝙝 ➠** `{raw_text0}`\n
**📥 𝙀𝙭𝙩𝙧𝙖𝙘𝙩𝙚𝙙 𝘽𝙮 ➠** {raw_text3}\n
**💙𝙎𝘼𝙈𝙀𝙀𝙍 𝙅𝙄 𝘽𝙊𝙏💙**'''
                await bot.send_video(
                    chat_id=message.chat.id,
                    video=InputFile(video_path),
                    caption=caption,
                    supports_streaming=True
                )
                await prog.delete()
                os.remove(video_path)

            count += 1
            time.sleep(1)

        except Exception as e:
            await message.reply_text(
                f"**⚠️ Download Interrupted**\n`{str(e)}`\n**📝 Name** » `{name or url}`\n**🔗 Link** » `{url}`"
            )
            continue

    await message.reply_text("✅ All Done! Uploads completed successfully.")

if __name__ == "__main__":
    bot.run()



