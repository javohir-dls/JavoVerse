from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from config import CHANNEL, INSTAGRAM
from handlers.menu import main_menu

router = Router()


async def check_subscription(bot, user_id: int):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False


@router.message(F.text == "/start")
async def start_command(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Telegram kanal",
                    url=f"https://t.me/{CHANNEL.replace('@', '')}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📸 Instagram",
                    url=f"https://instagram.com/{INSTAGRAM.replace('@', '')}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Obunani tekshirish",
                    callback_data="check_sub"
                )
            ]
        ]
    )

    text = (
        "👋 Assalomu alaykum!\n\n"
        "🤖 JavoVerse botiga xush kelibsiz.\n\n"
        "Botdan foydalanish uchun avval kanalga obuna bo'ling."
    )

    await message.answer(text, reply_markup=keyboard)


@router.callback_query(F.data == "check_sub")
async def check_sub(callback: CallbackQuery):
    if await check_subscription(callback.bot, callback.from_user.id):
        await callback.message.answer(
            "✅ Obunangiz tasdiqlandi!\n\n"
            "Quyidagi menyudan kerakli bo'limni tanlang.",
            reply_markup=main_menu()
        )
    else:
        await callback.answer(
            "❌ Avval @xushboqovblog kanaliga obuna bo'ling!",
            show_alert=True
        )
