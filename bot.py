from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
from config import Token, SOURCE_CHANNEL_ID
from commands.start import start
from handlers import message_handler, handle_new_post, handle_edited_post,IS_EDITED_POST,IS_NEW_POST,anti_link,join_handler,left_handler

def main():
    app = ApplicationBuilder().token(Token).build()
    
    app.add_handler(CommandHandler("start", start))
    
    my_channel = filters.Chat(chat_id=SOURCE_CHANNEL_ID)

    app.add_handler(MessageHandler(my_channel & IS_NEW_POST, handle_new_post))
    
    app.add_handler(MessageHandler(my_channel & IS_EDITED_POST, handle_edited_post))

    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, join_handler))

    app.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, left_handler))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, anti_link))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()