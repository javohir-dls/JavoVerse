import requests
from aiogram import Router, types

router = Router()

# O'zbekiston viloyatlari (demo coordinates)
regions = {
    "Toshkent": (41.2995, 69.2401),
    "Andijon": (40.7821, 72.3442),
    "Namangan": (40.9983, 71.6726),
    "Farg‘ona": (40.3864, 71.7868),
    "Samarqand": (39.6270, 66.9750),
    "Buxoro": (39.7747, 64.4286),
    "Xorazm": (41.5500, 60.6333),
    "Navoiy": (40.1033, 65.3688),
    "Qashqadaryo": (38.8986, 66.0467),
    "Surxondaryo": (37.9409, 67.5709),
    "Jizzax": (40.1158, 67.8422),
    "Sirdaryo": (40.8436, 68.6617),
    "Qoraqalpog‘iston": (43.8041, 59.4458),
}

@router.message(lambda m: "namoz" in m.text.lower())
async def prayer_menu(message: types.Message):
    text = "🕌 Viloyatni tanlang:\n\n" + "\n".join(regions.keys())
    await message.answer(text)

@router.message()
async def get_prayer_time(message: types.Message):
    city = message.text

    if city in regions:
        lat, lon = regions[city]

        url = f"http://api.aladhan.com/v1/timings?latitude={lat}&longitude={lon}&method=2"

        res = requests.get(url).json()

        if res["code"] != 200:
            await message.answer("❌ Xatolik yuz berdi")
            return

        times = res["data"]["timings"]

        await message.answer(
            f"🕌 {city} namoz vaqti:\n\n"
            f"🌅 Bomdod: {times['Fajr']}\n"
            f"☀️ Peshin: {times['Dhuhr']}\n"
            f"🌤 Asr: {times['Asr']}\n"
            f"🌇 Shom: {times['Maghrib']}\n"
            f"🌙 Xufton: {times['Isha']}"
        )
