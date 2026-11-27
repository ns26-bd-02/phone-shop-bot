from telegram import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def get_brand_keyboard(brands: list[str]) -> InlineKeyboardMarkup:
    buttons = []
    for brand in brands:
        buttons.append(
            [InlineKeyboardButton(text=brand, callback_data=f"brand:{brand}")]
        )

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_phones_keyboard(phones: list[dict]) -> InlineKeyboardMarkup:
    buttons = []
    for phone in phones:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=phone["model"], callback_data=f"phone:{phone['id']}"
                )
            ]
        )

    return InlineKeyboardMarkup(inline_keyboard=buttons)
