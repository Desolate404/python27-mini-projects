import telebot
from decouple import config


token = config('TOKEN')

#СТИКЕРЫ
yes_sticker = 'CAACAgIAAxkBAAEIBYVkBYbtb9jM0CQuA4KvD9CEBDeEZwACSgIAAladvQrJasZoYBh68C4E'
no_sticker = 'CAACAgIAAxkBAAEIBYNkBYbpeaSqmfg6viQTA808U0hKrgACKwADWbv8JTA6_WvNgxy4LgQ'

#Клавиатура под сообщением
keyboard = telebot.types.InlineKeyboardMarkup()
b1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
b2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(b1, b2)


bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку',reply_markup=keyboard)

# Func - Функция фильтр, в данном случае разрешается все сообщения
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_sticker)

bot.polling()