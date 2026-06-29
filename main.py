import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN

from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.currency import router as currency_router
from handlers.time import router as time_router
from handlers.prayer import router as prayer_router
from handlers.learn_prayer import router as learn_prayer_router
from handlers.weather import router as weather_router
from handlers.age import router as age_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(currency_router)
    dp.include_router(time_router)
    dp.include_router(prayer_router)
    dp.include_router(learn_prayer_router)
    dp.include_router(weather_router)
    dp.include_router(age_router)

    print("✅ JavoVerse Bot ishga tushdi!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
