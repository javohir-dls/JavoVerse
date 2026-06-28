import telebot
from telebot import types
import requests
from config import TOKEN, CHANNEL, INSTAGRAM

bot = telebot.TeleBot(TOKEN)

# ---------------- STATE ----------------
state = {}
data = {}

# ---------------- REGIONS ----------------
regions = [
    "Toshkent", "Andijon", "Buxoro", "Farg‘ona",
    "Jizzax", "Namangan", "Navoiy", "Qashqadaryo",
    "Samarqand", "Sirdaryo", "Surxondaryo",
    "Xorazm", "Qoraqalpog‘iston"
]

# ---------------- SUB CHECK (GLOBAL LOCK) ----------------
def is_subscribed(user_id):
    try:
        member = bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False


def block_not_subscribed(message):
    if not is_subscribed(message.from_user.id):
        bot.send_message(
            message.chat.id,
            "❌ Botdan foydalanish uchun kanalga obuna bo‘ling!"
        )
        return True
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
        "👋 JavoVerse botga xush kelibsiz!",
        reply_markup=markup
    )

# ---------------- CHECK ----------------
@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):

    if not is_subscribed(call.from_user.id):
        bot.answer_callback_query(call.id, "❌ Avval kanalga obuna bo‘ling!")
        return

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("🎵 MP3 qidirish", "💱 Valyuta kursi")
    markup.row("☁️ Ob-havo", "🌍 Dunyo soati")
    markup.row("🕌 Namoz vaqti", "👶 Yosh kalkulyator")

    bot.send_message(call.message.chat.id,
        "✅ Menyu:",
        reply_markup=markup
    )

# ---------------- MAIN HANDLER ----------------
@bot.message_handler(content_types=['text'])
def handler(message):

    # 🔒 GLOBAL LOCK (ENG MUHIM FIX)
    if block_not_subscribed(message):
        return

    chat_id = message.chat.id
    text = message.text
    st = state.get(chat_id)

    # ---------------- BACKUP RULE ----------------
    if text == "⬅️ Orqaga":
        state[chat_id] = None

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("🎵 MP3 qidirish", "💱 Valyuta kursi")
        markup.row("☁️ Ob-havo", "🌍 Dunyo soati")
        markup.row("🕌 Namoz vaqti", "👶 Yosh kalkulyator")

        bot.send_message(chat_id, "🔙 Menyu:", reply_markup=markup)
        return

    # ---------------- MP3 ----------------
    if st == "mp3":
        bot.send_message(chat_id, f"🎵 Qidirilmoqda: {text}")
        state[chat_id] = None
        return

    # ---------------- WEATHER ----------------
    if st == "weather":
        bot.send_message(chat_id, f"☁️ Ob-havo: {text} (real API keyin ulanadi)")
        state[chat_id] = None
        return

    # ---------------- TIME ----------------
    if st == "time":
        bot.send_message(chat_id, f"🌍 Dunyo vaqti: {text} (real API keyin)")
        state[chat_id] = None
        return

    # ---------------- PRAYER ----------------
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
                f"🕌 {text}\n\n"
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

    # ---------------- CURRENCY STEP 1 ----------------
    if st == "currency_select":
        data[chat_id] = text.upper()
        state[chat_id] = "currency_amount"
        bot.send_message(chat_id, "💰 Miqdorni yozing:")
        return

    # ---------------- CURRENCY STEP 2 ----------------
    if st == "currency_amount":
        rates = {
            "USD": 12500, "EUR": 13500, "RUB": 130,
            "GBP": 15500, "TRY": 400, "KZT": 25,
            "KRW": 9, "JPY": 85, "CNY": 1750, "AED": 3400
        }

        try:
            amount = float(text)
            cur = data.get(chat_id)

            result = amount * rates.get(cur, 1)

            bot.send_message(chat_id,
                f"💱 {amount} {cur} = {result} UZS"
            )
        except:
            bot.send_message(chat_id, "❗ Faqat raqam kiriting!")

        state[chat_id] = None
        return

    # ---------------- BUTTONS ----------------
    if text == "🎵 MP3 qidirish":
        state[chat_id] = "mp3"
        bot.send_message(chat_id, "🎧 Qo‘shiq yoki xonanda yozing:")
        return

    if text == "☁️ Ob-havo":
        state[chat_id] = "weather"
        bot.send_message(chat_id, "☁️ Shahar nomini yozing:")
        return

    if text == "🌍 Dunyo soati":
        state[chat_id] = "time"
        bot.send_message(chat_id, "🌍 Shahar nomini yozing:")
        return

    if text == "🕌 Namoz vaqti":
        state[chat_id] = "prayer"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for r in regions:
            markup.add(r)

        bot.send_message(chat_id, "🕌 Viloyatni tanlang:", reply_markup=markup)
        return

    if text == "💱 Valyuta kursi":
        state[chat_id] = "currency_select"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("USD", "EUR", "RUB", "GBP", "TRY")
        markup.row("KZT", "KRW", "JPY", "CNY", "AED")

        bot.send_message(chat_id, "💱 Valyuta tanlang:", reply_markup=markup)
        return

    bot.send_message(chat_id, "❗ Menudan tanlang.")

# ---------------- RUN ----------------
print("🚀 JavoVerse FINAL CLEAN ishlayapti...")
bot.polling(none_stop=True, interval=0, timeout=20)
