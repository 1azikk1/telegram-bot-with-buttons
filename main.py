from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton


bot = TeleBot('7315003162:AAEzvIEzzoEPhQ-6VVk-jLV42uxbNcPRrVY')
admin = '@ahmadjonovazizbek'


@bot.message_handler(commands=['start', 'about', 'dev', 'id'])
def reaction_to_start(message: Message):
    print(message)
    chat_id = message.chat.id
    if message.text == '/start':
        bot.send_message(chat_id, f"Assalomu alaykum {message.from_user.full_name}")

        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        help_button = KeyboardButton('about🤖')
        dev_button = KeyboardButton('dev 🧑‍💻')
        id_button = KeyboardButton('ID ✅')

        markup.add(help_button, dev_button, id_button)

        bot.send_message(chat_id, "Bot haqida ma'lumot olish uchun menyudagi tugmalardan birini tanlang!",
                         reply_markup=markup)

    elif message.text == '/about':
        bot.send_message(chat_id, "Ushbu @simple_difficultBOT Na'jot Ta'lim o'quvchisi Azizbek Ahmadjonov tomonidan "
                                  "2024-yilning 11-oktabr kuni yaratildi!")
    elif message.text == '/dev':
        bot.send_message(chat_id, f"Admin: {admin}")
    elif message.text == '/id':
        bot.send_message(chat_id, f"Sizning id: {message.from_user.id}")


@bot.message_handler(func=lambda message: True)
def reaction_to_buttons(message: Message):
    chat_id = message.chat.id

    if message.text == 'about🤖':
        bot.send_message(chat_id, "Ushbu @simple_difficultBOT Na'jot Ta'lim o'quvchisi Azizbek Ahmadjonov tomonidan "
                                  "2024-yilning 11-oktabr kuni yaratildi!")
    elif message.text == 'dev 🧑‍💻':
        bot.send_message(chat_id, f"Admin: {admin}")
    elif message.text == 'ID ✅':
        bot.send_message(chat_id, f"Sizning id: {message.from_user.id}")


bot.infinity_polling()
