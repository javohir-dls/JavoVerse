from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💱 Valyuta kursi"), KeyboardButton(text="🕒 Dunyo soati")],
        [KeyboardButton(text="🕌 Namoz vaqti"), KeyboardButton(text="📿 99 Ism")],
        [KeyboardButton(text="🌤 Ob-havo"), KeyboardButton(text="📅 Yosh kalkulyatori")]
    ],
    resize_keyboard=True
)

@router.message()
async def show_menu(message: types.Message):
    if message.text == "🏠 Menu":
        await message.answer("📌 Asosiy menyu:", reply_markup=main_menu)
