import os

from aiogram import Bot
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS: list[int] = list(map(lambda x: int(x.strip()), os.getenv("ADMINS", "").split(",")))
BOT = Bot(token=BOT_TOKEN)

