from telegram import Update
from telegram.ext import ContextTypes
from config import LOG_GROUP_ID

async def send(update:Update,context:ContextTypes.DEFAULT_TYPE,text):
    
    await context.bot.send_message(LOG_GROUP_ID,text)

async def send_notice(update,context,user_id,text):
    
    await send(
        update,context,text=f"Notice - From {user_id},\n\n{text}"
    )
    
async def send_warn(update,context,user_id,text):
    
    await send(
        update,context,text=f"Warn - From {user_id},\n\n{text}"
    )
    
async def send_error(update,context,user_id,text):
    
    await send(
        update,context,text=f"Error - From {user_id},\n\n{text}"
    )
    
async def send_info(update,context,user_id,text):
    
    await send(
        update,context,text=f"Info - From {user_id},\n\n{text}"
    )
    
