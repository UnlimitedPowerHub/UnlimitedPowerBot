from commands.commandRouter import CommandRouter
from commands.routercommands.admin import add_admin_,remove_admin_
from commands.routercommands.moderator import add_moderator_,remove_moderator_
from commands.routercommands.mute import mute_, unmute_,mute_list_bot
from commands.routercommands.ban import ban_,unban_,ban_list

router = CommandRouter()

router.add("staff.add.admin", add_admin_)
router.add("staff.remove.admin", remove_admin_)
router.add("staff.add.moderator", add_moderator_)
router.add("staff.remove.moderator", remove_moderator_)
router.add("mute",mute_)
router.add("unmute",unmute_)
router.add("mutelist",mute_list_bot)
router.add("ban",ban_)
router.add("unban",unban_)
router.add("banlist",ban_list)