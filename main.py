import telebot
from config import TOKEN

# handlers import
from handlers import start, menu, mp3, weather, prayer, currency, time

bot = telebot.TeleBot(TOKEN)

# ================= REGISTER HANDLERS =================
start.register(bot)
menu.register(bot)

# optional modul register (agar kerak bo‘lsa)
mp3.register(bot)
weather.register(bot)
prayer.register(bot)
currency.register(bot)
time.register(bot)

# ================= RUN =================
print("🚀 JavoVerse bot ishga tushdi...")
bot.polling(none_stop=True)
