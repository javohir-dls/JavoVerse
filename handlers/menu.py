from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    keyboard = [
        [KeyboardButton(text="💱 Valyuta kursi")],
        [KeyboardButton(text="🕒 Dunyo soati")],
        [KeyboardButton(text="🕌 Namoz vaqti")],
        [KeyboardButton(text="📿 Allohning 99 ismi")],
        [KeyboardButton(text="🌤 Ob-havo")],
        [KeyboardButton(text="🎂 Yosh kalkulyatori")]
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
