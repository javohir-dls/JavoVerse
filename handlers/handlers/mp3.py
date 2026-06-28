def handle(bot, message):
    bot.send_message(message.chat.id,
        f"🎵 {message.text} uchun top 10 qo‘shiq:\n1...\n2...\n3..."
    )
