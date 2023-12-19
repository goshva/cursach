# Form implementation generated from reading ui file 'menu_win.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery


class Ui_Menu(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 475)
        Form.setStyleSheet("font: 8pt \"MS Gothic\";\n"
"background-color: rgb(212, 212, 212);")
        self.menu_table = QtWidgets.QTableView(parent=Form)
        self.menu_table.setGeometry(QtCore.QRect(10, 20, 611, 411))
        self.menu_table.setObjectName("menu_table")
        self.back_btn = QtWidgets.QPushButton(parent=Form)
        self.back_btn.setGeometry(QtCore.QRect(524, 440, 91, 23))
        self.back_btn.setObjectName("back_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # вывод таблицы
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('main.db')
        db.open()
        query = QSqlQuery()
        query.prepare("SELECT * FROM menu")
        query.exec()

        model = QSqlQueryModel()
        model.setQuery(query)
        self.menu_table.setModel(model)
        self.menu_table.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Меню"))
        self.back_btn.setText(_translate("Form", "Назад"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Menu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())