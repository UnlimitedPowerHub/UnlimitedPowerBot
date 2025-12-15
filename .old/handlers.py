import traceback
from config import TARGET_GROUP_ID, SOURCE_CHANNEL_ID,LINK_REGEX
from commands.commands import router
from dbmanagers.noticechannel import set_message_map, get_group_message_id
from Logger import send_error,send_info,send_notice,send_warn
from telegram.ext import filters
from dbmanagers.user import get_users,add_user,remove_user

import re

async def router_command(update,context):
    try:
        if update.effective_message:
            await router.handle(update, context)
    except Exception as e:
        await send_error(update,context,"Bot",f"Critical Error in message_handler: {e}")
        traceback.print_exc()

async def message_handler(update, context):
    try:
        await router_command(update, context)
    except Exception as e:
        await send_error(update,context,"Bot",f"RouterCommand Error: {e}")
    try:
        await anti_link(update, context)
    except Exception as e:
        await send_error(update,context,"Bot",f"AntiLink Error: {e}")

class FilterNewChannelPost(filters.UpdateFilter):
    def filter(self, update):
        return bool(update.channel_post)

class FilterEditedChannelPost(filters.UpdateFilter):
    def filter(self, update):
        return bool(update.edited_channel_post)

IS_NEW_POST = FilterNewChannelPost()
IS_EDITED_POST = FilterEditedChannelPost()

async def handle_new_post(update, context):
    msg = update.channel_post
    ch_msg_id = str(msg.message_id) 

    try:
        forwarded_msg = await context.bot.forward_message(
            chat_id=TARGET_GROUP_ID,
            from_chat_id=SOURCE_CHANNEL_ID,
            message_id=msg.message_id
        )
        
        set_message_map(ch_msg_id, forwarded_msg.message_id)
        await send_info(update,context,SOURCE_CHANNEL_ID,"Forwarded New Message From Main Channel")

    except Exception as e:
        await send_error(update,context,"Bot",f"Error forwarding: {e}")

async def handle_edited_post(update, context):
    edited_msg = update.edited_channel_post
    ch_msg_id = str(edited_msg.message_id)

    old_group_msg_id = get_group_message_id(ch_msg_id)

    if old_group_msg_id:
        try:
            await context.bot.delete_message(
                chat_id=TARGET_GROUP_ID,
                message_id=int(old_group_msg_id)
            )
            await send_notice(update,context,"Bot","Deleted Old Message From Main Group")
        except Exception as e:
            await send_error(update,context,"Bot",f"Could not delete .old message from main group: {e}")
    else:
        await send_notice(update,context,"Bot", "No .old mapping found. It might be a new edit for an unmapped post.")
    
    try:
        new_forwarded_msg = await context.bot.forward_message(
            chat_id=TARGET_GROUP_ID,
            from_chat_id=SOURCE_CHANNEL_ID,
            message_id=edited_msg.message_id
        )
        
        set_message_map(ch_msg_id, new_forwarded_msg.message_id)
        
        await send_info(update,context,"Bot",f"Re-forwarded. New Group ID: {new_forwarded_msg.message_id}")
        
    except Exception as e:
        await send_error(update,context,"Bot",f"Error re-forwarding: {e}")


async def anti_link(update, context):

    message = update.message
    if not message:
        return

    text = message.text or ""
    matches = re.findall(LINK_REGEX, text)
    found_usernames = [u1 or u2 for u1, u2 in matches]

    if not found_usernames:
        return

    chat = message.chat

    for username in found_usernames:
        if username in get_users():
            continue

        try:
            await message.delete()
        except Exception as e:
            await send_error(update,context,"Bot","DELETE ERROR:", e)

        try:
            await send_warn(
                update,
                context,
                update.effective_user.id,
                f"Heyyyyy!!! <b>{message.from_user.mention_html()}</b>\n"
                f"Links are forbidden here!\n"
                f"Please don’t summon forbidden portals again"
            )
        except Exception as e:
            await send_error(update,context,"Bot","SEND_WARN ERROR:", e)

        try:
            await chat.send_message(
                f"Heyyyyy!!! <b>{message.from_user.mention_html()}</b>\n"
                f"Links are forbidden here!\n"
                f"Please don’t summon forbidden portals again",
                parse_mode="HTML"
            )
        except Exception as e:
            await send_error(update,context,"Bot","GROUP SEND ERROR:", e)

        return

async def join_handler(update, context):
    message = update.message
    if message is None:
        return

    try:
        await message.delete()
    except:
        pass

    for member in message.new_chat_members:
        username = member.username

        if username:
            add_user(username)

        await send_notice(update, context, update.effective_user.id, f"New User {username}!")

        await message.chat.send_message(
            f"🎉 <b>Welcome {member.mention_html()}!</b>\n"
            "You have entered the battlefield\n"
            "May your stay be legendary!",
            parse_mode="HTML"
        )

async def left_handler(update, context):
    message = update.message
    if message is None or message.left_chat_member is None:
        return

    try:
        await message.delete()
    except:
        pass

    member = message.left_chat_member
    username = member.username

    if username:
        remove_user(username)

    await send_notice(update, context, update.effective_user.id, f"User {username} Left!")

    await message.chat.send_message(
        f"💀 <b>{member.full_name}</b> is officially dead…\n"
        "They have left the arena. Rest in peace 🕊️",
        parse_mode="HTML"
    )


