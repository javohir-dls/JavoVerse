from telebot import types
from config import CHANNEL, INSTAGRAM

def register(bot):

    @bot.message_handler(commands=['start'])
    def start(message):

        markup = types.InlineKeyboardMarkup()

        markup.add(
            types.InlineKeyboardButton("📢 Telegram", url=f"https://t.me/{CHANNEL.replace('@','')}"),
            types.InlineKeyboardButton("📸 Instagram", url=f"https://instagram.com/{INSTAGRAM.replace('@','')}")
        )

        markup.add(types.InlineKeyboardButton("✅ Tekshirish", callback_data="check"))

        bot.send_message(message.chat.id,
            "👋 JavoVerse botga xush kelibsiz!",
            reply_markup=markup
        )
