from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()


def main_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="💱 Valyuta kursi"),
                KeyboardButton(text="🕒 Dunyo soati")
            ],
            [
                KeyboardButton(text="🕌 Namoz vaqti"),
                KeyboardButton(text="📿 Allohning 99 ismi")
            ],
            [
                KeyboardButton(text="🌦 Ob-havo"),
                KeyboardButton(text="🎂 Yosh kalkulyatori")
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Kerakli bo'limni tanlang..."
    )

    return keyboard
