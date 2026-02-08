from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command


from config import dp, ADMINS
from middleware.time_limit_middleware import Time_Limit



class AddMiddleware(StatesGroup):
    check_info = State()
    

router = Router()


@router.message(Command("add_middleware"))
async def add_router(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        
        if user_id not in ADMINS:
            await message.answer("siz admin emassiz")
        
        text = "Quyidagi shablonga kerakli sonlarni kirgizib yuboring !!!\n"
        text += "t: tekshiruv vaqti\n"
        text += "m_s: tekshiruv vaqtidagi  so'rovlar soni\n"
        text += "b: tekshiruv vaqtidagi so'rovlar sonidan oshgan foydalanuvchini bloklash vaqti\n"
        await message.answer(text)
        
        shablon = "t = , m_s = , b = "
        await message.answer(shablon)
        await state.set_state(AddMiddleware.check_info)
        

@router.message(AddMiddleware.check_info)
async def check_shablon(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id not in ADMINS:
            await message.answer("siz admin emassiz")
    
    content = str()  
    for char in message.text:
        if char.isdigit() or char == ",":
            content += char
            
    data = content.split(",")
    data = list(map(int, data))
            
    if len(data) != 3:
        text = "Quyidagi shablonga kerakli sonlarni kirgizib yuboring !!!\n"
        text += "v: tekshiruv vaqti\n"
        text += "t_s: tekshiruv vaqtidagi  so'rovlar soni\n"
        text += "b_v: tekshiruv vaqtidagi so'rovlar sonidan oshgan foydalanuvchini bloklash vaqti\n"
        
        await message.answer("Shablonni to'gri to'ldiring:")
        await message.answer(text)
        
        shablon = "v = , t_s = , b_v = "
        await message.answer(shablon)
        
        return
    
    max_requests = data[1]
    time_window = data[0]
    block_duration = data[2]
    
    text = f"vaqt = {time_window}, so'rovlar soni = {max_requests}, bloklanish vaqti = {block_duration}/n/n/n"
    text+= "middleware sozlamalari shunday belgilandi"
    
    
    dp.callback_query.middleware(Time_Limit(
                                            max_requests=max_requests, 
                                            time_window=time_window,
                                            block_duration=block_duration
                                            )
                                 )
    
    dp.message.middleware(Time_Limit(
                                    max_requests=max_requests, 
                                    time_window=time_window,
                                    block_duration=block_duration
                                    )
                            )
    
    await state.clear()
    await message.answer(text)
    
    
    
        