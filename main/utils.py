import telebot
import os
from dotenv import load_dotenv
import logger_setup

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

logger = logger_setup.setup_logger(__name__, 'main.log')


def send_to_telegram(message):
    try:
        bot = telebot.TeleBot(TELEGRAM_TOKEN)
        bot.send_message(CHAT_ID, message)
        logger.info(f"Message sent to Telegram: {message}")
    except Exception as e:
        logger.error(f"Failed to send message to Telegram: {e}")

