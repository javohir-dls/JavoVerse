from telebot import types
from state import state

CITIES = [
    "Toshkent", "Samarqand", "Buxoro", "Xiva", "Nukus",
    "Moskva", "London", "Parij", "Berlin", "Rim",
    "Madrid", "Istanbul", "Dubay", "Doha", "Riyod",
    "Tehron", "Dehli", "Pekin", "Tokio", "Seul",
    "Bangkok", "Singapur", "Kuala-Lumpur", "Jakarta",
    "Sidney", "Melburn", "Vellington", "Nyu-York",
    "Vashington", "Los-Anjeles", "Toronto", "Meksika",
    "San-Paulu", "Buenos-Ayres", "Qohira", "Keyptaun",
    "Nayrobi", "Afina", "Vena", "Bryussel",
    "Amsterdam", "Praga", "Budapesht", "Varshava",
    "Kiyev", "Boku", "Olmaota", "Bishkek",
    "Dushanbe", "Ashxobod"
]

def register(bot):

    @bot.message_handler(func=lambda message: message.text == "🌍 Dunyo soati")
    def world_time(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for city in CITIES:
            markup.add(city)

        markup.add("⬅️ Orqaga")

        state[message.chat.id] = "time"

        bot.send_message(
            message.chat.id,
            "🌍 Kerakli shaharni tanlang:",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda message: state.get(message.chat.id) == "time")
    def city_time(message):

        if message.text == "⬅️ Orqaga":
            state.pop(message.chat.id, None)
            return

        bot.send_message(
            message.chat.id,
            f"🕒 {message.text} vaqti (API keyin ulanadi)."
        )

        state.pop(message.chat.id, None)
