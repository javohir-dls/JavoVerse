from aiogram import Router, types

router = Router()

# 50 ta shahar (demo ro‘yxat)
cities = {
    "Tashkent": "+05:00",
    "Moscow": "+03:00",
    "London": "+00:00",
    "Dubai": "+04:00",
    "New York": "-05:00",
    "Tokyo": "+09:00",
    "Seoul": "+09:00",
    "Beijing": "+08:00",
    "Paris": "+01:00",
    "Berlin": "+01:00",
}

@router.message(lambda m: "soat" in m.text.lower())
async def world_time_menu(message: types.Message):
    text = "🕒 Dunyo soati:\n\n"

    for city in cities:
        text += f"🌍 {city}\n"

    text += "\nShahar nomini yuboring."
    await message.answer(text)


@router.message()
async def show_time(message: types.Message):
    city = message.text

    if city in cities:
        await message.answer(f"🕒 {city} vaqti: {cities[city]}")
