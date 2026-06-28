from aiogram import Router, types
from datetime import datetime
import pytz

router = Router()

cities = {
    "Tashkent": "Asia/Tashkent",
    "London": "Europe/London",
    "New York": "America/New_York",
    "Tokyo": "Asia/Tokyo",
    "Dubai": "Asia/Dubai",
    "Moscow": "Europe/Moscow",
}

@router.message(lambda m: "soat" in m.text.lower())
async def show_cities(message: types.Message):
    text = "🕒 Shaharlar:\n\n" + "\n".join(cities.keys())
    await message.answer(text)

@router.message()
async def get_time(message: types.Message):
    city = message.text

    if city in cities:
        tz = pytz.timezone(cities[city])
        time = datetime.now(tz).strftime("%H:%M:%S")

        await message.answer(f"🕒 {city} vaqti: {time}")
