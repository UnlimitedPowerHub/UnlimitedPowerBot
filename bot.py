from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

from bot_config import TOKEN
from command.start import start
from command.help import help
from command.command import set_my_commands

def main():

    bot = ApplicationBuilder().token(TOKEN).post_init(set_my_commands).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("help", help))

    bot.add_handler(CallbackQueryHandler(help, "^help_btn$"))

    bot.run_polling()


if __name__ == "__main__":
    main()
