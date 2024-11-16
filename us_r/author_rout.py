from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandStart, StateFilter, CommandObject
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize, ReplyKeyboardRemove)
from dotenv import load_dotenv
import os
import sqlite3
from aiogram.types import FSInputFile
from aiogram.utils.deep_linking import create_start_link, decode_payload
from aiogram import types
import base64
import logging.config
import logging
from random import randint
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage





from keyboard.keyb import kb_menu, like_menu, num_key, raska, num_buy
from inline.keyb import keyboard_author


router = Router()

@router.message(F.text=="Авторы🎬")
async def author(message: Message):
    print("ddd")
    await message.answer(text=f'Внимание, перед вашими глазами...')
    await message.answer_photo(photo=FSInputFile('author_img/menu.jpg'),
                        caption=f'Вот они...\n'
                        f'...Гениальные, Крутые, Умные...\n\n'
                        f'БелорусоЛюбители слева на право!\n\n'
                        f'Разработчик кода: DlzxnDev\n'
                        f'version: 3.0',
                        reply_markup=keyboard_author
                        )
