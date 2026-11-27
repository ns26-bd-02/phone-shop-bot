from telegram.ext import Updater

from config import settings


def main():
    updater = Updater(settings.TOKEN)
    dispatcher = updater.dispatcher

    print("Bot is running...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
