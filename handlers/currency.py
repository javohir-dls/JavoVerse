from aiogram import Router, types

router = Router()

rates = {
    "USD": 12500,
    "EUR": 13500,
    "RUB": 135,
    "GBP": 16000,
    "TRY": 400,
    "KZT": 25,
    "CNY": 1700,
    "KRW": 9,
    "JPY": 85,
    "AED": 3400
}

@router.message(lambda m: "valyuta" in m.text.lower())
async def currency_menu(message: types.Message):
    text = "💱 Format:\nUSD 10\nEUR 5\nva hokazo"
    await message.answer(text)


@router.message()
async def convert(message: types.Message):
    try:
        cur, amount = message.text.split()
        amount = float(amount)

        if cur.upper() in rates:
            result = amount * rates[cur.upper()]
            await message.answer(f"💰 {amount} {cur.upper()} = {result} UZS")
    except:
        pass
