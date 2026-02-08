from pprint import pprint as print


from aiogram import  types , Router, F, Bot

router = Router()

# @router.message(F.photo)
# async def save_photo(message: types.Message, bot):
#     # Eng yuqori sifatli rasmni olish
#     photo = message.photo[-1]
    
#     # Faylni yuklab olish
#     # file = await bot.get_file(photo.file_id)
#     # await bot.download_file(file.file_path)
    
#     await message.reply("✅ Rasm saqlandi!")
#     await message.answer(photo)
   
        
@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
        
        

