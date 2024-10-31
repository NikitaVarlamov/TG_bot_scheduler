from aiogram.types import (ReplyKeyboardMarkup, 
                     KeyboardButton,
                     InlineKeyboardMarkup, 
                     InlineKeyboardButton)

main_kb = [
    [KeyboardButton(text='\U000023F0 Начать рассылку'),
     KeyboardButton(text='\U0001F6AB Завершить рассылку'),
     KeyboardButton(text='Разовая отправка сообщения')],
    [KeyboardButton(text='Учеба'),
     KeyboardButton(text='Соц.сети')
     ]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                          resize_keyboard=True,
                          input_field_placeholder='Выберите комманду')

social = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Habr', url='https://career.habr.com/mahgapuhka')],
    [InlineKeyboardButton(text='LinkedIn', url='https://clck.ru/35qmRB')]
])

study = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Программа', url='https://canvas.instructure.com/courses/7174946')],
    [InlineKeyboardButton(text='Оценки', url='https://canvas.instructure.com/courses/7174946/grades')],
    [InlineKeyboardButton(text='Drive', url='https://drive.google.com/drive/u/0/my-drive')]
])