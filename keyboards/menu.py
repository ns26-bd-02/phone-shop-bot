from telegram import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)


def get_menu_keyboard(brands: list[str]) -> ReplyKeyboardMarkup:
    buttons = [
        [
            KeyboardButton("Sozlamalar"),
            KeyboardButton("Zakazlarim"),
        ]
    ]

    return ReplyKeyboardMarkup(keyboard=buttons)
