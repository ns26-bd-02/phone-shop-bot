from telegram import Update
from telegram.ext import CallbackContext

from database.phones import get_brands
from keyboards.menu import get_brand_keyboard


def handle_start(update: Update, context: CallbackContext) -> None:
    brands = get_brands()

    update.message.reply_html(
        text="Salom PhoneShop Botga xush kelibsiz, brand tanlang.",
        reply_markup=get_brand_keyboard(brands),
    )
