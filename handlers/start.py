from telegram import Update
from telegram.ext import CallbackContext

from database.phones import get_brands
from keyboards.menu import get_menu_keyboard
from keyboards.phones import get_brand_keyboard


def handle_start(update: Update, context: CallbackContext) -> None:
    brands = get_brands()

    update.message.reply_html(
        text="Salom xush kelibsiz",
        reply_markup=get_menu_keyboard(brands),
    )

    update.message.reply_html(
        text="Brand tanlang",
        reply_markup=get_brand_keyboard(brands),
    )
