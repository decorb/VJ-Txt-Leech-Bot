# utils.py — Combined with progress and basic helpers

import os
import shutil
import time
import logging
from datetime import timedelta
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("utils")

DOWNLOAD_DIR = "downloads"

# Basic file utils
def clean_up(path: str):
    try:
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
    except Exception as e:
        logger.error(f"Cleanup error: {e}")

def get_file_extension(file_name: str):
    return os.path.splitext(file_name)[-1]

# Progress Bar Helpers
class Timer:
    def __init__(self, delay=5):
        self.last = time.time()
        self.delay = delay

    def ready(self):
        if time.time() - self.last >= self.delay:
            self.last = time.time()
            return True
        return False

def format_size(size):
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024:
            return f"{size:.2f}{unit}"
        size /= 1024
    return f"{size:.2f}PB"

def format_time(seconds):
    return str(timedelta(seconds=int(seconds)))

progress_timer = Timer()

async def progress_bar(current, total, reply, start_time):
    if not progress_timer.ready():
        return

    now = time.time()
    elapsed = now - start_time
    if elapsed == 0:
        return

    speed = current / elapsed
    eta = (total - current) / speed if speed > 0 else 0
    bar_length = 15
    done = int(bar_length * current / total)
    percent = (current / total) * 100
    bar = '█' * done + '▒' * (bar_length - done)

    text = (
        f"**┌────═━⇗ 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗𝗜𝗡𝗚 ⇖━═────┐**\n\n"
        f"**┣⪼ [{bar}]**\n\n"
        f"**┣⪼ 🚀 Speed:** {format_size(speed)}/s\n\n"
        f"**┣⪼ 📈 Progress:** {percent:.1f}%\n\n"
        f"**┣⪼ 📦 Loaded:** {format_size(current)} / {format_size(total)}\n\n"
        f"**┣⪼ ⏳ ETA:** {format_time(eta)}\n\n"
        f"**└────═━ ✨ SAMEER JI ✨ ━═────┘**"
    )

    try:
        await reply.edit(text)
    except FloodWait as e:
        time.sleep(e.value)
