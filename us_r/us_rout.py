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



from func.defs import from_bd, ref_prov, db_table_val
from log_cfg.log_def import start_log, user_new
from keyboard.keyb import kb_menu, like_menu
from us_r.cla import FSMF

storage = MemoryStorage()
router = Router()

user_dict: dict[int, dict[str]] = {}



@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Привет любителям прекрасной Беларуси!\n'
                         f'Вас приветствует bot v1.0 by Dlzxn'
                         f'Для начала введите /start'
                         )

    print(message)
@router.message(Command(commands="start"))
async def start(message:Message):
    print("start")
    if ref_prov(message.from_user.id)==False:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
        user_new(us_name, us_id)
    await message.reply_photo(photo=FSInputFile('main_img/menu.jpg'),
                              caption='Беларусь гордилась бы вами!',
                              reply_markup=kb_menu
                              )

#блок фсма-------------------------------------------------------------------------------

nu=0
#запрос музыки
@router.message((F.text=="Беларусская Музыка🎼") | (F.text=='👎'))
async def mus(message: Message, state: FSMContext):
    global nu
    nu=randint(1, 2)
    print(nu)
    s='music/'+str(nu)+"b.mp3"
    print(s)
    # await message.reply_document(document=FSInputFile('music/1.mp3'))
    await message.answer_audio(audio=FSInputFile(s, 'rb'), protect_content=True,
                              reply_markup=like_menu,
                              caption=f'Если понравилась-жми ❤️\n'
                              f'И слушай оригинал!\n'
                              f'Если нет-👎'
                              )
    await state.set_state(FSMF.text)




@router.message(StateFilter(FSMF.text), F.text=='❤️') #StateFilter(FSMF.text), ((F.text =="👎") or (F.text =="❤️"))
async def process_name_sent(message: Message, state: FSMContext, bot: Bot):
    # Cохраняем введенное имя в хранилище по ключу "name"
    print("zashel")
    print(nu)
    s='music/'+str(nu)+".mp3"
    await message.answer_audio(audio=FSInputFile(s, 'rb'), protect_content=True,
                              reply_markup=like_menu,
                              caption=f'Проникнись Белорусским шедевром!')
    # await state.update_data(text=message.sticker)
    # user_dict[message.from_user.id] = await state.get_data()
    # await state.clear()
    await state.set_state(state=None)
