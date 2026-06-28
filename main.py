import telebot
from telebot import types
from config import TOKEN, CHANNEL, INSTAGRAM

bot = telebot.TeleBot(TOKEN)

# ---------------- STATE ----------------
user_state = {}
user_data = {}

# ---------------- START ----------------
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    markup.add(
        types.InlineKeyboardButton("📢 Telegram", url=f"https://t.me/{CHANNEL.replace('@','')}"),
        types.InlineKeyboardButton("📸 Instagram", url=f"https://instagram.com/{INSTAGRAM.replace('@','')}")
    )

    markup.add(
        types.InlineKeyboardButton("✅ Tekshirish", callback_data="check")
    )

    bot.send_message(message.chat.id,
        "👋 JavoVerse botga xush kelibsiz!",
        reply_markup=markup
    )

# ---------------- CHECK ----------------
@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("🎵 MP3 qidirish", "💱 Valyuta kursi")
    markup.row("☁️ Ob-havo", "🌍 Dunyo soati")
    markup.row("🕌 Namoz vaqti", "👶 Yosh kalkulyator")

    bot.send_message(call.message.chat.id,
        "✅ Menyuni tanlang:",
        reply_markup=markup
    )

# ---------------- MENU ----------------
@bot.message_handler(content_types=['text'])
def handler(message):
    chat_id = message.chat.id
    text = message.text
    state = user_state.get(chat_id)

    # ---------------- MP3 ----------------
    if state == "mp3":
        bot.send_message(chat_id, f"🎵 Qidirilmoqda: {text}\n🎧 Top 10 qo‘shiq (demo)")
        user_state[chat_id] = None
        return

    # ---------------- WEATHER ----------------
    if state == "weather":
        bot.send_message(chat_id, f"☁️ Ob-havo: {text} uchun olinmoqda...")
        user_state[chat_id] = None
        return

    # ---------------- CURRENCY STEP 1 ----------------
    if state == "currency_select":
        user_data[chat_id] = text
        user_state[chat_id] = "currency_amount"
        bot.send_message(chat_id, f"💱 {text} tanlandi\nEndi miqdorni yozing (masalan 10):")
        return

    # ---------------- CURRENCY STEP 2 ----------------
    if state == "currency_amount":
        cur = user_data.get(chat_id)
        amount = float(text)

        rates = {
            "USD": 12500,
            "RUB": 130,
            "EUR": 13500,
            "GBP": 15500,
            "TRY": 400,
            "KZT": 25,
            "KRW": 9,
            "JPY": 85,
            "CNY": 1750,
            "AED": 3400
        }

        result = amount * rates.get(cur, 1)

        bot.send_message(chat_id,
            f"💱 {amount} {cur} ≈ {result} UZS"
        )

        user_state[chat_id] = None
        return

    # ---------------- BUTTONS ----------------
    if text == "🎵 MP3 qidirish":
        user_state[chat_id] = "mp3"
        bot.send_message(chat_id, "🎧 Xonanda yoki qo‘shiq nomini yozing:")
        return

    if text == "☁️ Ob-havo":
        user_state[chat_id] = "weather"
        bot.send_message(chat_id, "☁️ Shahar nomini yozing:")
        return

    if text == "💱 Valyuta kursi":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.row("USD", "EUR", "RUB", "GBP", "TRY")
        markup.row("KZT", "KRW", "JPY", "CNY", "AED")

        user_state[chat_id] = "currency_select"

        bot.send_message(chat_id,
            "💱 10 ta valyutadan birini tanlang:",
            reply_markup=markup
        )
        return

    bot.send_message(chat_id, "❗ Menudan tanlang.")

# ---------------- RUN ----------------
print("🚀 JavoVerse ishlayapti...")
bot.polling(none_stop=True, interval=0, timeout=20)
