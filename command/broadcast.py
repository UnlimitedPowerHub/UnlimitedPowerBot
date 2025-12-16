from telegram import Update
from telegram.ext import ContextTypes

from db.user import get_users, is_owner


async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userid = update.effective_user.id

    if not is_owner(userid):
        await update.effective_message.reply_text("Don't Try Again!\nOnly Owner Can Use This Command.")
        return

    users = get_users()

    reply = update.effective_message.reply_to_message
    if not reply:
        await update.effective_message.reply_text("Reply To A Message")
        return

    for user in users:
        try:
            await context.bot.forwardMessage(
                user,
                userid,
                reply.id
            )
        except:
            pass
