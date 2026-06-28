from aiogram import Router, types

router = Router()

ASMA = [
    "1. Ar-Rahman — Mehribon",
    "2. Ar-Rahim — Rahmli",
    "3. Al-Malik — Podshoh",
    "4. Al-Quddus — Pok",
    "5. As-Salam — Tinchlik",
    "6. Al-Mu'min — Iymon beruvchi",
    "7. Al-Muhaymin — Himoya qiluvchi",
    "8. Al-Aziz — Kuchli",
    "9. Al-Jabbar — Majbur qiluvchi",
    "10. Al-Mutakabbir — Ulug‘",
    # 👉 qolgan 99 tagacha davom ettiramiz
]

@router.message(lambda m: "ism" in m.text.lower())
async def names(message: types.Message):
    text = "📿 Allohning 99 go‘zal ismi:\n\n"
    text += "\n".join(ASMA)

    await message.answer(text)
