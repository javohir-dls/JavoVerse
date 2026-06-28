from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

# 🔐 Kanallar
CHANNEL_1 = "@xushboqovblog"
CHANNEL_2 = "@xushboqovblog"  # agar 2 ta kanal bo‘lsa keyin almashtirasan

# 🌐 Ijtimoiy tarmoqlar
INSTAGRAM = "@javohir.ftbl"


def check_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Telegram kanal", url=f"https://t.me/{CHANNEL_1[1:]}")],
        [InlineKeyboardButton(text="📸 Instagram", url=f"https://instagram.com/{INSTAGRAM[1:]}")],
        [InlineKeyboardButton(text="📢 Ikkinchi kanal", url=f"https://t.me/{CHANNEL_2[1:]}")],
        [InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_sub")]
    ])


@router.message(CommandStart())
async def start_handler(message: types.Message):
    text = (
        "🤖 *JavoVerse Botga xush kelibsiz!*\n\n"
        "📌 Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:\n\n"
        "🔹 @xushboqovblog\n"
        "🔹 Instagram: @javohir.ftbl"
    )

    await message.answer(text, reply_markup=check_keyboard(), parse_mode="Markdown")
