import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from handlers import routers

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS", "").split(",")

logging.basicConfig(level=logging.INFO)


async def on_startup_notify(bot: Bot):
    for admin_id in ADMINS:
        try:
            if admin_id.strip():
                await bot.send_message(int(admin_id), "🤖 Bot ishga tushdi!")
        except Exception as e:
            logging.warning(f"Admin {admin_id} ga xabar yuborilmadi: {e}")


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # ✅ Routerlarni tartib bilan qo‘shamiz
    for router in routers:
        dp.include_router(router)

    print("🚀 Bot ishga tushmoqda...")
    await on_startup_notify(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
