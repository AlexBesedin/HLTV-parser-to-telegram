import telebot
import os
import logging
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='telegram.log',
    encoding='utf-8'
)
logger = logging.getLogger(__name__)

def send_to_telegram(message):
    try:
        bot = telebot.TeleBot(TELEGRAM_TOKEN)
        bot.send_message(CHAT_ID, message)
        logger.info(f"Message sent to Telegram: {message}")
    except Exception as e:
        logger.error(f"Failed to send message to Telegram: {e}")

