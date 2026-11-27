from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from database.phones import get_phones_by_brand, get_phones_by_id
from keyboards.phones import get_phones_keyboard
from utils.formatter import format_phone


def handle_brand(update: Update, context: CallbackContext) -> None:
    data = update.callback_query.data

    brand = data.split(":")[1]

    phones = get_phones_by_brand(brand)

    update.callback_query.message.reply_html(
        text=f"{brand} telefonlar",
        reply_markup=get_phones_keyboard(phones),
    )


def handle_phone(update: Update, context: CallbackContext) -> None:
    data = update.callback_query.data

    phone_id = data.split(":")[1]

    phone = get_phones_by_id(int(phone_id))

    update.callback_query.message.reply_photo(
        caption=format_phone(phone), photo=phone["photo"], parse_mode=ParseMode.HTML
    )
