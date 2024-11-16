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



from func.defs import from_bd, ref_prov, db_table_val, pict, pict_prov, pict_us, new_us_kl
from log_cfg.log_def import start_log, user_new
from keyboard.keyb import kb_menu, like_menu, num_key, raska, num_buy
from us_r.cla import FSMF
storage = MemoryStorage()
router = Router()

user_dict: dict[int, dict[str]] = {}

#БЛОК РАЗДЕЛА РИСОВАННЫЙ ФЛАГ-----------------------------------------------------------------------------
@router.message(F.text=="Раскраска")
async def rask(message:Message):
    s1, s2, s3, s4=pict()
    await message.answer(text=f'Раскрась флаг Белоруси🇧🇾\n'
                         f'{s1}\n'
                         f'{s2}\n'
                         f'{s3}\n'
                         f'{s4}\n',
                         reply_markup=num_key)

#выбор по номеру
@router.message(F.text.in_([str(i) for i in range(1, 21)]))
async def chislo(message: Message):
    if pict_prov(message.text)==True:
        await message.answer_photo(photo=FSInputFile('main_img/user.jpg'),
                                   caption=f'Данная клетка уже приобретена!\n'
                                   f'Владелец: {pict_us(message.text)}\n'
                                   f'Не расстраивайся!\n'
                                   f'Есть еще много красивых клеток!',
                                   reply_markup=raska
                                   )
    else:
        await message.answer_photo(photo=FSInputFile('main_img/us_tr.jpg'),
                                   caption=f'Данная клетка еще не занята!\n'
                                   f'Скорее занимай!',
                                   reply_markup=num_buy
                                   )
        global kle
        kle=message.text

#закрашивание
@router.message(F.text=="Закрасить")
async def zacr_kl(message: Message):
    new_us_kl(kle, message.from_user.id, message.from_user.first_name, message.from_user.username)
    await message.answer(text=f'Поздравляю, вы закрасили клетку {kle}!\n'
                         f'Теперь статус клетки:')
    await message.answer_photo(photo=FSInputFile('main_img/user.jpg'),
                                   caption=f'Данная клетка уже приобретена!\n'
                                   f'Статус: закрашена\n'
                                   f'Владелец: {pict_us(kle)}\n',
                                   reply_markup=raska
                                   )
#картинка блок окончен----------------------------------------------------------------------------