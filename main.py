#Сделать!!!
'''1) авторизация(частично сделанна)
'''



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
from windows.orders import Ui_ord
from windows.client_win import Ui_Client

from windows.add_emp import Ui_add_emp
from windows.add_client import Ui_add_client
from windows.add_order import Ui_add_ord


from base import Database
from check_db import *




#Окно авторизации
class Vhod_win(QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.datab = Database()
        self.datab.connection()
        

        self.pushButton_2.clicked.connect(self.auth)
        self.pushButton.clicked.connect(self.reg_bt)

        self.base_line_edit = [self.lineEdit, self.lineEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)


    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        

    def reg_bt(self):    
        vhod_win.close()
        reg_win.show()


    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    @check_input
    def auth(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        role = self.combobox2.currentText()
        check_us = self.check_db.thr_login(username, password)
        role_us = self.check_db.thr_role(username, role)
        oficiant_win.show()
'''        if check_us == username and role_us == 'admin':
            vhod_win.close()
            admin_win.show()
        elif check_us == username and role_us == 'waiter':
            vhod_win.close()
            oficiant_win.show()
'''


#Окно регистрации

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
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Имя пользователя уже используется!')
            error.exec()

        elif value == []:
            cur.execute(f"INSERT INTO users (username, password, email, role)"
                        f" VALUES ('{self.reg_line.text()}', '{self.pass_line.text()}',"
                        f" '{self.emai_line.text()}', '{self.combobox2.currentText()}')")
            con.commit()
            con.close
            done = QMessageBox()
            done.setWindowTitle('Успешно!')
            done.setText('Пользователь успешно зарегестрирован!')
            done.exec()

        reg_win.close()

        admin_win.show()
        


#Окно админа
class Admin_win(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Back_btn.clicked.connect(self.back)
        self.sotrudniki.clicked.connect(self.emp_btn)
        self.menu.clicked.connect(self.menu_btn)
        self.klienti.clicked.connect(self.clients)
        
    def back(self):
        admin_win.close()
        vhod_win.show()

    def emp_btn(self):
        emp_win.show()

    def menu_btn(self):
        menu_win.show()

    def clients(self):
        clients_win.show()


#Сотрудники
class Employers(QMainWindow, Ui_Emp, Ui_add_emp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.back_btn)
        self.add_btn.clicked.connect(self.add_emp)


    def back_btn(self):
        emp_win.close()
        admin_win.show()

    def add_emp(self):
        add_emp.show()


#Окно официанта
class Oficiant_win(QMainWindow, Ui_Form_of):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_5.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.menu_btn)
        self.pushButton_4.clicked.connect(self.orders)

    def back(self):
        oficiant_win.close()
        vhod_win.show()

    def menu_btn(self):
        menu_win.show()


    def orders(self):
        zakaz_win.show()


#окно меню
class Menu_win(QMainWindow, Ui_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back_btn.clicked.connect(self.back)

    def back(self):
        menu_win.close()


#окно заказов
class Orders_win(QMainWindow, Ui_ord):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.back_btn)
        self.add_btn.clicked.connect(self.add_ord)

    def back_btn(self):
        zakaz_win.close()

    def add_ord(self):
        add_order.show()

#окно клиентов
class Clients(QMainWindow, Ui_Client):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.back_btn)
        self.add_btn.clicked.connect(self.add_client)

    def back_btn(self):
        clients_win.close()

    def add_client(self):
        add_client.show()


#добавочные окна
    
class Add_client(QMainWindow, Ui_add_client):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Add_emp(QMainWindow, Ui_add_emp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Add_order(QMainWindow, Ui_add_ord):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   



    
app = QApplication([])

vhod_win = Vhod_win()
vhod_win.show()

admin_win = Admin_win()
oficiant_win = Oficiant_win()
reg_win = Registr_win()

menu_win = Menu_win()
emp_win = Employers()
zakaz_win = Orders_win()
clients_win = Clients()

add_client = Add_client()
add_emp = Add_emp()
add_order = Add_order()

app.exec()