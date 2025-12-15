from database import DataBase

noticechannel = DataBase("noticechannel.json")

def set_message_map(channel_msg_id, group_msg_id):
    noticechannel.set_key(str(channel_msg_id), group_msg_id)

def get_group_message_id(channel_msg_id):
    return noticechannel.get_key(str(channel_msg_id))