# Form implementation generated from reading ui file 'add_emp.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_add_emp(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(352, 236)
        Form.setStyleSheet("font: 8pt \"MS Gothic\";\n"
"background-color: rgb(212, 212, 212);")
        self.name_line = QtWidgets.QLineEdit(parent=Form)
        self.name_line.setGeometry(QtCore.QRect(40, 20, 271, 31))
        self.name_line.setObjectName("name_line")
        self.lastaname_line = QtWidgets.QLineEdit(parent=Form)
        self.lastaname_line.setGeometry(QtCore.QRect(40, 70, 271, 31))
        self.lastaname_line.setObjectName("lastaname_line")
        self.phone_line = QtWidgets.QLineEdit(parent=Form)
        self.phone_line.setGeometry(QtCore.QRect(40, 120, 271, 31))
        self.phone_line.setObjectName("phone_line")
        self.add_btn = QtWidgets.QPushButton(parent=Form)
        self.add_btn.setGeometry(QtCore.QRect(40, 180, 271, 41))
        self.add_btn.setObjectName("add_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить сотрудника"))
        self.name_line.setPlaceholderText(_translate("Form", "Введите имя..."))
        self.lastaname_line.setPlaceholderText(_translate("Form", "Введите фамилию..."))
        self.phone_line.setPlaceholderText(_translate("Form", "Введите номер телефона..."))
        self.add_btn.setText(_translate("Form", "Добавить"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_add_emp()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())