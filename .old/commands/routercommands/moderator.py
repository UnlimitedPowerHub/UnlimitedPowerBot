from dbmanagers.staff import add_moderator, remove_moderator, moderator
from Logger import send_notice,send_error,send_info
from func import is_owner

async def add_moderator_(update, context, args):
    try:
        reply = update.effective_message.reply_to_message
        user_id = update.effective_user.id
        
        fff="Tried To Use staff.add.moderator Command"
        
        if not is_owner(user_id):
            await send_notice(update,context,user_id,fff)
            return
        
        if not reply:
            await update.effective_message.reply_text("Please Reply To An User")
            await send_notice(update,context,user_id,fff)
            return
        target_id = reply.from_user.id
        
        if moderator(target_id) is not None:
            await update.effective_message.reply_text("User Already Is Moderator")
            await send_notice(update,context,update.effective_user.id,f"Tried To Add Moderator User {target_id}")
            return
        add_moderator(target_id)
        textt=f"Moderator Added - ID: `{target_id}`"
        await update.effective_message.reply_text(textt, parse_mode="Markdown")
        await send_info(update,context,user_id,textt)
    except ValueError:
        tttt="Invalid ID Format"
        await update.effective_message.reply_text(tttt)
        await send_error(update,context,user_id,tttt+"\n Use staff.add.moderator Command")
    except Exception as e:
        await send_error(update,context,user_id,f"Error in add_moderator_: {e}")

async def remove_moderator_(update, context, args):
    try:
        reply = update.effective_message.reply_to_message
        user_id = update.effective_user.id
        
        fff="Tried To Use staff.remove.moderator Command"
        
        if not is_owner(user_id):
            await send_notice(update,context,user_id,fff)
            return
        
        if not reply:
            await update.effective_message.reply_text("Please Reply To An User")
            await send_notice(update,context,user_id,fff)
            return
        target_id = reply.from_user.id
        
        if moderator(target_id) is None:
            await update.effective_message.reply_text("User Is Not Moderator")
            await send_notice(update,context,update.effective_user.id,f"Tried To Remove Moderator User {target_id}")
            return
        remove_moderator(target_id)
        textt=f"Moderator Removed - ID: `{target_id}`"
        await update.effective_message.reply_text(textt, parse_mode="Markdown")
        await send_info(update,context,user_id,textt)
    except ValueError:
        tttt="Invalid ID Format"
        await update.effective_message.reply_text(tttt)
        await send_error(update,context,user_id,tttt+"\n Use staff.remove.moderator Command")
    except Exception as e:
        await send_error(update,context,user_id,f"Error in remove_moderator_: {e}")
