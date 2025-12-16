from telegram import BotCommand
from telegram.ext import Application

commands = {
    'start': 'start bot',
    'help': 'get help message',
    'broadcast': 'broadcast a message'
}


def list_command():
    lc = f""
    for command in commands:
        lc += f" ‣ <b>{command}</b> ⇾ {commands[command]}\n"
    return lc


async def set_my_commands(application: Application):
    c_ = []
    for command in commands:
        c_.append(BotCommand(command, commands[command]))
    await application.bot.set_my_commands(c_)
