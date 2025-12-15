from db.db import DB

users = DB('users')


def get_users():
    return users.get_all()


def exist_user(userid):
    return users.exist(userid)


def add_user(userid, user_data):
    users.set_key(userid, user_data)


def get_user_data(userid):
    return get_users()[str(userid)]
