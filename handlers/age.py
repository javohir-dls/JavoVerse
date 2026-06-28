from aiogram import Router, types
from datetime import datetime

router = Router()

@router.message(lambda m: "yosh" in m.text.lower())
async def ask_birth(message: types.Message):
    await message.answer("📅 Tug‘ilgan sanani yuboring:\nFormat: YYYY-MM-DD")


@router.message()
async def calc_age(message: types.Message):
    try:
        birth = datetime.strptime(message.text, "%Y-%m-%d")
        now = datetime.now()

        days = (now - birth).days
        months = days // 30
        years = days // 365

        await message.answer(
            f"📊 Natija:\n"
            f"🗓 Yil: {years}\n"
            f"📆 Oy: {months}\n"
            f"📅 Kun: {days}"
        )
    except:
        pass
