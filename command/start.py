import time
import datetime as dt

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from db.user import *
from bot_config import bot_run_time


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    userid = user.id

    if not exist_user(userid):
        add_user(userid, {})

    current_time = dt.datetime.now(dt.timezone.utc)

    uptime = await format_uptime(bot_run_time, current_time)

    start_time = time.time()

    msg = await update.effective_message.reply_text('starting...')

    end_time = time.time()

    await msg.delete()

    ping = (end_time - start_time) * 10

    await update.effective_message.reply_photo(
        'https://i.ibb.co/23BXRS7h/d516b8a07ebb.jpg',
        f"ʜᴇʏ ᴜsᴇʀ {user.mention_html()}, WᴇʟCᴏᴍᴇ ᴛᴏ UɴʟɪᴍɪᴛᴇᴅPᴏᴡᴇʀBᴏᴛ :)\n"
        "——————————‹ ⁌※⁍ ›——————————\n"
        "Tʜɪs ʙᴏᴛ ᴍᴀᴅᴇ ғᴏʀ UɴʟɪᴍɪᴛᴇᴅPᴏᴡᴇʀ ᴄᴏᴍᴍᴜɴɪᴛʏ.\n"
        "ᴏᴡɴᴇʀ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇʀ ɪs ᴀᴍɪʀʀᴇᴢᴀ(@ManamMadara).\n"
        "——————————‹ ⁌※⁍ ›——————————\n"
        f"ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"ᴘɪɴɢ: {ping: .2f}ᴍs",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Aᴅᴅ Mᴇ ➕", url=f"https://t.me/{context.bot.username}?startgroup=true")],
            [
                InlineKeyboardButton("◜Mᴀɪɴ Cʜᴀɴɴᴇʟ◞", url='https://t.me/UnlimitedPowerHub'),
                InlineKeyboardButton("◜Mᴀɪɴ Gʀᴏᴜᴘ◞", url='https://t.me/UnlimitedPowerGroup')
            ],
            [InlineKeyboardButton("Help", callback_data='help_btn')]
        ]),
        parse_mode='HTML'
    )


async def format_uptime(start, end):
    delta_uptime = end - start

    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    if days > 0:
        return f"{days}d {hours}h {minutes}m {seconds}s"
    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"
