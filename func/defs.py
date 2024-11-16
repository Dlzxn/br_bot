import sqlite3
from log_cfg.log_def import start_log


def ref_prov(id_use):
    sqlite_connection = sqlite3.connect('bd/bd_users')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from users"""
    # start_log()
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if row[0]==id_use:
            cursor.close()
            return True
    cursor.close()
    return False
#проверка есть ли юзер в бд



def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    conn = sqlite3.connect('bd/bd_users', check_same_thread=False)
    # start_log()
    cursor = conn.cursor() #курсор для бд
    cursor.execute('INSERT INTO users (user_id, user_name, user_suname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()
#запись нового юзера в бд


def from_bd(num: int, user_id: int):
    sqlite_connection = sqlite3.connect('bd/bd_users')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from users"""
    # start_log()
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if row[0]==user_id:
            return row[num]
    cursor.close()
#забирает номер столбца бд кот нуден и пользователя возвращает значение заданнного столбца

def pars_all():
    sqlite_connection = sqlite3.connect('bd/bd_users')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from users"""
    # start_log()
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    sp_out=[]
    for row in records:
        sp_out.append(row[0])
    cursor.close()
    return sp_out
#запрос всех юзеров --->список


#рисует по бд картинку
def pict():
    sqlite_connection = sqlite3.connect('bd/bd_users')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from picture"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    cursor.close()
    sp=[[['0'], ['0'], ['0'], ['0'], ['0']], [['0'], ['0'], ['0'], ['0'], ['0']], [['0'], ['0'], ['0'], ['0'], ['0']], [['0'], ['0'], ['0'], ['0'], ['0']]]
    s1=''
    s2=''
    s3=''
    s4=''
    for i in range(0,4):
        for j in range(0, 5):
            sp[i][j]='⬜️'
    for row in records:
        if row[1]!=None:
            stroka=row[0]%10
            stb=row[0]//10
            if stb<3:
                sp[stb-1][stroka-1]='🟥'
            else:
                sp[stb-1][stroka-1]='🟩'
    for i in range(0, 5):
        s1=s1+sp[0][i]
        s2=s2+sp[1][i]
        s3=s3+sp[2][i]
        s4=s4+sp[3][i]
    return s1, s2, s3, s4


def pict_prov(nu):
    nu=int(nu)
    strk=(nu-1)//5+1
    stlb=(nu-1)%5+1
    st=str(strk)+str(stlb)
    sqlite_connection = sqlite3.connect('bd/bd_users')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from picture"""
    # start_log()
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    for row in records:
        if str(row[0])==st:
            # cursor.close()
            if row[1]!=None:
                return True
            else:
                return False
    cursor.close()
    return False
#проверка закрашена ли клетка

def pict_us(nu):
    nu=int(nu)
    strk=(nu-1)//5+1
    stlb=(nu-1)%5+1
    st=str(strk)+str(stlb)
    sqlite_connection = sqlite3.connect('bd/bd_users')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from picture"""
    # start_log()
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if str(row[0])==st:
            cursor.close()
            return row[2]
    cursor.close()
    return False
#вывод кто закрасил клетку

def new_us_kl(num: int, user_id: int, user_name: str, username: str):
    nu=int(num)
    strk=(nu-1)//5+1
    stlb=(nu-1)%5+1
    st=str(strk)+str(stlb)
    sqlite_connection = sqlite3.connect('bd/bd_users')
    cursor = sqlite_connection.cursor()
    start_log()
    cursor.execute('UPDATE picture SET user_id = ? WHERE num = ?', (user_id, st))
    cursor.execute('UPDATE picture SET user_name = ? WHERE num = ?', (user_name, st))
    cursor.execute('UPDATE picture SET username = ? WHERE num = ?', (username, st))
    sqlite_connection.commit()
    sqlite_connection.close()





#удаление из бд всех
def del_pict():
    sqlite_connection = sqlite3.connect('bd/bd_users')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from picture"""
    # start_log()
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        cursor.execute('UPDATE picture SET user_id = ? WHERE num = ?', (None, row[0]))
        cursor.execute('UPDATE picture SET user_name = ? WHERE num = ?', (None, row[0]))
        cursor.execute('UPDATE picture SET username = ? WHERE num = ?', (None, row[0]))
        sqlite_connection.commit()
    cursor.close()
    sqlite_connection.close()


#парсинг топ юзера
def stat_us():
    sqlite_connection = sqlite3.connect('bd/bd_users')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from users"""
    # start_log()
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    sp_us=['', '', '']
    sp_kol=[0, 0, 0]
    for row in records:
        print(sp_us, sp_kol)
        if int(row[5])>sp_kol[0]:
            sp_kol[0]=int(row[5])
            sp_us[0]='@'+row[3]
            if sp_kol[1]<sp_kol[0]:
                sp_kol[1], sp_kol[0]=sp_kol[0], sp_kol[1]
                sp_us[1], sp_us[0]=sp_us[0], sp_us[1]
                if sp_kol[2]<sp_kol[1]:
                    sp_kol[2], sp_kol[1]=sp_kol[1], sp_kol[2]
                    sp_us[2], sp_us[1]=sp_us[1], sp_us[2]
    for i in range(len(sp_us)):
        if sp_us[i]=='':
            sp_us[i]="❌"
    return sp_us, sp_kol

#введение закраски клетки
def top_up(id: int):
    sqlite_connection = sqlite3.connect('bd/bd_users')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from users"""
    # start_log()
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if int(row[0])==id:
            cursor.execute('UPDATE users SET rate = ? WHERE user_id = ?', (int(row[5])+1, id))
            break
    sqlite_connection.commit()
