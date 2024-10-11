import asyncio
from aiogram import Bot, Dispatcher
from appp.handlers import router
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from appp import handlers


with open('token.txt', 'r') as f:
    TOKEN = f.readline()
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)
loop = asyncio.get_event_loop()

# Polling - постоянная работа бота.
async def main():
    await dp.start_polling(bot)

# def main() запускается только с этого файла.
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
