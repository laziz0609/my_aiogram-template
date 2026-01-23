import datetime

from aiogram import BaseMiddleware
from aiogram.types import  CallbackQuery
from typing import Callable, Dict, Any, Awaitable


USERS: dict[int, dict[str, list[int] | datetime.datetime]] = {}



class Time_Limit(BaseMiddleware):
    def __init__(self, max_requests: int = 20, time_window: int = 30, block_duration: int = 3600):

        super().__init__()
        self.max_requests = max_requests
        self.time_window = time_window
        self.block_duration = block_duration
    
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any]
    ) -> Any:
        
        user_id = event.from_user.id
        
        # user yo'q bo'lsa USERS dict ga qo'shamiz
        if user_id not in USERS:
            USERS[user_id] = {"block_time": None, "requests":[]}
        
        user = USERS[user_id]   
        
        # user bloklangan yoki yo'qligini tekshiramiz 
        now = datetime.datetime.now()
        if user["block_time"] and user["block_time"] > now:
            await event.answer(f'siz bloklangansiz {user["block_time"]} da ochilasiz')
            return
        
        # user blokdan ochilgan yoki yo'qligini tekshiramiz
        elif user["block_time"] and user["block_time"] <= now:
            user["block_time"] = None
        
        # so'rovni qo'shamiz va eski so'rovlarni olib tashlaymiz 
        user["requests"].append(now)
        user["requests"] = list(filter(lambda time: (time + datetime.timedelta(seconds=self.time_window)) > now, user["requests"]))
        
        # so'rovlar limitdan o'tsa userni bloklaymiz
        if len(user["requests"]) >= self.max_requests:
            user["block_time"] = now + datetime.timedelta(seconds=self.block_duration)
            await event.answer(f'siz bloklandingiz {user["block_time"]} da ochilasiz')
            return    
        
        # so'rov callbackquery bo'lsa loadingni o'chirish
        if isinstance(event, CallbackQuery):
            await event.answer()
            
        return await handler(event, data)
        
