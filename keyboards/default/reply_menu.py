from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/start"), KeyboardButton(text="/help")],
    ],
    resize_keyboard=True
)
