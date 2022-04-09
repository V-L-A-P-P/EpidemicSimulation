import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import SimulatorGUI
import GraphBuilder
import StatisticCalculator


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = SimulatorGUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_botton.clicked.connect(self.start_btn_clicked)

    def start_btn_clicked(self):
        print(self.ui.n1_input.text())


