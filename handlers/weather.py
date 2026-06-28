from telebot import types
from state import state

REGIONS = [
    "Toshkent", "Andijon", "Buxoro", "Farg'ona",
    "Jizzax", "Xorazm", "Namangan", "Navoiy",
    "Qashqadaryo", "Qoraqalpog'iston",
    "Samarqand", "Sirdaryo", "Surxondaryo"
]

def register(bot):

    @bot.message_handler(func=lambda message: message.text == "☁️ Ob-havo")
    def weather_menu(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for region in REGIONS:
            markup.add(region)

        markup.add("⬅️ Orqaga")

        state[message.chat.id] = "weather"

        bot.send_message(
            message.chat.id,
            "🌤 Viloyatni tanlang:",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda message: state.get(message.chat.id) == "weather")
    def weather_region(message):

        if message.text == "⬅️ Orqaga":
            state.pop(message.chat.id, None)
            return

        bot.send_message(
            message.chat.id,
            f"🌤 {message.text} ob-havosi (API keyin ulanadi)."
        )

        state.pop(message.chat.id, None)
