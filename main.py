import telebot
from telebot import types
import requests
from config import TOKEN, CHANNEL, INSTAGRAM

bot = telebot.TeleBot(TOKEN)

# ---------------- STATE ----------------
user_state = {}
user_data = {}

# ---------------- UZBEK REGIONS ----------------
regions = [
    "Toshkent", "Andijon", "Buxoro", "Farg‘ona",
    "Jizzax", "Namangan", "Navoiy", "Qashqadaryo",
    "Samarqand", "Sirdaryo", "Surxondaryo",
    "Xorazm", "Qoraqalpog‘iston"
]

# ---------------- CHECK SUB ----------------
def is_member(user_id):
    try:
        member = bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

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
        "👋 JavoVerse botga xush kelibsiz!\n\nAvval kanalga obuna bo‘ling.",
        reply_markup=markup
    )

# ---------------- CHECK ----------------
@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):

    if not is_member(call.from_user.id):
        bot.answer_callback_query(call.id, "❌ Avval kanalga obuna bo‘ling!")
        return

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("🎵 MP3 qidirish", "💱 Valyuta kursi")
    markup.row("☁️ Ob-havo", "🌍 Dunyo soati")
    markup.row("🕌 Namoz vaqti", "👶 Yosh kalkulyator")

    bot.send_message(call.message.chat.id,
        "✅ Tasdiqlandi!\n📌 Menyuni tanlang:",
        reply_markup=markup
    )

# ---------------- HANDLER ----------------
@bot.message_handler(content_types=['text'])
def handler(message):
    chat_id = message.chat.id
    text = message.text
    state = user_state.get(chat_id)

    # ---------------- MP3 ----------------
    if state == "mp3":
        bot.send_message(chat_id, f"🎵 Qidirilmoqda: {text}")
        user_state[chat_id] = None
        return

    # ---------------- WEATHER ----------------
    if state == "weather":
        bot.send_message(chat_id, f"☁️ Ob-havo: {text}")
        user_state[chat_id] = None
        return

    # ---------------- TIME ----------------
    if state == "time":
        bot.send_message(chat_id, f"🌍 Vaqt: {text}")
        user_state[chat_id] = None
        return

    # ---------------- PRAYER REGION ----------------
    if state == "prayer":
        city = text

        try:
            res = requests.get(
                "https://api.aladhan.com/v1/timingsByCity",
                params={
                    "city": city,
                    "country": "Uzbekistan",
                    "method": 2
                }
            )
            data = res.json()["data"]["timings"]

            msg = (
                f"🕌 Namoz vaqtlari ({city})\n\n"
                f"🌅 Bomdod: {data['Fajr']}\n"
                f"🌄 Quyosh: {data['Sunrise']}\n"
                f"🏙 Peshin: {data['Dhuhr']}\n"
                f"🌇 Asr: {data['Asr']}\n"
                f"🌆 Shom: {data['Maghrib']}\n"
                f"🌙 Xufton: {data['Isha']}"
            )

        except:
            msg = "❌ Namoz vaqti topilmadi!"

        bot.send_message(chat_id, msg)
        user_state[chat_id] = None
        return

    # ---------------- CURRENCY STEP 1 ----------------
    if state == "currency_select":
        user_data[chat_id] = text
        user_state[chat_id] = "currency_amount"
        bot.send_message(chat_id, f"💱 {text} tanlandi\nMiqdorni yozing:")
        return

    # ---------------- CURRENCY STEP 2 ----------------
    if state == "currency_amount":
        cur = user_data.get(chat_id)

        try:
            amount = float(text)
        except:
            bot.send_message(chat_id, "❗ Raqam kiriting!")
            return

        rates = {
            "USD": 12500,
            "EUR": 13500,
            "RUB": 130,
            "GBP": 15500,
            "TRY": 400,
            "KZT": 25,
            "KRW": 9,
            "JPY": 85,
            "CNY": 1750,
            "AED": 3400
        }

        result = amount * rates.get(cur, 1)

        bot.send_message(chat_id, f"💱 {amount} {cur} ≈ {result} UZS")

        user_state[chat_id] = None
        return

    # ---------------- BUTTONS ----------------
    if text == "🎵 MP3 qidirish":
        user_state[chat_id] = "mp3"
        bot.send_message(chat_id, "🎧 Qo‘shiq yoki xonanda nomini yozing:")
        return

    if text == "☁️ Ob-havo":
        user_state[chat_id] = "weather"
        bot.send_message(chat_id, "☁️ Shahar nomini yozing:")
        return

    if text == "🌍 Dunyo soati":
        user_state[chat_id] = "time"
        bot.send_message(chat_id, "🌍 Shahar nomini yozing:")
        return

    if text == "🕌 Namoz vaqti":
        user_state[chat_id] = "prayer"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for r in regions:
            markup.add(r)

        bot.send_message(chat_id, "🕌 Viloyatni tanlang:", reply_markup=markup)
        return

    if text == "💱 Valyuta kursi":
        user_state[chat_id] = "currency_select"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("USD", "EUR", "RUB", "GBP", "TRY")
        markup.row("KZT", "KRW", "JPY", "CNY", "AED")

        bot.send_message(chat_id, "💱 Valyuta tanlang:", reply_markup=markup)
        return

    bot.send_message(chat_id, "❗ Menudan tanlang.")

# ---------------- RUN ----------------
print("🚀 JavoVerse ULTIMATE ishlayapti...")
bot.polling(none_stop=True, interval=0, timeout=20)
