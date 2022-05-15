from PyQt5 import QtWidgets
import StatisticCalculator
import DataWorker
import infoWindowGUI
import sys

class InfoWin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = infoWindowGUI.Ui_Dialog()
        self.ui.setupUi(self)
