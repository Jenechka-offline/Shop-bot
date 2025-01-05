from aiogram.filters import CommandStart
from aiogram import types, Router
from config import dp, bot

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Приветственный текст!')