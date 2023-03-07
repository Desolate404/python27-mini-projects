import telebot
from decouple import config
from bot.buttons import get_keyboard
from parsing.db_utils import get_db
from parsing.main import parse


bot = telebot.TeleBot(config('TOKEN'))

@bot.message_handler(commands=['start'])
def start(message):
    text =''' "Hello, we are parsing https://www.kivano.kg/igrushki" '''
    bot.send_message(message.chat.id, text, disable_web_page_preview=True)
    
    if not get_db():
        parse()
    
    bot.send_message(message.chat.id, 'Chose the page', reply_markup=get_keyboard())

@bot.callback_query_handler(lambda x: True)
def send_data(call):
    db = get_db()
    page = call.data
    products = db[page]
    for prod in products:
        text = f'''title: {prod['title']},Price: {prod['price']}'''
        bot.send_message(call.from_user.id, text)
    start(call.message)

bot.polling()