from telegram.ext import (
    Dispatcher,
    CommandHandler,
)

from .start import handle_start


def add_command_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.add_handler(
        handler=CommandHandler(command="start", callback=handle_start)
    )


def add_message_handlers(dispatcher: Dispatcher) -> None:
    pass


__all__ = [
    "add_command_handlers",
    "add_message_handlers",
]
