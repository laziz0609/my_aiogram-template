import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot

from handlers import routers
from utils.on_startup_notify import on_startup_notify
from config import dp, ADMINS
from middleware.time_limit_middleware import Time_Limit

logging.basicConfig(level=logging.INFO)




async def main():
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")   
    BOT = Bot(token=BOT_TOKEN)
    
    

    # ✅ Routerlarni tartib bilan qo‘shamiz
    for router in routers:
        dp.include_router(router)
    
    print("🚀 Bot ishga tushmoqda...")
    await on_startup_notify(BOT, ADMINS)
    await dp.start_polling(BOT)


if __name__ == "__main__":
    asyncio.run(main())
