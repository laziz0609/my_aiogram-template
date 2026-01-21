from aiogram import  types , Router
import asyncio

router = Router()

@router.message()
async def echo(message: types.Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
        
        
        

