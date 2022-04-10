import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import SimulatorGUI
import GraphBuilder
import StatisticCalculator
import json
import traceback


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.statistic_calculator = StatisticCalculator.StatisticCalculator()
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = SimulatorGUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_botton.clicked.connect(self.start_btn_clicked)
        '''
        with open("styles_dict.json", "r") as read_file:
            self.styles_dict = json.load(read_file)
        '''

    def start_btn_clicked(self):
        # print(float(self.ui.k1_input.text()))
        # GraphBuilder.GraphBuilder.build_animated_graph([0])
        try:
            GraphBuilder.GraphBuilder.build_animated_graphs(
                self.statistic_calculator.get_disease_stat_array([100000, 0, 0, 0, 0, 0], 300), 100, 300)
            print(traceback.format_exc())
        except Exception as _ex:
            print(traceback.format_exc())
        # self.ui.n1_input.setStyleSheet(self.styles_dict['error_input'])
