from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage


from ad_r.cla import FSMF

from func.defs import pars_all, del_pict


storage = MemoryStorage()
router = Router()

user_dict: dict[int, dict[str]] = {}
#адм меню
@router.message((F.text=="/adm") & (F.from_user.id==1007130027))
async def adm_list(message: Message):
    await message.answer(f'Вы-админ\n'
                         f'рассылка- /pars\n'
                         f'Удаление флага /delflag'
                         )

#админское удаление базы с флагом
@router.message((F.text=="/delflag") & (F.from_user.id==1007130027))
async def adm_list(message: Message, bot: Bot):
    await message.answer(text="Начало удаления...")
    del_pict()
    su=pars_all()
    for x in su:
        await bot.send_message(x, "Обновление флага прошло успешно! Начинайте его красить!")
    await message.answer(text="Ветвь удалена//Рассылка запущена")


@router.message((F.text=="/pars") & (F.from_user.id==1007130027), StateFilter(default_state))
async def adm_list(message: Message, bot: Bot, state: FSMContext):
    await message.answer(text="Начало, введи:")
    await state.set_state(FSMF.text)
    # for n in sp_all:
    #     await bot.send_message(n, "Лучшая работа? Ставь 100/10")

    # await message.answer(text="Конец")

#вызод из фсма
@router.message(((F.text=="/exit") & (F.from_user.id==1007130027)), ~StateFilter(default_state))
async def adm_list(message: Message, bot: Bot, state: FSMContext):
    await state.set_state(state=None)
    await message.answer(text="Вышел")


#Ввели имя---проработка
@router.message((F.from_user.id==1007130027), StateFilter(FSMF.text), F.text)
async def process_name_sent(message: Message, state: FSMContext, bot: Bot):
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(text=message.text)
    sp_all=pars_all()
    user_dict[message.from_user.id] = await state.get_data()
    for n in sp_all:
        await bot.send_message(n, user_dict[message.from_user.id]['text'])
    await state.clear()
    await state.set_state(state=None)
    await message.answer(text="Конец")