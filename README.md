# Telegram Bots
Репозиторий содержит два небольших pet-проекта: асинхронный [schedule-бот](#scheduler-bot) и легкий [бот-парсер](#currency-bot).

<a name="scheduler"><h2>Scheduler bot</h2></a>
Телеграмм-бот, созданный по запросу знакомого блогера. Автоматизирует ежедневную отправку необходимых сообщений по заданному шаблону в закрытый телеграмм канал.<br>
Дополнительный функционал предусматривает быстрый доступ к необходимым для личного использования ресурсам из меню бота.

### Технологии
- [aiogram](https://aiogram.dev/)
- [asyncio](https://docs.python.org/3/library/asyncio.html#module-asyncio)

### Использование
+ main для инициализации бота
+ appp
  - *frases* и *smiles*  &nbsp;&nbsp;&nbsp;- хранение списка выражений и смайлов для формирования сообщения по шаблону
  - *keyboard* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- кнопки управления, иными словами, интерфейс меню бота
  - *handlers*   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- исполнительные комманды

<a name="currency-bot"><h2>Currency bot</h2></a>
Простой парсер официального сайта ЦБ РФ для получения информации о текущем курсе валют с главной страницы.

### Технологии
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

### Использование
+ main для инициализации бота
+ currency_bot
  - *def run_currency_bot*  &nbsp;&nbsp;&nbsp;- запуск бота
  - *def get_text_messages* &nbsp;- интерфейс бота
  - *def callback_worker*   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- парсинг и вывод информации