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
