from telegram import Update
from telegram.ext import ContextTypes
from dbmanagers.user import add_ban,remove_ban,get_bans
from Logger import send_info

async def ban_(update:Update,context:ContextTypes.DEFAULT_TYPE,args):
    
    reply = update.effective_message.reply_to_message
    
    if not reply:
        await update.effective_message.reply_text("Please Reply To An User.")
        return
    
    user_id = update.effective_user.id
    
    target = reply.from_user
    
    target_id = target.id
    
    chat = update.effective_chat
    
    await chat.ban_member(target_id)
    add_ban(target_id)
    tt=f"User ```{target_id}``` Banned!"
    await update.effective_message.reply_text(tt)
    await send_info(update,context,user_id,tt+f"\nFrom Group {chat.id}")

async def unban_(update:Update,context:ContextTypes.DEFAULT_TYPE,args):
    
    reply = update.effective_message.reply_to_message
    
    if not reply:
        await update.effective_message.reply_text("Please Reply To An User.")
        return
    
    user_id = update.effective_user.id
    
    target = reply.from_user
    
    target_id = target.id
    
    chat = update.effective_chat
    
    await chat.unban_member(target_id)
    remove_ban(target_id)
    tt=f"User ```{target_id}``` UnBanned!"
    await update.effective_message.reply_text(tt)
    await send_info(update,context,user_id,tt+f"\nFrom Group {chat.id}")
           
async def ban_list(update: Update, context: ContextTypes.DEFAULT_TYPE):

    bans = get_bans()

    if not bans:
        await update.effective_message.reply_text("No muted users.")
        return

    user_id = update.effective_user.id
    text = f"List Mutes From Bot:\nCount: {len(bans)}\n\n"

    limit = min(10, len(bans))

    for i, ban in enumerate(bans, start=1):
        if i > limit:
            break
        text += f"{i} - User: `{ban}`\n"

    if len(bans) > 10:
        text += "..."

    await update.effective_message.reply_text(text)
    await send_info(update, context, user_id, text)
    