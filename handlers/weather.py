from aiogram import Router, types

router = Router()

regions = {
    "Toshkent": ["Chilonzor", "Yunusobod", "Bektemir"],
    "Andijon": ["Asaka", "Xonobod", "Shahrixon"],
    "Farg‘ona": ["Marg‘ilon", "Qo‘qon", "Farg‘ona"],
}

@router.message(lambda m: "ob-havo" in m.text.lower())
async def weather_menu(message: types.Message):
    text = "🌤 Viloyatni tanlang:\n\n"

    for region in regions:
        text += f"📍 {region}\n"

    await message.answer(text)


@router.message()
async def weather_region(message: types.Message):
    region = message.text

    if region in regions:
        text = f"🌤 {region} tumanlari:\n\n"

        for tuman in regions[region]:
            text += f"• {tuman}\n"

        text += "\nTuman nomini tanlang (demo ob-havo chiqadi)."

        await message.answer(text)

    elif any(region in t for tlist in regions.values() for t in tlist):
        await message.answer(f"🌤 {region} hozir: 28°C, quyoshli ☀️")
