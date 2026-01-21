from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"salom <b>{message.from_user.first_name}</b>", parse_mode="html")
