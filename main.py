import telebot
from telebot import types
import requests
from config import TOKEN, CHANNEL, INSTAGRAM

bot = telebot.TeleBot(TOKEN)

# ================= STATE =================
state = {}
data = {}

# ================= DATA =================
regions = {
    "Toshkent": ["Chilonzor", "Yunusobod", "Bektemir"],
    "Andijon": ["Andijon shahar", "Asaka", "Xonobod"],
    "Buxoro": ["Buxoro shahar", "G‘ijduvon", "Kogon"],
    "Farg‘ona": ["Farg‘ona shahar", "Qo‘qon", "Marg‘ilon"],
    "Namangan": ["Namangan shahar", "Chust", "Pop"],
    "Samarqand": ["Samarqand shahar", "Urgut", "Kattaqo‘rg‘on"],
    "Qashqadaryo": ["Qarshi", "Shahrisabz", "Kitob"],
    "Surxondaryo": ["Termiz", "Denov", "Sherobod"],
    "Jizzax": ["Jizzax shahar", "Zomin", "G‘allaorol"],
    "Sirdaryo": ["Guliston", "Yangiyer", "Shirin"],
    "Navoiy": ["Navoiy shahar", "Zarafshon", "Uchquduq"],
    "Xorazm": ["Urganch", "Xiva", "Shovot"],
    "Qoraqalpog‘iston": ["Nukus", "Chimboy", "Taxiatosh"]
}

# ================= SUB CHECK =================
def is_sub(user_id):
    try:
        m = bot.get_chat_member(CHANNEL, user_id)
        return m.status in ["member", "administrator", "creator"]
    except:
        return False

def block(message):
    if not is_sub(message.from_user.id):
        bot.send_message(message.chat.id, "❌ Avval kanalga obuna bo‘ling!")
        return True
    return False

# ================= START =================
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

# ================= CHECK =================
@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):

    if not is_sub(call.from_user.id):
        bot.answer_callback_query(call.id, "❌ Obuna bo‘ling!")
        return

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("🎵 MP3", "💱 Valyuta")
    markup.row("☁️ Ob-havo", "🌍 Soat")
    markup.row("🕌 Namoz", "👶 Yosh")
    markup.row("⬅️ Orqaga")

    bot.send_message(call.message.chat.id,
        "✅ Menyu:",
        reply_markup=markup
    )

# ================= MAIN HANDLER =================
@bot.message_handler(content_types=['text'])
def handler(message):

    if block(message):
        return

    chat_id = message.chat.id
    text = message.text
    st = state.get(chat_id)

    # ---------------- BACK ----------------
    if text == "⬅️ Orqaga":
        state[chat_id] = None

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("🎵 MP3", "💱 Valyuta")
        markup.row("☁️ Ob-havo", "🌍 Soat")
        markup.row("🕌 Namoz", "👶 Yosh")

        bot.send_message(chat_id, "🔙 Menyu:", reply_markup=markup)
        return

    # ================= MP3 (FIXED) =================
    if text == "🎵 MP3":
        state[chat_id] = "mp3"
        bot.send_message(chat_id, "🎧 Qo‘shiq yoki xonanda yozing:")
        return

    if st == "mp3":
        bot.send_message(chat_id, f"🎵 Qidirilmoqda: {text}")

        bot.send_message(chat_id,
            f"🎧 Natija:\n"
            f"1. {text} - Official\n"
            f"2. {text} - Remix\n"
            f"3. {text} - Live"
        )

        state[chat_id] = None
        return

    # ================= WEATHER =================
    if text == "☁️ Ob-havo":
        state[chat_id] = "weather_region"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for r in regions.keys():
            markup.add(r)

        bot.send_message(chat_id, "🌍 Viloyat tanlang:", reply_markup=markup)
        return

    if st == "weather_region":
        data[chat_id] = text
        state[chat_id] = "weather_district"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for d in regions.get(text, []):
            markup.add(d)

        bot.send_message(chat_id, "🏙 Tuman tanlang:", reply_markup=markup)
        return

    if st == "weather_district":
        district = text

        try:
            r = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={
                    "q": district,
                    "appid": "YOUR_API_KEY",
                    "units": "metric",
                    "lang": "uz"
                }
            )

            w = r.json()

            bot.send_message(chat_id,
                f"☁️ {district}\n\n"
                f"🌡 {w['main']['temp']}°C\n"
                f"💧 {w['main']['humidity']}%\n"
                f"🌬 {w['wind']['speed']} m/s\n"
                f"⛅ {w['weather'][0]['description']}"
            )

        except:
            bot.send_message(chat_id, "❌ Xatolik!")

        state[chat_id] = None
        return

    # ================= PRAYER =================
    if text == "🕌 Namoz":
        state[chat_id] = "prayer"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for r in regions.keys():
            markup.add(r)

        bot.send_message(chat_id, "🕌 Viloyatni tanlang:", reply_markup=markup)
        return

    if st == "prayer":
        try:
            r = requests.get(
                "https://api.aladhan.com/v1/timingsByCity",
                params={
                    "city": text,
                    "country": "Uzbekistan",
                    "method": 2
                }
            )
            d = r.json()["data"]["timings"]

            bot.send_message(chat_id,
                f"🕌 {text}\n"
                f"🌅 Bomdod: {d['Fajr']}\n"
                f"🏙 Peshin: {d['Dhuhr']}\n"
                f"🌇 Asr: {d['Asr']}\n"
                f"🌆 Shom: {d['Maghrib']}\n"
                f"🌙 Xufton: {d['Isha']}"
            )
        except:
            bot.send_message(chat_id, "❌ Xatolik!")

        state[chat_id] = None
        return

    # ================= CURRENCY =================
    if text == "💱 Valyuta":
        state[chat_id] = "currency"

        bot.send_message(chat_id,
            "💱 USD, EUR, RUB, GBP, TRY, KZT, KRW, JPY, CNY, AED yozing:"
        )
        return

    if st == "currency":
        rates = {
            "USD": 12500, "EUR": 13500, "RUB": 130,
            "GBP": 15500, "TRY": 400, "KZT": 25,
            "KRW": 9, "JPY": 85, "CNY": 1750, "AED": 3400
        }

        data[chat_id] = text.upper()
        state[chat_id] = "currency_amount"
        bot.send_message(chat_id, "💰 Miqdorni yozing:")
        return

    if st == "currency_amount":
        try:
            amount = float(text)
            cur = data.get(chat_id)
            result = amount * rates.get(cur, 1)

            bot.send_message(chat_id, f"💱 {amount} {cur} = {result} UZS")
        except:
            bot.send_message(chat_id, "❗ Raqam kiriting!")

        state[chat_id] = None
        return

    # ================= DEFAULT =================
    bot.send_message(chat_id, "❗ Menyudan tanlang.")

print("🚀 JavoVerse FINAL RUNNING...")
bot.polling(none_stop=True)
