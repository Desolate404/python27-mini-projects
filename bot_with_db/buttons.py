from telebot import types
from utils import get_pages

keyboard = types.InlineKeyboardMarkup()

pages = get_pages()
buttons = []
for page in pages:
    button = types.InlineKeyboardButton(page, callback_data=page)
    buttons.append(button)

keyboard.add(*buttons)
