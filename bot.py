import asyncio
import logging

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import routers
from config import BOT_TOKEN
from utils.on_startup_notify import on_startup_notify
from config import BOT, ADMINS

logging.basicConfig(level=logging.INFO)




async def main():
    dp = Dispatcher(storage=MemoryStorage())

    # ✅ Routerlarni tartib bilan qo‘shamiz
    for router in routers:
        dp.include_router(router)

    print("🚀 Bot ishga tushmoqda...")
    await on_startup_notify(BOT, ADMINS)
    await dp.start_polling(BOT)


if __name__ == "__main__":
    asyncio.run(main())
