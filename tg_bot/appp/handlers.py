from aiogram import Bot, Router, F, types
from aiogram.types import Message
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import random
import appp.keyboard as kb
from appp.frases_dic import frases_dic
from appp.smiles import smiles_list

# Initialize bot
def get_bot_token():
    with open('token.txt', 'r') as f:
        return f.readline().strip()

TOKEN = get_bot_token()
bot = Bot(token=TOKEN)
router = Router()

# Global scheduler (singleton)
scheduler = AsyncIOScheduler(timezone='Asia/Yekaterinburg')

# Get current weekday function
def get_weekday():
    return datetime.isoweekday(datetime.now())

# Increment day function
def increment_day(current_day):
    return current_day + 1

# Initialize day count
day = 582


# Start command to show menu
@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=kb.main)


# Single message sending
@router.message(F.text == 'Разовая отправка сообщения')
async def one_message(message: Message):
    global day
    day = increment_day(day)
    weekday = get_weekday()
    message_text = f'День {day} {random.choice(smiles_list)} \n{random.choice(frases_dic[str(weekday)])}'
    try:
        await bot.send_message(-1001924564036, message_text)
    except Exception as e:
        await message.answer(f"Ошибка при отправке сообщения: {e}")


# Daily message sender
async def send_message_cron():
    global day
    day = increment_day(day)
    weekday = get_weekday()
    message_text = f'День {day} {random.choice(smiles_list)} \n{random.choice(frases_dic[str(weekday)])}'
    try:
        await bot.send_message(-1001924564036, message_text)
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")


# Start scheduled message sending
@router.message(F.text == '\U000023F0 Начать рассылку')
async def do_job(message: Message):
    scheduler.add_job(send_message_cron, trigger='cron', hour='17', minute='*', start_date=datetime.now())
    if not scheduler.running:
        scheduler.start()
    await message.answer("Рассылка запущена!")
    
    # Periodic sleep to keep the bot running
    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Task was cancelled")


# Stop scheduled message sending
@router.message(F.text == '\U0001F6AB Завершить рассылку')
async def stop_schedule_job(message: Message):
    if scheduler.running:
        await scheduler.shutdown(wait=False)
        await message.answer("Рассылка остановлена!")
    else:
        await message.answer("Рассылка не запущена.")


# List of social network links
@router.message(F.text == 'Соц.сети')
async def social_net(message: Message):
    await message.answer('Рабочие соцсети', reply_markup=kb.social)


# List of study links
@router.message(F.text == 'Учеба')
async def study(message: Message):
    await message.answer('Учебные ссылки', reply_markup=kb.study)


# Echo function for unrecognized commands
@router.message()
async def echo(message: Message):
    await asyncio.sleep(10)
    await message.answer('Такой команды нет или надо подождать')


if __name__ == "__main__":
    # You can add your bot polling or webhook code here
    pass
