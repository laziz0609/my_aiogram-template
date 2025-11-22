from aiogram import  types , Router


roter = Router()

@roter.message()
async def echo(message: types.Message):
    print(message)
    try:
        await message.send_copy(chat_id=message.chat.id)
    except:
        await  message.answer("ERROR")


