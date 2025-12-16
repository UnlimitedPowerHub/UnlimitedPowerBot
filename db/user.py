from db.db import DB
from bot_config import OWNER_ID

users = DB('users')


def is_owner(userid):
    return bool(str(userid) == str(OWNER_ID))


def get_users():
    return users.get_all()


def exist_user(userid):
    return users.exist(userid)


def add_user(userid, user_data):
    users.set_key(userid, user_data)


def get_user_data(userid):
    return get_users()[str(userid)]
