import telebot
from telebot import types

TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

CHANNEL = "@xushboqovblog"
INSTAGRAM = "@javohir.ftbl"


# ---------------- START ----------------
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "📢 Telegram kanal", 
        url="https://t.me/xushboqovblog"
    )

    btn2 = types.InlineKeyboardButton(
        "📸 Instagram (ixtiyoriy)", 
        url="https://instagram.com/javohir.ftbl"
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
        "👋 *JavoVerse botga xush kelibsiz!*\n\n"
        "👉 Avval kanalga obuna bo‘ling va tekshiring.",
        parse_mode="Markdown",
        reply_markup=markup
    )


# ---------------- CHECK ----------------
@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("🎵 MP3 qidirish")
    btn2 = types.KeyboardButton("👶 Yosh kalkulyator")
    btn3 = types.KeyboardButton("🌍 Dunyo soati")
    btn4 = types.KeyboardButton("🕌 Namoz vaqti")
    btn5 = types.KeyboardButton("☁️ Ob-havo")
    btn6 = types.KeyboardButton("💱 Valyuta kursi")

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)

    bot.send_message(
        call.message.chat.id,
        "✅ Tasdiqlandi!\n\n🧭 Menudan birini tanlang:",
        reply_markup=markup
    )


# ---------------- TEXT HANDLER ----------------
@bot.message_handler(content_types=['text'])
def menu_handler(message):
    text = message.text

    if text == "🎵 MP3 qidirish":
        bot.send_message(message.chat.id, "🎧 Qo‘shiq nomini yozing:")

    elif text == "👶 Yosh kalkulyator":
        bot.send_message(message.chat.id, "📅 Tug‘ilgan sanani yozing (YYYY-MM-DD):")

    elif text == "🌍 Dunyo soati":
        bot.send_message(message.chat.id, "🌍 Shahar nomini yozing:")

    elif text == "🕌 Namoz vaqti":
        bot.send_message(message.chat.id, "🕌 Shahar nomini yozing:")

    elif text == "☁️ Ob-havo":
        bot.send_message(message.chat.id, "☁️ Shahar nomini yozing:")

    elif text == "💱 Valyuta kursi":
        bot.send_message(message.chat.id, "💱 Miqdor va valyutani yozing (masalan: 75 USD)")

    else:
        bot.send_message(message.chat.id, "❗ Menudan tanlang yoki to‘g‘ri yozing.")


# ---------------- RUN ----------------
print("JavoVerse bot ishga tushdi...")
bot.polling()
