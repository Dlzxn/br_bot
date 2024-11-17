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
from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup

from bibleo.bib import sp
from random import randint
from bibleo.sessy import ses, open_sour, base_game, open_panel, prov_igr, my_game, clava_del, clava_st_game, num_u, bucv_otg, prot, bal
from func.defs import top_up, top_up5
import time
import asyncio

router = Router()

server=ses()

us_in_game=[]
@router.message(F.text=="Игра🎮")
async def game(message: Message):
    if prov_igr(base_game, message.from_user.id)==False :
        await message.answer(text=open_panel(base_game),
                         reply_markup=open_sour(base_game))
    else:
        await message.answer(text=my_game(base_game, message.from_user.id),
                             reply_markup=clava_del())

@router.message(F.text=="Создать игру")
async def create_game(message: Message):
    if len(base_game)<6:
        server=ses()
        server.n_us1=message.from_user.username
        server.us1=message.from_user.id
        server.time_start=time.time()
        base_game.append(server)
        us_in_game.append(message.from_user.id)
        await message.answer(text=f'Вы создали игру, ожидание пользователя\n',
                             reply_markup=clava_del())
        await message.answer(text=my_game(base_game, message.from_user.id))
    else:
        await message.answer(text="Нелья создать больше 6-ти игр!")
    #таймер



#вход в игру со стороны юзера2
# @router.message(F.text[:4]=="Игра")
# async def game_in(message: Message):


