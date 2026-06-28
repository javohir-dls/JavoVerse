from datetime import datetime
from telebot import types
from state import state

def register(bot):

    @bot.message_handler(func=lambda message: message.text == "👶 Yosh kalkulyator")
    def age_start(message):

        state[message.chat.id] = "age"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("⬅️ Orqaga")

        bot.send_message(
            message.chat.id,
            "📅 Tug'ilgan sanangizni kiriting.\n\nMisol: 2010-01-31",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda message: state.get(message.chat.id) == "age")
    def age_calculator(message):

        if message.text == "⬅️ Orqaga":
            state.pop(message.chat.id, None)
            return

        try:
            birth = datetime.strptime(message.text, "%Y-%m-%d")
            today = datetime.now()

            days = (today - birth).days
            years = days // 365

            bot.send_message(
                message.chat.id,
                f"🎉 Siz taxminan {years} yoshdasiz.\n📆 {days} kun yashagansiz."
            )

        except:
            bot.send_message(
                message.chat.id,
                "❌ Sana noto'g'ri.\nMisol: 2010-01-31"
            )

        state.pop(message.chat.id, None)
