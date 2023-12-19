import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt6.QtWidgets import QMessageBox


class Database():
    def __init__(self):
        super().__init__()
    
    def connection(self):
        self.con = sqlite3.connect('main.db')
        self.cur = self.con.cursor()

    def login(self, username, password):
        #проверка пользователя
        self.cur.execute(f'SELECT * FROM users WHERE username="{username}" and password="{password}";')
        value = self.cur.fetchall()
        return value
    