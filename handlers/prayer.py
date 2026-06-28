from aiogram import Router, types

router = Router()

regions = [
    "Toshkent", "Andijon", "Namangan", "Farg‘ona",
    "Samarqand", "Buxoro", "Xorazm", "Navoiy",
    "Qashqadaryo", "Surxondaryo", "Jizzax", "Sirdaryo",
    "Qoraqalpog‘iston"
]

@router.message(lambda m: "namoz" in m.text.lower())
async def prayer_regions(message: types.Message):
    await message.answer("🕌 Viloyatni tanlang:\n\n" + "\n".join(regions))


@router.message()
async def prayer_time(message: types.Message):
    # hozir demo (keyin API qo‘shamiz)
    if message.text in regions:
        await message.answer(
            f"🕌 {message.text} uchun namoz vaqti:\n"
            f"Bomdod: 05:10\nPeshin: 12:30\nAsr: 16:45\nShom: 18:10\nXufton: 19:40"
        )
