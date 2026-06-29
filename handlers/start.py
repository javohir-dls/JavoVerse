from aiogram import Router, F
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

from config import CHANNEL, INSTAGRAM
from handlers.menu import main_menu

router = Router()


async def check_subscription(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ("member", "administrator", "creator")
    except:
        return False


@router.message(F.text == "/start")
async def start_command(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Telegram kanal",
                    url=f"https://t.me/{CHANNEL.replace('@','')}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📸 Instagram",
                    url=f"https://instagram.com/{INSTAGRAM.replace('@','')}"
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

    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "Botdan foydalanish uchun kanalga obuna bo'ling.",
        reply_markup=keyboard
    )


@router.callback_query(F.data == "check_sub")
async def check_sub(callback: CallbackQuery):
    ok = await check_subscription(callback.bot, callback.from_user.id)

    if ok:
        await callback.message.answer(
            "✅ Obuna tasdiqlandi!\n\nJavoVerse botiga xush kelibsiz.",
            reply_markup=main_menu()
        )
    else:
        await callback.answer(
            "❌ Avval kanalga obuna bo'ling!",
            show_alert=True
        )
