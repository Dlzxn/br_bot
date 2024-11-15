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

#пакеты локальные
from us_r import us_rout
from ad_r import ad_rout
from log_cfg.log_def import start_log, user_new
from log_cfg.cfg import logging_config




async def main():
    # logging.config.dictConfig(logging_config) #загрузка настроек
    # start_log()
    #ffff
    load_dotenv()
    # Создаем объекты бота и диспетчера
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    #роутеры

    dp.include_router(us_rout.router)
    dp.include_router(ad_rout.router)

    await dp.start_polling(bot)



asyncio.run(main())