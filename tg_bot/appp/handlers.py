from aiogram import Bot, Router, F, types
from aiogram.types import Message, CallbackQuery
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import asyncio
import aioschedule

import random
import appp.keyboard as kb

from appp.frases_dic import frases_dic
from appp.smiles import smiles_list

with open('token.txt', 'r') as f:
    TOKEN = f.readline()
bot = Bot(token=TOKEN)

router = Router()
day = 582
now = datetime.now()
weekday = datetime.isoweekday(now)
scheduler = AsyncIOScheduler(timezone='Asia/Yekaterinburg')


# Стартовая комманда, открывает меню.
@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=kb.main)
    # scheduler.start()


# Разовая отправка сообщения.
@router.message(F.text == 'Разовая отправка сообщения')
async def one_message(message: Message):
    global day
    day = day + 1
    await bot.send_message(-1001924564036, (f'День {day} {random.choice(smiles_list)} \n{random.choice(frases_dic[str(weekday)])}'))


# Запус ежедневной рассылки.
async def send_message_cron():
    global day
    day = day + 1
    await bot.send_message(-1001924564036, (f'День {day} {random.choice(smiles_list)} \n{random.choice(frases_dic[str(weekday)])}'))


@router.message(F.text == '\U000023F0 Начать рассылку')
async def do_job(message: Message):
    scheduler = AsyncIOScheduler(timezone='Asia/Yekaterinburg')
    scheduler.add_job(send_message_cron, trigger='cron', hour='21', minute='*', start_date=datetime.now())
    scheduler.start()
    while True:
        await asyncio.sleep(1)
    
# Завершение ежедневной рассылки.
@router.message(F.text == '\U0001F6AB Завершить рассылку')
async def stop_schedule_job(message: Message):
    await scheduler.shutdown(wait=False)

# Список ссылок социальных сетей для будущей работы в IT.
@router.message(F.text == 'Соц.сети')
async def social_net(message: Message):
    await message.answer('Рабочие соцсети', reply_markup=kb.social)

# Список ссылок для учёбы в MathsHub.
@router.message(F.text == 'Учеба')
async def study(message: Message):
    await message.answer('Учебные ссылки', reply_markup=kb.study)

# Эхо-функция для ответа на несуществующие запросы.
@router.message()
async def echo(message: Message):
    await asyncio.sleep(10)
    await message.answer('Такой команды нет или надо подождать')
