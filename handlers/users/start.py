from aiogram import Router, types
from aiogram.filters import Command
from keyboards.default.reply_menu import menu_kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Salom! Bu aiogram 3.22 shablon boti.", reply_markup=menu_kb)
