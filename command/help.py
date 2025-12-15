from telegram import Update
from telegram.ext import ContextTypes

from command.command import list_command


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.effective_message.reply_photo(
        'https://i.ibb.co/23BXRS7h/d516b8a07ebb.jpg',
        help_text(),
        parse_mode='HTML'
    )


def help_text():
    return f"Commands: \n{list_command()}"
