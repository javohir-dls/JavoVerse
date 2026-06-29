import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN

from handlers import (
    start,
    menu,
    currency,
    time,
    prayer,
    learn_prayer,
    weather,
    age,
)

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(currency.router)
    dp.include_router(time.router)
    dp.include_router(prayer.router)
    dp.include_router(learn_prayer.router)
    dp.include_router(weather.router)
    dp.include_router(age.router)

    print("✅ JavoVerse ishga tushdi!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
