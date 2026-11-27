from telegram.ext import Updater

from config import settings


def main():
    updater = Updater(settings.TOKEN)
    dispatcher = updater.dispatcher

    updater.start_polling()
    updater.idle()
    print("Bot is running...")


if __name__ == "__main__":
    main()
