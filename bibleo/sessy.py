import aiogram
from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup



class ses():
    us1: int=None
    n_us1: str=None
    us2: int=None
    n_us2: str=None
    sost: bool=False
    time_start: int
    s1_bal: int=0
    s2_bal: int=0
    len_b: int=None
    slov: str=None
    slov_sh: str=None


base_game=[]

def open_sour(sp):
    kol_ses=len(sp)
    but=[[KeyboardButton(text="Создать игру")], [KeyboardButton(text="Игра "+str(i)) for i in range(1, kol_ses+1)]]
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

#проверка на наличие игры у юзера
def prov_igr(sp ,id):
    for i in range(len(sp)):
        if sp[i].us1==id or sp[i].us2==id:
            return True
    return False

#вывод игры юзера
def my_game(sp, id):
    s=f'Ваша игра:\n\n'
    for i in range(0, len(sp)):
        if sp[i].sost==False:
            stat='Неактивна-\nОжидайте игрока\nИли начните один!'
        else:
            stat='В игре'
        if sp[i].us1==id:
            s2=(f'🎮Игра {i+1}\n'
            f'👤Игрок 1: {sp[i].n_us1}\n'
            f'👥Игрок 2: {sp[i].n_us2}\n'
            f'--Состояние: {stat}\n\n')
            s=s+s2
            break
    return s

#
def one_game(sp, id):
    s=0
    for i in range(0, len(sp)):
        if sp[i].us1==id:
            s==1
    if s==0:
        return True
    else:
        return False

def clava_del():
    bust=[[KeyboardButton(text="Удалить игру")]]
    nur_key=ReplyKeyboardMarkup(keyboard=bust, resize_keyboard=True, input_field_placeholder="Ожидание игрока")
    return nur_key

def clava_st_game():
    bust=[[KeyboardButton(text="Начать игру")]]
    nur_key=ReplyKeyboardMarkup(keyboard=bust, resize_keyboard=True, input_field_placeholder="Ожидание игрока")
    return nur_key
#вывод номера игры юзера
def num_u(sp ,id):
    for i in range(len(sp)):
        if sp[i].us1==id or sp[i].us2==id:
            return i
    return 52

#отгадал букву
def bucv_otg(bu, st, std):
    sp=[std[i] for i in range(len(std))]
    s=''
    for i in range(len(st)):
        if st[i]==bu.lower():
            sp[i]=bu.lower()
        s+=sp[i]
    return s


#чат ид противника
def prot(sp, cd, id):
    if sp[cd].us1==id:
        return sp[cd].us2
    elif sp[cd].us2==id:
        return sp[cd].us1


#выдача локально баллов
def bal(sp, nu, col, id):
    if sp[nu].us1==id:
        return 1
    else:
        return 2