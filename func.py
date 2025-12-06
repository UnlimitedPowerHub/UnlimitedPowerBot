from dbmanagers.staff import admins,moderators
from config import OWNER

async def is_owner(user_id):
    return bool(OWNER == user_id)

async def is_admin(user_id):
    return bool(user_id in admins())

async def is_moderator(user_id):
    return bool(user_id in moderators())

async def is_owner_or_admin(user_id):
    return bool(is_admin(user_id) or is_owner(user_id))