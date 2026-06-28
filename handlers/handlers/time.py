def handle(bot, message):
    bot.send_message(message.chat.id,
        f"🌍 {message.text} vaqti: 12:00 (demo)"
    )
