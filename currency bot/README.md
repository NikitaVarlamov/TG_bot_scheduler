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