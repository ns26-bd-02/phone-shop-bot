from telegram.ext import Updater

from config import settings
from handlers import add_command_handlers, add_message_handlers


def main():
    updater = Updater(settings.TOKEN)

    add_command_handlers(updater.dispatcher)
    add_message_handlers(updater.dispatcher)

    print("Bot is running...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
