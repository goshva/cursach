import sqlite3


def login(username, password):
    con = sqlite3.connect('main.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE username="{username}" ;')
    value = cur.fetchall()

    if value != [] and value[0][2] == password:
        print('Успешная авторизация!')

    else:
        print('Проверьте правильность ввода данных!')

    cur.close()
    con.close()