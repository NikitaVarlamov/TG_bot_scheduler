# TG_bot_scheduler
Телеграмм-бот, созданный по запросу знакомого блогера. Автоматизирует ежедневную отправку необходимых шаблонных сообщений в закрытый телеграмм канал.
Дополнительный функционал предусматривает быстрый доступ к необходимым ресурсам из меню бота.

## Технологии
- [aiogram](https://aiogram.dev/)
- [asyncio](https://docs.python.org/3/library/asyncio.html#module-asyncio)
- requirements.txt - полный необходимый список пакетов 

## Разработка
### main
  Создание бота
### appp
- *frases.dic и smiles*   для хранения вариантов текста сообщения в зависимости от дня недели
- *keyboard*              интерфейс меню бота
- *handlers*              исполнительные комманды

# TG_bot_currency
Телеграмм-бот, легкий парсер официального сайта ЦБ РФ для получения информации о текущем курсе валют с главной страницы.

## Технологии
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- requirements.txt - полный необходимый список пакетов 

## Разработка
### main
  Запуск бота
### currency_bot
- *def run_currency_bot*  запуск бота
- *def get_text_messages* интерфейс бота
- *def callback_worker*   парсинг и вывод информации