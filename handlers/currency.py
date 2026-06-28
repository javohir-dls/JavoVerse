import requests
from aiogram import Router, types

router = Router()

@router.message(lambda m: "valyuta" in m.text.lower())
async def currency_help(message: types.Message):
    await message.answer("💱 Format: USD UZS 10")

@router.message()
async def convert(message: types.Message):
    try:
        from_cur, to_cur, amount = message.text.split()
        amount = float(amount)

        url = f"https://api.exchangerate.host/convert?from={from_cur}&to={to_cur}&amount={amount}"
        res = requests.get(url).json()

        result = res["result"]

        await message.answer(f"💰 Natija: {result} {to_cur}")

    except:
        await message.answer("❌ Format xato: USD UZS 10")
