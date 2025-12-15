import time

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from db.user import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    userid = user.id

    if not exist_user(userid):
        add_user(userid, {})

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
        f"ᴜᴘᴛɪᴍᴇ: None\n"
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
