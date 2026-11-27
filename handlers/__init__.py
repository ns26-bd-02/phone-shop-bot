from telegram.ext import (
    Dispatcher,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)

from .start import handle_start
from .phones import handle_brand, handle_phone


def add_command_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.add_handler(
        handler=CommandHandler(command="start", callback=handle_start)
    )


def add_message_handlers(dispatcher: Dispatcher) -> None:
    pass


def add_callback_query_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.add_handler(
        handler=CallbackQueryHandler(callback=handle_brand, pattern="brand:")
    )
    dispatcher.add_handler(
        handler=CallbackQueryHandler(callback=handle_phone, pattern="phone:")
    )


__all__ = [
    "add_command_handlers",
    "add_message_handlers",
    "add_callback_query_handlers",
]
