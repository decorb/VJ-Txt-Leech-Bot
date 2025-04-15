import time
import random
from math import ceil
from pyrogram.types import Message

# Emoji groups to randomly decorate bottom line
EMOJI_SETS = [
    "🦋✨🌸💫🌼🌙",
    "🔥💎⚡🌪️🧿💥",
    "📀📼💽💾📂📁",
    "🌟👑🚀🎯🎉🧲",
    "🎵🎶🎧🎷🎺🎸",
    "💙💚💛🧡❤️💜",
    "🧠📚📝✏️📖📒",
    "🧃🍭🍬🍫🍩🍪"
]

def human_readable_size(size):
    power = 2**10
    n = 0
    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    while size > power and n < len(units) - 1:
        size /= power
        n += 1
    return f"{round(size, 2)}{units[n]}"


async def progress_bar(current, total, message: Message, start_time, tag="@DOCTOR_JB"):
    now = time.time()
    elapsed = now - start_time
    if elapsed == 0:
        elapsed = 1

    speed = current / elapsed
    percentage = current * 100 / total
    eta = (total - current) / speed if speed > 0 else 0

    # Get random emoji line
    emoji_line = random.choice(EMOJI_SETS)

    # Format status text
    progress_text = f"""
⟪ 💥 UPLOADER 💥 ⟫
├SPEED ⚡ = {human_readable_size(speed)}/s
├PROGRESS 🌀 = {round(percentage, 1)}%
├LOADED 📥 = {human_readable_size(current)}
├SIZE 🧲 = {human_readable_size(total)}
├ETA ⏳ = {time.strftime('%Mm %Ss', time.gmtime(eta))}
⟬ {tag} ⟭

{emoji_line}
"""
    try:
        await message.edit_text(f"```{progress_text}```")
    except Exception:
        pass

