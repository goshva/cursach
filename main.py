import sys
import sqlite3
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QComboBox
from PyQt6.QtSql import QSqlQueryModel

from windows.vhod import Ui_Main
from windows.admin import Ui_Form
from windows.oficiant import Ui_Form_of
from windows.registr import Ui_widget

from windows.menu_win import Ui_Menu
from windows.emp_win import Ui_Emp

from base import Database


#Окно авторизации
class Vhod_win(QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.datab = Database()
        self.datab.connection()
        

        self.pushButton_2.clicked.connect(self.auth)
        self.pushButton.clicked.connect(self.reg_bt)
        
        
    def reg_bt(self):    
        vhod_win.close()
        reg_win.show()



    def auth(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        data = self.datab.login(username, password)
        print(data)
        if data == []:
            error = QMessageBox()
            error.setWindowTitle('ОШИБКА!')
            error.setText('Ошибка авторизации!')
            error.exec()
        else:
            print('Успешная авторизация!')
            admin_win.show()
            vhod_win.close()
    
       #oficiant_win.show()



#Окно регистрации
'''class Registr_win(QMainWindow, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.reg_btn.clicked.connect(self.reg)

    def reg(self):
        reg_win.close()
        vhod_win.show()
'''
class Registr_win(QMainWindow, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.username = self.reg_line.text()
        self.password = self.pass_line.text()
        self.email = self.emai_line.text()
        self.role_us = self.combobox2.currentText()
        self.reg_btn.clicked.connect(self.reg)

    def reg(self):
        con = sqlite3.connect('main.db')
        cur = con.cursor()
        cur.execute(f'SELECT * FROM users WHERE username="{self.reg_line.text()}";')
        value = cur.fetchall()

        if value != []:
            print('Имя пользователя уже используется!')

        elif value == []:
            cur.execute(f"INSERT INTO users (username, password, email, role) VALUES ('{self.reg_line.text()}', '{self.pass_line.text()}', '{self.emai_line.text()}', '{self.combobox2.currentText()}')")
            con.commit()
            con.close
            print('Успешная регистарция!')

        reg_win.close()
        #vhod_win.show()
        admin_win.show()
        


#Окно админа
class Admin_win(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Back_btn.clicked.connect(self.back)
        self.sotrudniki.clicked.connect(self.emp_btn)

    def back(self):
        admin_win.close()
        vhod_win.show()

    def emp_btn(self):
        admin_win.close()
        emp_win.show()

class Employers(QMainWindow, Ui_Emp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table_name = 'Сотрудники'

        self.back.clicked.connect(self.back_btn)
 

    def back_btn(self):
        emp_win.close()
        admin_win.show()


#Окно официанта
class Oficiant_win(QMainWindow, Ui_Form_of):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_5.clicked.connect(self.back)

    def back(self):
        oficiant_win.close()
        #vhod_win.show()



class Menu_win(QMainWindow, Ui_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back_btn.clicked.connect(self.back)
    def back(self):
        menu_win.close()
        admin_win.show()





app = QApplication([])

vhod_win = Vhod_win()
vhod_win.show()

admin_win = Admin_win()
oficiant_win = Oficiant_win()
reg_win = Registr_win()

menu_win = Menu_win()
emp_win = Employers()


app.exec()