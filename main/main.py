import asyncio
import aiohttp
import requests_cache
import random
import logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from utils import send_to_telegram
from constants import (HLTV_ORG, EXPIRE_AFTER, USER_AGENT_1, 
                       USER_AGENT_2, USER_AGENT_3, USER_AGENT_4, 
                       USER_AGENT_5, USER_AGENT_6)


class Parse:
    def __init__(self, link) -> None:
        self.link = link
        self.session = requests_cache.CachedSession(expire_after=EXPIRE_AFTER)
        self.user_agents = [
            USER_AGENT_1,
            USER_AGENT_2,
            USER_AGENT_3,
            USER_AGENT_4,
            USER_AGENT_5,
            USER_AGENT_6
            ]
        self.last_news = None


    async def fetch_news(self):
        async with aiohttp.ClientSession() as session:
            user_agent = random.choice(self.user_agents)
            headers = {
                'User-Agent': user_agent
                }
            async with session.get(self.link, headers=headers) as response:
                response_text = await response.text()
                soup = BeautifulSoup(response_text, features='lxml')
                tag_div = soup.find_all('a', attrs={'class': 'newsline article'})
                news_links = set()
                for link in tag_div:
                    href = link['href']
                    news_link = urljoin(HLTV_ORG, href)
                    news_links.add(news_link)
                return news_links


    async def parse_today_news(self):
        while True:
            current_news = await self.fetch_news()
            if self.last_news is None:
                self.last_news = current_news
            else:
                new_news = current_news - self.last_news
                if new_news:
                    for news in new_news:
                        send_to_telegram(news)
                        logging.info(f"Sent news to Telegram: {news}")
                    self.last_news = current_news
            await asyncio.sleep(300)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s, %(levelname)s, %(name)s, %(message)s',
        filename='main.log',
        encoding='utf-8'

    )
    
    # Создание обработчика для вывода в консоль
    console_handler = logging.StreamHandler()
    # Установка уровня логирования для обработчика
    console_handler.setLevel(logging.INFO)
    # Создание форматировщика для вывода в консоль
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # Привязка форматировщика к обработчику
    console_handler.setFormatter(console_formatter)
    # Получение корневого логгера
    root_logger = logging.getLogger()
    # Добавление обработчика в корневой логгер
    root_logger.addHandler(console_handler)
    logging.info('Парсер запущен!')
    
    parser = Parse(HLTV_ORG)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(parser.parse_today_news())