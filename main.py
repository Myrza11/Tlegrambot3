# # импорт всех пакетов
# import telebot
# import config
# import random
# from telebot import types
# # создаем экземпляр класса
# bot = telebot.TeleBot(config.TOKEN)

# # дикоратор с помощью комманды старт мы запускаем его
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     # добавляем стикер
#     sti = open('static/statick.html', "rb")
#     # отправляем стикер в чат
#     bot.send_sticker(message.chat.id, sti)

#     # средство для подключения кнопок
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     # кнопки
#     item1 = types.KeyboardButton('рандомное число')
#     item2 = types.KeyboardButton('как дела')
#     item3 = types.KeyboardButton('я тебя люблю')
#     item4 = types.KeyboardButton('мне нужна помошь!')
#     item5 = types.KeyboardButton('где я?')
#     item6 = types.KeyboardButton('я красивый?')
#     item7 = types.KeyboardButton('где летали люди?')
#     item8 = types.KeyboardButton('когда началась вторая мировая война?')
#     item9 = types.KeyboardButton('Какой сегодня день')
#     item10 = types.KeyboardButton('здесь есть посхалка?')
#     item11 = types.KeyboardButton('ты умный?')
#     markup.add(item1, item2, item4, item5, item6, item7, item8, item9, item10, item11)
#     # приветственное сообщение с выводом кнопок
#     bot.send_message(message.chat.id, 
#         'Добро пожаловать {0.first_name}!\n Я {1.first_name}, бот, который тебя приветствует'.format(
#         message.from_user, 
#         bot.get_me()), 
#         parse_mode='html', 
#         reply_markup=markup)

# # нужно чтоб вводить сообщение и обработка кнопок
# @bot.message_handler(content_types=['text'])
# def blabla(message):
#     # обработка кнопок рандом
#     if message.text == 'рандомное число':
#         bot.send_message (message.chat.id, str(random.randint(1, 1000000)))
#     # вывод логической цепочки
#     elif message.text == "мне нужна помошь!":
#         bot.send_message (message.chat.id, "Иди гугли")
#     elif message.text == "где я?":
#         bot.send_message (message.chat.id, "в Кыргызстане в Бишкеке на улице Разакова")
#     elif message.text == "я красивый?":
#         bot.send_message (message.chat.id, "да")
#     elif message.text == "где летали люди?":
#         bot.send_message (message.chat.id, "в облаках")
#     elif message.text == 'как дела': 


#             markup = telebot.types.InlineKeyboardMarkup(row_width=2)
#             item1 = telebot.types.InlineKeyboardButton('Хорошо', callback_data='good')
#             item2 = telebot.types.InlineKeyboardButton('Плохо', callback_data='bad')
#             markup.add(item1, item2)
                       
                       
#             bot.send_message(message.chat.id,
#             "Отлично сам как?", reply_markup=markup)


#     elif message.text == 'когда началась вторая мировая война?': 
#             markup = telebot.types.InlineKeyboardMarkup(row_width=2)
#             item1 = telebot.types.InlineKeyboardButton('1939', callback_data='a')
#             item2 = telebot.types.InlineKeyboardButton('1945', callback_data='b')
#             markup.add(item1, item2)

#             bot.send_message(message.chat.id,
#             "вторая мировая война началась в:", reply_markup=markup)


#     elif message.text == 'Какой сегодня день': 
#             markup = telebot.types.InlineKeyboardMarkup(row_width=2)
#             item1 = telebot.types.InlineKeyboardButton('4 июня', callback_data='d')
#             item2 = telebot.types.InlineKeyboardButton('хороший', callback_data='w')
#             markup.add(item1, item2)

#             bot.send_message(message.chat.id,
#             "Сегодня:", reply_markup=markup)


#     elif message.text == "я тебя люблю":
#             markup = telebot.types.InlineKeyboardMarkup(row_width=2)
#             item1 = telebot.types.InlineKeyboardButton('Женшина', callback_data='q')
#             item2 = telebot.types.InlineKeyboardButton('Мужчина', callback_data='m')
#             markup.add(item1, item2)

#             bot.send_message(message.chat.id,
#             "Ты кто?:", reply_markup=markup)


        
#     elif message.text == "здесь есть пасхалка?":
#             markup = telebot.types.InlineKeyboardMarkup(row_width=2)
#             item1 = telebot.types.InlineKeyboardButton('как вывести пасхалку', callback_data='z')
#             item2 = telebot.types.InlineKeyboardButton('сколько пасхалков', callback_data='h')
#             markup.add(item1, item2)

#             bot.send_message(message.chat.id,
#             "Тебе сказать какие пасхалки?:", reply_markup=markup)        

#     elif message.text == "ты умный?":
#             markup = telebot.types.InlineKeyboardMarkup(row_width=2)
#             item1 = telebot.types.InlineKeyboardButton('я тоже умный', callback_data='p')
#             item2 = telebot.types.InlineKeyboardButton('нет я дурак', callback_data='t')
#             markup.add(item1, item2)

#             bot.send_message(message.chat.id,
#             "да а ты?:", reply_markup=markup)

#     else:
#         bot.send_message(message.chat.id, 'Я не знаю что ответить🦥')



# # обратная свясь с пользователем
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     # обработка логической цепочки
#     try:
#         if call.message:
#             if call.data == 'good':
#                 bot.send_message(call.message.chat.id, 'Очень хорошо, я за тебя рад)')
#             elif call.data == 'bad':
#                 bot.send_message(call.message.chat.id, 'Чыдап койсон отуп кетет')     
#             elif call.data == 'b':
#                 bot.send_message(call.message.chat.id, 'ошибка')
#             elif call.data == 'a':
#                 bot.send_message(call.message.chat.id, 'правильно')
#             elif call.data == "d":
#                 bot.send_message(call.message.chat.id, 'правильно')
#             elif call.data == "w":
#                 bot.send_message(call.message.chat.id, 'пусть он будет таким всегда')
#             elif call.data == "q":
#                 bot.send_message(call.message.chat.id, 'Можешь любить дальше')
#             elif call.data == "m":
#                 bot.send_message(call.message.chat.id, 'Эммм... но я мужик')
#             elif call.data == "z":
#                 bot.send_message(call.message.chat.id, 'Напиши я тебя люблю')
#             elif call.data == "h":
#                 bot.send_message(call.message.chat.id, 'одна')
#             elif call.data == "p":
#                 bot.send_message(call.message.chat.id, 'продолжайте быть им')
#             elif call.data == "t":
#                 bot.send_message(call.message.chat.id, 'соболезную')

#             bot.edit_message_text(
#                 chat_id = call.message.chat.id,
#                 message_id = call.message.message_id,
#                 reply_markup=None
#             )
#     except Exception as e:
#         print(repr(e))

# # запуск бота
# bot.polling(none_stop=True)





