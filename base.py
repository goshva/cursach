import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3


class Database():
    def __init__(self):
        super().__init__()
        

    
    def connection(self):
        self.con = sqlite3.connect('main.db')
        self.cur = self.con.cursor()
        


    def login(self, username, role):
                #проверка пользователя
        self.cur.execute(f'SELECT * FROM users WHERE username="{username}" and role="{role}";')
        value = self.cur.fetchall()
        return value

''' import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3


con = sqlite3.connect('database.db')
cur = connection.cur()

cur.execute(f'SELECT * FROM us WHERE username="{username}" and password="{password}";')
value = cur.fetchall()
'''
    
