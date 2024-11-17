#пакеты внешние
from aiogram import Bot, Dispatcher, F
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
import asyncio
from aiogram.types import ReplyKeyboardRemove, keyboard_button, ReplyKeyboardMarkup
import time

#пакеты локальные
from us_r import us_rout, pict_ro, author_rout, mus_rout, game
from ad_r import ad_rout
from log_cfg.log_def import start_log, user_new
from log_cfg.cfg import logging_config
from us_r.game import base_game, us_in_game





async def main():
    # logging.config.dictConfig(logging_config) #загрузка настроек
    # start_log()
    #ffff
    load_dotenv()
    # Создаем объекты бота и диспетчера
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    #роутеры
    # for i in range(len(base_game)):
    #     print("fff")
    #     print(base_game[i].time_start)
    #     if time.time()-base_game[i].time_start>120 and base_game[i].sost==False:
    #         us_in_game.remove(base_game[i].us1)
    #         await bot.send_message(base_game[i].us1, "Ваша игра удалена из-за неактивности")
    #         try:
    #             await bot.send_message(base_game[i].us2, "Ваша игра удалена из-за неактивности")
    #             us_in_game.remove(base_game[i].us2)
    #         except:
    #             print("нет 2-го юзера")
    #         base_game.pop(i)
    dp.include_router(ad_rout.router)
    dp.include_router(us_rout.router)
    dp.include_router(mus_rout.router)
    dp.include_router(pict_ro.router)
    dp.include_router(author_rout.router)
    dp.include_router(game.router)



    await dp.start_polling(bot)



asyncio.run(main())