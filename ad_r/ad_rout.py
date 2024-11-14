from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F


router = Router()


@router.message((F.text=="/adm") & (F.from_user.id==1007130027))
async def adm_list(message: Message):
    await message.answer(f'Вы-админ')