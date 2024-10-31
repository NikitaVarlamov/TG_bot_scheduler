import re
import requests
import logging
import telebot
from telebot import types
from bs4 import BeautifulSoup

# Set up logging
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

def run_currency_bot(token: str) -> None:
    """ Run bot that returns today's currency from https://cbr.ru/ """
    bot = telebot.TeleBot(token, parse_mode=None)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        """ Respond to text messages """
        if message.text == "/start":
            keyboard = types.InlineKeyboardMarkup()
            key_usd = types.InlineKeyboardButton(text='Доллар', callback_data='usd')
            keyboard.add(key_usd)
            key_eur = types.InlineKeyboardButton(text='Евро', callback_data='eur')
            keyboard.add(key_eur)
            key_cny = types.InlineKeyboardButton(text='Юань', callback_data='cny')
            keyboard.add(key_cny)
            bot.send_message(message.from_user.id,
                             "Привет! Я бот-конвертер валют.\nВведите валюту для которой вы хотите получить её курс ЦБ.",
                             reply_markup=keyboard)
        elif message.text == "":
            bot.send_message(message.from_user.id, "Введите валюту для которой вы хотите получить её курс ЦБ")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        valid_currencies = {'usd': [2, "доллара"], 'eur': [4, "евро"], 'cny': [0, "юаня"]}
        
        """ Respond to keyboard calls """
        if call.data not in valid_currencies:
            bot.send_message(call.message.chat.id, 'Я пока не умею работать с этой валютой')
            return

        try:
            r = requests.get('https://cbr.ru/')
            r.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(r.text, "html.parser")
            data = soup.findAll('div', class_='col-md-2 col-xs-9 _right mono-num')

            if len(data) != 6:
                bot.send_message(call.message.chat.id, 'Упссс, я сломался')
                return

            helper = valid_currencies[call.data]
            info = str(data[helper[0]].text)

            match = re.search(r'(\d+,?\d*)\s*₽', info)
            if match:
                value = float(match.group(1).replace(',', '.'))
                bot.send_message(call.message.chat.id, f'Текущий курс {helper[1]} равен {value} рублей')
            else:
                bot.send_message(call.message.chat.id, 'Не удалось получить курс валюты.')

        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            bot.send_message(call.message.chat.id, 'Не удалось получить данные о курсе валют. Попробуйте позже.')
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            bot.send_message(call.message.chat.id, 'Произошла ошибка. Попробуйте позже.')

    # Start the bot
    bot.infinity_polling()