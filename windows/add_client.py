# Form implementation generated from reading ui file 'add_client.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_add_client(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(313, 266)
        Form.setStyleSheet("font: 8pt \"MS Gothic\";\n"
"background-color: rgb(212, 212, 212);")
        self.name_lline = QtWidgets.QLineEdit(parent=Form)
        self.name_lline.setGeometry(QtCore.QRect(10, 20, 291, 31))
        self.name_lline.setObjectName("name_lline")
        self.lastname_line = QtWidgets.QLineEdit(parent=Form)
        self.lastname_line.setGeometry(QtCore.QRect(10, 70, 291, 31))
        self.lastname_line.setText("")
        self.lastname_line.setObjectName("lastname_line")
        self.phone_line = QtWidgets.QLineEdit(parent=Form)
        self.phone_line.setGeometry(QtCore.QRect(10, 120, 291, 31))
        self.phone_line.setObjectName("phone_line")
        self.skidka_line = QtWidgets.QLineEdit(parent=Form)
        self.skidka_line.setGeometry(QtCore.QRect(10, 170, 291, 31))
        self.skidka_line.setObjectName("skidka_line")
        self.add_btn = QtWidgets.QPushButton(parent=Form)
        self.add_btn.setGeometry(QtCore.QRect(10, 220, 291, 31))
        self.add_btn.setObjectName("add_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить клиента"))
        self.name_lline.setPlaceholderText(_translate("Form", "Введите имя..."))
        self.lastname_line.setPlaceholderText(_translate("Form", "Введите фамилию..."))
        self.phone_line.setPlaceholderText(_translate("Form", "Введите номер телефона..."))
        self.skidka_line.setPlaceholderText(_translate("Form", "Введите процент скидки..."))
        self.add_btn.setText(_translate("Form", "Добавить "))