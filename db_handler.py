import sqlite3
from PyQt6.QtWidgets import QMessageBox

def login(username, password):
    con = sqlite3.connect('main.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE username="{username}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == password:
        print('Успешная авторизация!')
    else:
        error = QMessageBox()
        error.setWindowTitle('Ошибка!')
        error.setText('Ошибка авторизации!')
        error.exec()


    cur.close()
    con.close()

def check_role(username, role):
    con = sqlite3.connect('main.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE username="{username}" and role="{role}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == role:
        
        print('Роль успешно выбрана!')
    else:
        error = QMessageBox()
        error.setWindowTitle('Ошибка!')
        error.setText('Ошибка выбора роли!')
        error.exec()

    cur.close()
    con.close()