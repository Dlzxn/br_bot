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


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Привет любителям прекрасной Беларуси!\n'
                         f'Вас приветствует bot v1.0 by Dlzxn'
                         f'Для начала введите /start'
                         )

@router.message(Command(commands="start"))
async def start(message:Message):
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
    s='music/'+str(nu)+"b.mp3"
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
    s='music/'+str(nu)+".mp3"
    await message.answer_audio(audio=FSInputFile(s, 'rb'), protect_content=True,
                              reply_markup=like_menu,
                              caption=f'Проникнись Белорусским шедевром!')
    # await state.update_data(text=message.sticker)
    # user_dict[message.from_user.id] = await state.get_data()
    # await state.clear()
    await state.set_state(state=None)

#закончил раздел фсм--------------------------------------------------------------------------------------



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
                                   f'Статус: закрашена'
                                   f'Владелец: {pict_us(kle)}\n',
                                   reply_markup=raska
                                   )
