import requests
from aiogram import Router, types

router = Router()

API_KEY = "YOUR_OPENWEATHER_API_KEY"

@router.message(lambda m: "ob-havo" in m.text.lower())
async def weather_start(message: types.Message):
    await message.answer("🌤 Shahar nomini yuboring (masalan: Tashkent)")

@router.message()
async def get_weather(message: types.Message):
    city = message.text

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        await message.answer("❌ Shahar topilmadi")
        return

    temp = data["main"]["temp"]
    feel = data["main"]["feels_like"]
    desc = data["weather"][0]["description"]

    await message.answer(
        f"🌤 {city}\n"
        f"🌡 Harorat: {temp}°C\n"
        f"🤔 His qilinadi: {feel}°C\n"
        f"☁️ Holat: {desc}"
    )