#начало игры
@router.message(F.text=="Начать игру")
async def start_game(message:Message, bot: Bot):
    n_game=num_u(base_game, message.from_user.id)
    nu=n_game
    if n_game!=52 and base_game[nu].sost == False:
        num=randint(1, len(sp))
        base_game[n_game].slov=sp[num]
        print(base_game[n_game].time_start)
        print(base_game[n_game].slov)
        base_game[n_game].slov_sh=len(base_game[n_game].slov)*"*"
        base_game[n_game].sost=True
        await message.answer(text=f'Игра началась!\n'
                             f'Ваше слово: {base_game[n_game].slov_sh}\n'
                             f'Счет: {base_game[nu].n_us1} {base_game[nu].s1_bal}:{base_game[nu].s2_bal} {base_game[nu].n_us2}\n'
                             f'Пиши буквы или слово целиком что бы выйграть!',
                             reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        so=prot(base_game, n_game, message.from_user.id)
        if so!=None:
                await bot.send_message(so, f'Игра началась!\n'
                             f'Ваше слово: {base_game[n_game].slov_sh}\n'
                             f'Счет: {base_game[nu].n_us1} {base_game[nu].s1_bal}:{base_game[nu].s2_bal} {base_game[nu].n_us2}\n'
                             f'Пиши буквы или слово целиком что бы выйграть!',
                             reply_markup=ReplyKeyboardRemove(remove_keyboard=True))


#удаление игр
@router.message(F.text=="Удалить игру")
async def sel_game(message: Message):
    nur=num_u(base_game, message.from_user.id)
    if nur!=52:
        base_game.pop(nur)
        us_in_game.remove(message.from_user.id)
        await message.answer(text= "Игра удалена")
        await message.answer(text=open_panel(base_game),
                         reply_markup=open_sour(base_game))
    else:
        await message.answer(text="У вас нет созданной игры")
        await message.answer(text=open_panel(base_game),
                         reply_markup=open_sour(base_game))

#отгадание слова или буквы
@router.message((F.text & F.from_user.id.in_(us_in_game)))
async def otg(message: Message, bot: Bot):
    nu=num_u(base_game, message.from_user.id)
    if len(message.text)==1:
        if base_game[nu].sost==True and (message.text).lower() in base_game[nu].slov and (message.text).lower() not in base_game[nu].slov_sh:
            base_game[nu].slov_sh=bucv_otg(message.text, base_game[nu].slov, base_game[nu].slov_sh)
            top_up(message.from_user.id)
            wh=bal(base_game, nu, 1, message.from_user.id)
            if wh==1:
                base_game[nu].s1_bal+=1
            if wh==2:
                base_game[nu].s2_bal+=1
            await message.answer(text=f"Правильно!\n"
                                 f'Вы получаете +1 балл в рейтингу!\n'
                                 f'Счет: {base_game[nu].n_us1} {base_game[nu].s1_bal}:{base_game[nu].s2_bal} {base_game[nu].n_us2}\n'
                           f'Теперь слово: {base_game[nu].slov_sh}')
            so=prot(base_game, nu, message.from_user.id)
            if so!=None:
                await bot.send_message(so, f"Ваш соперник отгадал букву!\n"
                                       f'Счет: {base_game[nu].n_us1} {base_game[nu].s1_bal}:{base_game[nu].s2_bal} {base_game[nu].n_us2}\n'
                           f'Теперь слово: {base_game[nu].slov_sh}'
                )
        else:
            if base_game[nu].sost==True:
                await message.answer(text="Увы, но такой буквы в слове нет!")
            else:
                await message.answer(text="Игра еще не началась")
        if base_game[nu].sost==True and base_game[nu].slov_sh==base_game[nu].slov:
            top_up(message.from_user.id)
            wh=bal(base_game, nu, 1, message.from_user.id)
            if wh==1:
                base_game[nu].s1_bal+=1
            if wh==2:
                base_game[nu].s2_bal+=1
            await message.answer(text=f'Идеально!\n'
                                 f'Все буквы отгаданы!\n'
                                 f'Вы получаете +1 рейтинг'
                                 f'Счет: {base_game[nu].n_us1} {base_game[nu].s1_bal}:{base_game[nu].s2_bal} {base_game[nu].n_us2}\n'
                                 f'Слово было: {base_game[nu].slov}')
            so=prot(base_game, nu, message.from_user.id)
            if so!=None:
                await bot.send_message(so, f'Вы проиграли!\n'
                                 f'Все буквы отгаданы!\n'
                                 f'Счет: {base_game[nu].n_us1} {base_game[nu].s1_bal}:{base_game[nu].s2_bal} {base_game[nu].n_us2}\n'
                                 f'Слово было: {base_game[nu].slov}')
                us_in_game.remove(so)
            us_in_game.remove(message.from_user.id)
            base_game.pop(nu)
    elif len(message.text)==len(base_game[nu].slov):
        if (message.text).lower()==base_game[nu].slov:
            bals=(len(base_game[nu].slov)-base_game[nu].s1_bal-base_game[nu].s2_bal)
            wh=bal(base_game, nu, 1, message.from_user.id)
            if wh==1:
                base_game[nu].s1_bal+=bals
            if wh==2:
                base_game[nu].s2_bal+=bals
            top_up5(message.from_user.id, bals)# --------------------------------
            await message.answer(text=f'Идеально!\n'
                                 f'Ты отгадал слово!\n'
                                 f'Вы получаете +{bals} к рейтингу\n'
                                 f'Счет: {base_game[nu].n_us1} {base_game[nu].s1_bal}:{base_game[nu].s2_bal} {base_game[nu].n_us2}\n'
                                 f'Слово было: {base_game[nu].slov}')
            so=prot(base_game, nu, message.from_user.id)
            if so!=None:
                await bot.send_message(so, f"Ваш соперник отгадал слово полностью!\n"
                                       f'Вы проиграли\n'
                                       f'Счет: {base_game[nu].n_us1} {base_game[nu].s1_bal}:{base_game[nu].s2_bal} {base_game[nu].n_us2}\n'
                           f'слово было: {base_game[nu].slov}')
                us_in_game.remove(so)
            us_in_game.remove(message.from_user.id)
            base_game.pop(nu)
        else:
            await message.answer(text="Увы, но это другое слово")






#вход в игру со стороны юзера
@router.message(F.text[:4]=="Игра")
async def game_in(message: Message):
    print("fff")
    nu=int(message.text[-1])-1
    if base_game[nu].us2==None:
        base_game[nu].us2=message.from_user.id
        base_game[nu].n_us2=message.from_user.username
        us_in_game.append(message.from_user.id)
        print(us_in_game)
        await message.answer(text=f"Поздравляю, вы зашли в игру!\n"
                            f'Ваш противник: {base_game[nu].n_us1}\n'
                            f'Счет: {base_game[nu].n_us1} {base_game[nu].s1_bal}:{base_game[nu].s2_bal} {base_game[nu].n_us2}\n'
                    f'Отгадывайте буквы или слово целиком',
                    reply_markup=clava_st_game())
    else:
        print("ddd")
        await message.answer(text=f"Игра уже началась\n"
                       f'Вы не можете к ней присоединиться\n\n'
                       f'Счет игры: {base_game[nu].n_us1} {base_game[nu].s1_bal}:{base_game[nu].s2_bal} {base_game[nu].n_us2}')
