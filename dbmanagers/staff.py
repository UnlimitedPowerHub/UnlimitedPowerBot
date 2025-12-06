from database import DataBase

staff=DataBase('staff.json')

def admin(user_id):
    return staff.get_path(["admins"],user_id)

def admins():
    return staff.get_path(["admins"])

def add_admin(user_id):
    staff.list_add("admins",user_id)

def remove_admin(user_id):
    staff.list_remove("admins",user_id)

def moderators():
    return staff.get_path(["moderators"])

def add_moderator(user_id):
    staff.list_add("moderators",user_id)

def remove_moderator(user_id):
    staff.list_remove("moderators",user_id)
