import aiogram
from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup



class ses():
    us1: int
    n_us1: str=None
    us2: int
    n_us2: str=None
    sost: bool=False


base_game=[]

def open_sour(sp):
    kol_ses=len(sp)
    but=[[KeyboardButton(text="Создать игру")], [KeyboardButton(text=str(i)+" игра") for i in range(1, kol_ses+1)]]
    num_key=ReplyKeyboardMarkup(keyboard=but, resize_keyboard=True, input_field_placeholder="Выберите сессию игры")
    # but=['{i}' for i in range(1, kol_ses+1)]
    return num_key
def open_panel(sp):
    s=f'Все игры в данный момент:\n\n'
    for i in range(0, len(sp)):
        if sp[i].sost==False:
            stat='Неактивна'
        else:
            stat='В игре'
        s2=(f'🎮Игра {i+1}\n'
        f'👤Игрок 1: {sp[i].n_us1}\n'
        f'👥Игрок 2: {sp[i].n_us2}\n'
        f'--Состояние: {stat}\n\n')
        s=s+s2
    return s
