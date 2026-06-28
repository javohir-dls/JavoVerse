import telebot
from telebot import types
from config import TOKEN, CHANNEL, INSTAGRAM

bot = telebot.TeleBot(TOKEN)

# ---------------- START ----------------
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "📢 Telegram kanal",
        url=f"https://t.me/{CHANNEL.replace('@','')}"
    )

    btn2 = types.InlineKeyboardButton(
        "📸 Instagram (ixtiyoriy)",
        url=f"https://instagram.com/{INSTAGRAM.replace('@','')}"
    )

    btn3 = types.InlineKeyboardButton(
        "✅ Tekshirish",
        callback_data="check"
    )

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)

    bot.send_message(
        message.chat.id,
        "👋 JavoVerse botga xush kelibsiz!\n\n"
        "👉 Avval kanalga obuna bo‘ling.",
        reply_markup=markup
    )

# ---------------- CHECK ----------------
@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("🎵 MP3 qidirish", "👶 Yosh kalkulyator")
    markup.row("🌍 Dunyo soati", "🕌 Namoz vaqti")
    markup.row("☁️ Ob-havo", "💱 Valyuta kursi")

    bot.send_message(
        call.message.chat.id,
        "✅ Tasdiqlandi!\n\n🧭 Menudan tanlang:",
        reply_markup=markup
    )

# ---------------- MENU ----------------
@bot.message_handler(content_types=['text'])
def menu(message):
    text = message.text

    if text == "🎵 MP3 qidirish":
        bot.send_message(message.chat.id, "🎧 Qo‘shiq yoki xonanda nomini yozing:")

    elif text == "👶 Yosh kalkulyator":
        bot.send_message(message.chat.id, "📅 Tug‘ilgan sanani yozing (YYYY-MM-DD):")

    elif text == "🌍 Dunyo soati":
        bot.send_message(message.chat.id, "🌍 Shahar nomini yozing:")

    elif text == "🕌 Namoz vaqti":
        bot.send_message(message.chat.id, "🕌 Shahar nomini yozing:")

    elif text == "☁️ Ob-havo":
        bot.send_message(message.chat.id, "☁️ Shahar nomini yozing:")

    elif text == "💱 Valyuta kursi":
        bot.send_message(message.chat.id, "💱 Masalan: 75 USD")

    else:
        bot.send_message(message.chat.id, "❗ Menudan tanlang.")

# ---------------- ERROR HANDLING ----------------
@bot.message_handler(func=lambda message: True)
def fallback(message):
    pass

print("JavoVerse bot ishga tushdi...")

# ---------------- RUN ----------------
bot.polling(none_stop=True, interval=0, timeout=20)
