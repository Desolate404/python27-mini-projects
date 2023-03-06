import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.send_sticker(message.chat.id,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLEGB9govSJ7hY80ANJPuZ_OxLk2zL9MpPTw&usqp=CAU')

@bot.message_handler(content_types=('text'))
def aaa(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id,'Привет')
    else:
        bot.send_message(message.chat.id,'Сообщение не распознанно')

@bot.message_handler(content_types=('sticker'))
def bbb(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)


bot.polling()

