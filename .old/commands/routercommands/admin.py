from dbmanagers.staff import add_admin, remove_admin, admin
from Logger import send_notice,send_info,send_error
from func import is_owner

async def add_admin_(update, context, args):
    try:
        reply = update.effective_message.reply_to_message
        user_id = update.effective_user.id
        fff="Tried To Use staff.add.admin Command"
        
        if not is_owner(user_id):
            await send_notice(update,context,user_id,fff)
            return
        
        if not reply:
            await update.effective_message.reply_text("Please Reply To An User")
            await send_notice(update,context,user_id,fff)
            return
        target_id = reply.from_user.id
        
        if admin(target_id) is not None:
            await update.effective_message.reply_text("User Already Is Admin")
            await send_notice(update,context,update.effective_user.id,f"Tried To Add Admin User {target_id}")
            return
        add_admin(target_id)
        textt=f"Admin Added - ID: `{target_id}`"
        await update.effective_message.reply_text(textt, parse_mode="Markdown")
        await send_info(update,context,user_id,textt)
    except ValueError:
        tttt="Invalid ID Format"
        await update.effective_message.reply_text(tttt)
        await send_error(update,context,user_id,tttt+"\n Use staff.add.admin Command")
    except Exception as e:
        await send_error(update,context,user_id,f"Error in add_admin_: {e}")

async def remove_admin_(update, context, args):
    try:
        reply = update.effective_message.reply_to_message
        user_id = update.effective_user.id
        fff="Tried To Use staff.remove.admin Command"
        if not is_owner(user_id):
            await send_notice(update,context,user_id,fff)
            return
        
        if not reply:
            await update.effective_message.reply_text("Please Reply To An User")
            await send_notice(update,context,user_id,fff)
            return
        target_id = reply.from_user.id
        
        if admin(target_id) is None:
            await update.effective_message.reply_text("User Is Not Admin")
            await send_notice(update,context,update.effective_user.id,f"Tried To Remove Admin User {target_id}")
            return
        remove_admin(target_id)
        textt=f"Admin Removed - ID: `{target_id}`"
        await update.effective_message.reply_text(textt, parse_mode="Markdown")
        await send_info(update,context,user_id,textt)
    except ValueError:
        tttt="Invalid ID Format"
        await update.effective_message.reply_text(tttt)
        await send_error(update,context,user_id,tttt+"\n Use staff.remove.admin Command")
    except Exception as e:
        await send_error(update,context,user_id,f"Error in remove_admin_: {e}")
        