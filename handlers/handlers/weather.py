import requests

def handle(bot, message):
    bot.send_message(message.chat.id,
        f"☁️ {message.text} ob-havo:\n🌡 +25°C (demo)"
    )
