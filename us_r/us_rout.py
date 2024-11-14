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



from func.defs import from_bd, ref_prov, db_table_val
from log_cfg.log_def import start_log, user_new

router = Router()

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
                              caption='Беларусь гордилась бы вами!')
    # if (message.text[7:])!="" and (int(decode_payload(message.text[7:])))!=message.from_user.id:
    #     zamena_para(int(decode_payload(message.text[7:])), message.from_user.id)
    #     await message.answer(f'Теперь ВЫ и {from_bd(1, int(decode_payload(message.text[7:])))} пара!')
