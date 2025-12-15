from telegram import Update
from telegram.ext import ContextTypes
from Logger import send_info

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    
    user_id = update.effective_user.id
    await update.effective_message.reply_text("Start")
    await send_info(update,context,user_id,"Started The Bot")