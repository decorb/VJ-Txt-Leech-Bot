async def progress_bar(current, total, reply, start, your_batch_name="Not Set", your_file_name="Unknown File", total_links=0):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            percent = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            remaining = total - current
            eta = hrt(remaining / speed, precision=1) if speed > 0 else "-"
            
            speed_str = f"{hrb(speed)}/s"
            total_str = hrb(total)
            current_str = hrb(current)
            
            bar_length = 11
            done = int(current * bar_length / total)
            left = bar_length - done
            progress = "█" * done + "░" * left

            try:
                text = (
                    "<b>\n"
                    "╭──⌯════⏫ 𝗨𝗣𝗟𝗢𝗔𝗗𝗜𝗡𝗚... ⌯────╮\n"
                    f"├ 📚 𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘     » {your_batch_name}\n"
                    f"├ 📄 𝗙𝗶𝗹𝗲 𝗡𝗮𝗺𝗲      » {your_file_name}\n"
                    f"├ 🔗 𝗧𝗼𝘁𝗮𝗹 𝗟𝗶𝗻𝗸𝘀     » {total_links}\n"
                    f"├ 📊 Progress       » {progress} |﹝{percent}﹞\n"
                    f"├ ⚡ Speed          » {speed_str}\n"
                    f"├ 📥 Uploaded       » {current_str}\n"
                    f"├ 📦 Total Size     » {total_str}\n"
                    f"├ ⏳ ETA            » {eta}\n"
                    "├ 🤖 Bot by        » <a href='https://t.me/A_S_9162'>@A_S_9162</a>\n"
                    "╰──═✪ <a href='https://t.me/SAMEER_OFFICAL_092'>SAMEER OFFICAL</a> ✪══─╯\n"
                    "</b>"
                )
                await reply.edit(text, disable_web_page_preview=True)
            except FloodWait as e:
                time.sleep(e.x)
