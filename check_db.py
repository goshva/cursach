from PyQt6 import QtCore, QtGui, QtWidgets
from db_handler import *


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, username, password ):
        login(username, password)
