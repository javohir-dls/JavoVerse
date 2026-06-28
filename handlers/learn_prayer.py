from aiogram import Router, types

router = Router()

ASMA_UL_HUSNA = [
    "1. Ar-Rahman — Mehribon",
    "2. Ar-Rahim — Rahmli",
    "3. Al-Malik — Podshoh",
    "4. Al-Quddus — Pok",
    "5. As-Salam — Tinchlik beruvchi",
    # ... qolgan 99 ta (xohlasang to‘liq qilib beraman)
]

@router.message(lambda m: "ism" in m.text.lower())
async def names(message: types.Message):
    await message.answer("\n".join(ASMA_UL_HUSNA))
