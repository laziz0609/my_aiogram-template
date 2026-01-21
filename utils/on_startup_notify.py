import logging

from aiogram import Bot



async def on_startup_notify(bot: Bot, ADMINS: list[int]):
    for admin_id in ADMINS:
        try:
            if admin_id:
                await bot.send_message(admin_id, "🤖 Bot ishga tushdi!")
        except Exception as e:
            logging.warning(f"Admin {admin_id} ga xabar yuborilmadi: {e}")