import telebot
from config import TOKEN

from handlers import start
from handlers import menu
from handlers import mp3
from handlers import weather
from handlers import prayer
from handlers import currency
from handlers import time

bot = telebot.TeleBot(TOKEN)

# Handlerlarni ulash
start.register(bot)
menu.register(bot)
mp3.register(bot)
weather.register(bot)
prayer.register(bot)
currency.register(bot)
time.register(bot)

print("✅ JavoVerse ishga tushdi!")

bot.infinity_polling(skip_pending=True)
