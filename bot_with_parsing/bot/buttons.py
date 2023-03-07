from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from parsing.db_utils import get_pages


def get_keyboard():
    pages = get_pages()

    pages_keyboard = InlineKeyboardMarkup()

    buttons = []
    for page in pages:
        button = InlineKeyboardButton(page, callback_data=page)
        buttons.append(button)

    pages_keyboard.add(*buttons)
    return pages_keyboard
