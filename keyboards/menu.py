from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_brand_keyboard(brands: list[str]) -> ReplyKeyboardMarkup:
    buttons = []
    for brand in brands:
        buttons.append([KeyboardButton(brand)])

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
