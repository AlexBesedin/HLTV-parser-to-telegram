# HLTV-parser-to-telegram
## Описание проекта:

Данная утилита, выполняет парсинг информации о последней добавленной новости на сайте HLTV.org каждые 5 минут. Если найдена новая новость (то есть ссылка на новость, которая отсутствовала на предыдущей итерации парсинга), то ссылка отправляется в телеграм чат сообщества. 

## Технологии:
- **aiohttp**: для работы с сетевыми запросами.
- **beautifulsoup4**: для парсинга HTML и XML.
- **pyTelegramBotAPI**: для создания Telegram-бота.
- **requests**: для выполнения HTTP-запросов.
- **requests-cache**: для кеширования HTTP-ответов.

## Как запустить проект:

```sh
git clone git@github.com:AlexBesedin/HLTV-parser-to-telegram.git
cd HLTV-parser-to-telegram
```
Cоздать и активировать виртуальное окружение:
```sh
python3 -m venv env
```
Если у вас Linux/macOS:
```sh
source env/bin/activate
```
Если у вас windows
```sh
source env/scripts/activate
```
```sh
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```sh
python -m pip install -r requirements.txt
```
Создать файл с переменными окружения .env
```sh
touch .env
```
Пример содержимого файла .env:
```sh
TELEGRAM_TOKEN =Y1235124643414645513125
CHAT_ID =-41281282371851923981293
```
Установите docker и docker-compose:
```sh
sudo apt install docker.io 
sudo apt install docker-compose
```
Соберите контейнер:
```sh
sudo docker-compose up -d --build
```



