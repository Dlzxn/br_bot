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
                           InlineKeyboardMarkup, Message, PhotoSize)
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

from bibleo.bib import sp
from bibleo.sessy import ses, open_sour, base_game, open_panel


router = Router()

server=ses()
@router.message(F.text=="Игра🎮")
async def game(message: Message):
    await message.answer(text=open_panel(base_game),
                         reply_markup=open_sour(base_game))

@router.message(F.text=="Создать игру")
async def create_game(message: Message):
    server=ses()
    server.n_us1=message.from_user.username
    server.us1=message.from_user.id
    base_game.append(server)
    print(len(base_game))
    await message.answer(text="ddd")