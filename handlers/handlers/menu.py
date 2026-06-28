from telebot import types
from utils.subscription import check_sub

def register(bot):

    @bot.callback_query_handler(func=lambda call: call.data == "check")
    def check(call):

        if not check_sub(bot, call.from_user.id, "@xushboqovblog"):
            bot.answer_callback_query(call.id, "❌ Obuna bo‘ling!")
            return

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.row("🎵 MP3","💱 Valyuta")
        markup.row("☁️ Ob-havo","🕌 Namoz")
        markup.row("🌍 Soat")

        bot.send_message(call.message.chat.id, "✅ Menyu:", reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def router(message):

        text = message.text

        if text == "🎵 MP3":
            bot.send_message(message.chat.id, "🎧 Qo‘shiq yozing:")
            return

        if text == "☁️ Ob-havo":
            bot.send_message(message.chat.id, "🌍 Shahar yozing:")
            return

        if text == "🕌 Namoz":
            bot.send_message(message.chat.id, "🕌 Viloyat yozing:")
            return

        if text == "💱 Valyuta":
            bot.send_message(message.chat.id, "💱 USD, EUR, RUB...")
            return

        if text == "🌍 Soat":
            bot.send_message(message.chat.id, "🌍 Shahar yozing:")
            return

        bot.send_message(message.chat.id, "❗ Menyudan tanlang")
