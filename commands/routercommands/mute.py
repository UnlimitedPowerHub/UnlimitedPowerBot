from telegram import Update,ChatPermissions
from telegram.ext import ContextTypes
from Logger import send_notice,send_info
from dbmanagers.user import is_mute,mute,unmute,get_mutes
from func import is_owner_or_admin

async def mute_(update:Update,context:ContextTypes.DEFAULT_TYPE,args):
    user_id = update.effective_user.id
    
    if not is_owner_or_admin(user_id):
        return
    reply = update.effective_message.reply_to_message
    
    if not reply:
        await update.effective_message.reply_text(f"Please Reply To An User")
        await send_notice(update,context,user_id,"Tried To Use .mute Command")
        return
    
    target = reply.from_user
    
    target_id = target.id
    
    if is_mute(target_id):
        await update.effective_message.reply_text(f"User {target_id} Already Is Mute")
        await send_notice(update,context,user_id,f"Tried To Mute User {target_id} But User Is Already Is Mute")
        return
    
    await update.effective_chat.restrict_member(target_id,permissions=ChatPermissions(can_send_messages=False))
    mute(target_id)
    asndioha=f"User {target_id} Muted"
    await update.effective_message.reply_text(asndioha)
    await send_info(update,context,user_id,asndioha)

async def unmute_(update:Update,context:ContextTypes.DEFAULT_TYPE,args):
    user_id = update.effective_user.id
    
    if not is_owner_or_admin(user_id):
        return
    reply = update.effective_message.reply_to_message
    
    if not reply:
        await update.effective_message.reply_text(f"Please Reply To An User")
        await send_notice(update,context,user_id,"Tried To Use .unmute Command")
        return
    
    target = reply.from_user
    
    target_id = target.id
    
    if not is_mute(target_id):
        await update.effective_message.reply_text(f"User {target_id} Is Not Mute")
        await send_notice(update,context,user_id,f"Tried To UnMute User {target_id} But User Is Already Is Mute")
        return
    
    await update.effective_chat.restrict_member(target_id,permissions=ChatPermissions(can_send_messages=True))
    unmute(target_id)
    asndioha=f"User {target_id} UnMuted"
    await update.effective_message.reply_text(asndioha)
    await send_info(update,context,user_id,asndioha)
    
async def mute_list_bot(update: Update, context: ContextTypes.DEFAULT_TYPE,args):
    user_id = update.effective_user.id
    
    if not is_owner_or_admin(user_id):
        return
    bans = get_mutes()

    if not bans:
        await update.effective_message.reply_text("No muted users.")
        return

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
