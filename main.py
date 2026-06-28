import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

# HANDLERS IMPORT
from handlers import start
from handlers import menu
from handlers import age
from handlers import currency
from handlers import weather
from handlers import time
from handlers import prayer
from handlers import learn_prayer


# logging
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # ROUTERS ULASH
    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(age.router)
    dp.include_router(currency.router)
    dp.include_router(weather.router)
    dp.include_router(time.router)
    dp.include_router(prayer.router)
    dp.include_router(learn_prayer.router)

    print("🤖 JavoVerse Bot ishga tushdi!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
