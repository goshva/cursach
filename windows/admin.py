# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(413, 286)
        Form.setStyleSheet("font: 8pt \"MS Gothic\";\n"
"background-color: rgb(212, 212, 212);")
        self.menu = QtWidgets.QPushButton(parent=Form)
        self.menu.setGeometry(QtCore.QRect(100, 80, 211, 41))
        self.menu.setObjectName("menu")
        self.sotrudniki = QtWidgets.QPushButton(parent=Form)
        self.sotrudniki.setGeometry(QtCore.QRect(100, 20, 211, 41))
        self.sotrudniki.setObjectName("sotrudniki")
        self.klienti = QtWidgets.QPushButton(parent=Form)
        self.klienti.setGeometry(QtCore.QRect(100, 140, 211, 41))
        self.klienti.setObjectName("klienti")
        self.Back_btn = QtWidgets.QPushButton(parent=Form)
        self.Back_btn.setGeometry(QtCore.QRect(100, 230, 211, 41))
        self.Back_btn.setAutoExclusive(False)
        self.Back_btn.setObjectName("Back_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Окно Администратора"))
        self.menu.setText(_translate("Form", "Меню"))
        self.sotrudniki.setText(_translate("Form", "Сотрудники"))
        self.klienti.setText(_translate("Form", "Клиенты"))
        self.Back_btn.setText(_translate("Form", "Назад"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())