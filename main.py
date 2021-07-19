import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('Магазин')
    item2 = types.KeyboardButton('Баланс')
    item3 = types.KeyboardButton('Поддержка')
    item4 = types.KeyboardButton('Промокод')
    item5 = types.KeyboardButton('Реферальная программа')
    item6 = types.KeyboardButton('Наличие')
    item7 = types.KeyboardButton('Диспут/ненаход')
    item8 = types.KeyboardButton('Отзывы')
    item9 = types.KeyboardButton('Поддержка и правила')
    item10 = types.KeyboardButton('Обменки')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

    bot.send_message(message.chat.id, 
        'Дамы и господа приветствуем'.format(
        message.from_user, 
        bot.get_me()), 
        parse_mode='html', 
        reply_markup=markup)



@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == 'Магазин': 


            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            item1 = telebot.types.InlineKeyboardButton('Cookies', callback_data='good')
            markup.add(item1)
                       
                       
            bot.send_message(message.chat.id,
            "Отлично сам как?", reply_markup=markup)

# запуск бота
bot.polling(none_stop=True)