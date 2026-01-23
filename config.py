import os

from dotenv import load_dotenv
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


load_dotenv()
ADMINS: list[int] = list(map(lambda x: int(x.strip()), os.getenv("ADMINS", "").split(",")))

dp = Dispatcher(storage=MemoryStorage())

