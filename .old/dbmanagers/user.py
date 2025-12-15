from database import DataBase

user = DataBase("user.json")

def add_user(username_or_userid):
    user.set_path(["users"], username_or_userid)

def remove_user(username_or_userid):
    user.remove_path(["users"], username_or_userid)

def get_users():
    return user.all().get("users", {})

def add_ban(user_id):
    user.set_path(["bans"], user_id)

def remove_ban(user_id):
    user.remove_path(["bans"], user_id)

def get_bans():
    return user.all().get("bans", {})

def mute(user_id):
    user.list_add_path(["mutes"], user_id)

def unmute(user_id):
    user.list_remove_path(["mutes"], user_id)

def is_mute(user_id):
    mutes = user.get_path(["mutes"], [])
    return user_id in mutes

def get_mutes():
    return user.get_path(["mutes"], [])
