import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers import start, menu, age, currency, weather, time, prayer, learn_prayer

logging.basicConfig(level=logging.INFO)


async def main():
    print("BOT STARTING...")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(age.router)
    dp.include_router(currency.router)
    dp.include_router(weather.router)
    dp.include_router(time.router)
    dp.include_router(prayer.router)
    dp.include_router(learn_prayer.router)

    print("ALL ROUTERS LOADED")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
