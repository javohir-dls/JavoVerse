from telebot import types
from state import state

CURRENCIES = [
    "🇺🇸 USD",
    "🇪🇺 EUR",
    "🇷🇺 RUB",
    "🇬🇧 GBP",
    "🇨🇳 CNY",
    "🇯🇵 JPY",
    "🇰🇿 KZT",
    "🇹🇷 TRY",
    "🇰🇷 KRW",
    "🇦🇪 AED"
]

def register(bot):

    @bot.message_handler(func=lambda message: message.text == "💱 Valyuta")
    def currency_menu(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for currency in CURRENCIES:
            markup.add(currency)

        markup.add("⬅️ Orqaga")

        state[message.chat.id] = "currency"

        bot.send_message(
            message.chat.id,
            "💱 Kerakli valyutani tanlang:",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda message: state.get(message.chat.id) == "currency")
    def currency_info(message):

        if message.text == "⬅️ Orqaga":
            state.pop(message.chat.id, None)
            return

        rates = {
            "🇺🇸 USD": "1 USD ≈ 12 800 UZS",
            "🇪🇺 EUR": "1 EUR ≈ 14 900 UZS",
            "🇷🇺 RUB": "1 RUB ≈ 165 UZS",
            "🇬🇧 GBP": "1 GBP ≈ 17 200 UZS",
            "🇨🇳 CNY": "1 CNY ≈ 1 780 UZS",
            "🇯🇵 JPY": "1 JPY ≈ 89 UZS",
            "🇰🇿 KZT": "1 KZT ≈ 25 UZS",
            "🇹🇷 TRY": "1 TRY ≈ 320 UZS",
            "🇰🇷 KRW": "1 KRW ≈ 9 UZS",
            "🇦🇪 AED": "1 AED ≈ 3 485 UZS"
        }

        bot.send_message(
            message.chat.id,
            rates.get(message.text, "❌ Noma'lum valyuta.")
        )

        state.pop(message.chat.id, None)
