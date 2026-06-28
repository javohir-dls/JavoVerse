from telebot import types
from config import CHANNEL, INSTAGRAM

def register(bot):

    @bot.message_handler(commands=['start'])
    def start(message):

        keyboard = types.InlineKeyboardMarkup()

        keyboard.add(
            types.InlineKeyboardButton(
                "📢 Telegram kanal",
                url=f"https://t.me/{CHANNEL.replace('@','')}"
            )
        )

        keyboard.add(
            types.InlineKeyboardButton(
                "📸 Instagram",
                url=f"https://instagram.com/{INSTAGRAM.replace('@','')}"
            )
        )

        keyboard.add(
            types.InlineKeyboardButton(
                "✅ Tekshirish",
                callback_data="check_sub"
            )
        )

        bot.send_message(
            message.chat.id,
            "👋 JavoVerse botiga xush kelibsiz!\n\nBotdan foydalanish uchun kanalga obuna bo'ling.",
            reply_markup=keyboard
        )
