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
        self.ui.start_button.clicked.connect(self.start_btn_clicked)
        '''
        with open("styles_dict.json", "r") as read_file:
            self.styles_dict = json.load(read_file)
        '''

    def start_btn_clicked(self):
        # print(float(self.ui.k1_input.text()))
        # GraphBuilder.GraphBuilder.build_animated_graph([0])
        try:
            self.statistic_calculator.coeffs_dict['k1'] = float(self.ui.k1_input.text())
            self.statistic_calculator.coeffs_dict['k2'] = float(self.ui.k2_input.text())
            self.statistic_calculator.coeffs_dict['k3'] = float(self.ui.k3_input.text())
            self.statistic_calculator.coeffs_dict['k4'] = float(self.ui.k4_input.text())
            self.statistic_calculator.coeffs_dict['k5'] = float(self.ui.k5_input.text())
            self.statistic_calculator.coeffs_dict['k6'] = float(self.ui.k6_input.text())
            self.statistic_calculator.coeffs_dict['k7'] = float(self.ui.k7_input.text())
            GraphBuilder.GraphBuilder.build_animated_graphs(
                self.statistic_calculator.get_disease_stat_array([int(self.ui.h1_input.text()), int(self.ui.h2_input.text()), int(self.ui.s1_input.text()), int(self.ui.s2_input.text()), int(self.ui.d_input.text())], 300), 100, 300)
            print(traceback.format_exc())
        except Exception as _ex:
            print(traceback.format_exc())
        # self.ui.n1_input.setStyleSheet(self.styles_dict['error_input'])
