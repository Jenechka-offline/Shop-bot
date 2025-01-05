from aiogram import types
import asyncio

from middleweres.db import CounterMiddlewere
from config import dp, bot 
from handlers.user_private import user_private_router

dp.include_router(user_private_router)

admin_router.message.middlewere(CounterMiddlewere())

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print('Online')
    await dp.start_polling(bot)
asyncio.run(main())

