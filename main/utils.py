import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def send_to_telegram(message):
        bot = telebot.TeleBot(TELEGRAM_TOKEN)
        bot.send_message(CHAT_ID, message)