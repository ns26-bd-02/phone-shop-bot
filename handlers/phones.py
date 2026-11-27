from telegram import Update
from telegram.ext import CallbackContext

from database.phones import get_phones_by_brand
from keyboards.phones import get_phones_keyboard


def handle_brand(update: Update, context: CallbackContext) -> None:
    data = update.callback_query.data

    brand = data.split(":")[1]

    phones = get_phones_by_brand(brand)

    update.callback_query.message.reply_html(
        text=f"{brand} telefonlar",
        reply_markup=get_phones_keyboard(phones),
    )
