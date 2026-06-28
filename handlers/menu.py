from telebot import types

def register(bot):

    @bot.callback_query_handler(func=lambda call: call.data == "check_sub")
    def check_subscription(call):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.row("🎵 MP3", "☁️ Ob-havo")
        markup.row("🕌 Namoz", "💱 Valyuta")
        markup.row("🌍 Dunyo soati", "👶 Yosh kalkulyator")

        bot.send_message(
            call.message.chat.id,
            "✅ Asosiy menyu",
            reply_markup=markup
        )
