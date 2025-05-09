from telebot import TeleBot
from config.env import env
from . import texts, keyboard

import logging

BOT_TOKEN = env.str("BOT_TOKEN")

bot = TeleBot(token=BOT_TOKEN, parse_mode='HTML')
logging.basicConfig(level=logging.INFO)


@bot.message_handler(commands=['start'])
def start_handler(message):
    first_name = message.from_user.first_name

    bot.send_message(
        chat_id=message.chat.id,
        text=texts.START.format(first_name),
        reply_markup=keyboard.WebappButton()
    )



bot.infinity_polling()

