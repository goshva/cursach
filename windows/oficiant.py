# Form implementation generated from reading ui file 'oficiant.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_of(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(407, 248)
        Form.setStyleSheet("font: 8pt \"MS Gothic\";\n"
"background-color: rgb(212, 212, 212);")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 40, 201, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 100, 201, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 180, 201, 41))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Окно Официанта"))
        self.pushButton_3.setText(_translate("Form", "Меню"))
        self.pushButton_4.setText(_translate("Form", "Заказы"))
        self.pushButton_5.setText(_translate("Form", "Назад"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_of()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())