import telebot
from config import TOKEN
from handlers import start

bot = telebot.TeleBot(TOKEN)

# Start handlerni ulash
start.register(bot)

print("🚀 JavoVerse ishga tushdi!")

bot.infinity_polling(skip_pending=True)
