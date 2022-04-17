from PyQt5 import QtWidgets
import SimulatorGUI
import GraphBuilder
import StatisticCalculator
import traceback
import StylesGetter
import DataWorker


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.statistic_calculator = StatisticCalculator.StatisticCalculator()
        print(DataWorker.DataWorker.load_coefs_dict())
        self.statistic_calculator.coeffs_dict = DataWorker.DataWorker.load_coefs_dict()
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = SimulatorGUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.k1_input.setText(str(self.statistic_calculator.coeffs_dict['k1']))
        self.ui.k2_input.setText(str(self.statistic_calculator.coeffs_dict['k2']))
        self.ui.k3_input.setText(str(self.statistic_calculator.coeffs_dict['k3']))
        self.ui.k4_input.setText(str(self.statistic_calculator.coeffs_dict['k4']))
        self.ui.k5_input.setText(str(self.statistic_calculator.coeffs_dict['k5']))
        self.ui.k6_input.setText(str(self.statistic_calculator.coeffs_dict['k6']))
        self.ui.k7_input.setText(str(self.statistic_calculator.coeffs_dict['k7']))
        self.ui.start_button.clicked.connect(self.start_btn_clicked)

    def start_btn_clicked(self):
        try:
            self.set_init_input_styles()
            errors_coef_input_dict = self.check_coef_input()
            errors_people_input_dict = self.check_people_input()

            if not 1 in (list(errors_coef_input_dict.values()) + list(errors_people_input_dict.values())):
                self.statistic_calculator.coeffs_dict['k1'] = float(self.ui.k1_input.text())
                self.statistic_calculator.coeffs_dict['k2'] = float(self.ui.k2_input.text())
                self.statistic_calculator.coeffs_dict['k3'] = float(self.ui.k3_input.text())
                self.statistic_calculator.coeffs_dict['k4'] = float(self.ui.k4_input.text())
                self.statistic_calculator.coeffs_dict['k5'] = float(self.ui.k5_input.text())
                self.statistic_calculator.coeffs_dict['k6'] = float(self.ui.k6_input.text())
                self.statistic_calculator.coeffs_dict['k7'] = float(self.ui.k7_input.text())
                errors_coef_dict = self.statistic_calculator.check_coeffs_correctness()
                if not 1 in list(errors_coef_dict.values()):
                    DataWorker.DataWorker.dump_coefs_dict(self.statistic_calculator.coeffs_dict)
                    GraphBuilder.GraphBuilder.build_animated_graphs(
                        self.statistic_calculator.get_disease_stat_array([int(self.ui.h1_input.text()),
                                                                          int(self.ui.h2_input.text()),
                                                                          int(self.ui.s1_input.text()),
                                                                          int(self.ui.s2_input.text()),
                                                                          int(self.ui.d_input.text())], 600), 100, 600,
                        list(self.statistic_calculator.groups_names_values_dict.values()))
                else:
                    self.mark_coef_input_error(errors_coef_dict)
            else:
                self.mark_coef_input_error(errors_coef_input_dict)
                self.mark_people_input_error(errors_people_input_dict)
        except:
            print(traceback.format_exc())
        # self.ui.n1_input.setStyleSheet(self.styles_dict['error_input'])

    def set_init_input_styles(self):
        self.ui.k1_input.setStyleSheet(StylesGetter.StylesGetter.get_init_coef_input_style())
        self.ui.k2_input.setStyleSheet(StylesGetter.StylesGetter.get_init_coef_input_style())
        self.ui.k3_input.setStyleSheet(StylesGetter.StylesGetter.get_init_coef_input_style())
        self.ui.k4_input.setStyleSheet(StylesGetter.StylesGetter.get_init_coef_input_style())
        self.ui.k5_input.setStyleSheet(StylesGetter.StylesGetter.get_init_coef_input_style())
        self.ui.k6_input.setStyleSheet(StylesGetter.StylesGetter.get_init_coef_input_style())
        self.ui.k7_input.setStyleSheet(StylesGetter.StylesGetter.get_init_coef_input_style())

        self.ui.h1_input.setStyleSheet((StylesGetter.StylesGetter.get_init_people_input_style()))
        self.ui.h2_input.setStyleSheet((StylesGetter.StylesGetter.get_init_people_input_style()))
        self.ui.s1_input.setStyleSheet((StylesGetter.StylesGetter.get_init_people_input_style()))
        self.ui.s2_input.setStyleSheet((StylesGetter.StylesGetter.get_init_people_input_style()))
        self.ui.d_input.setStyleSheet((StylesGetter.StylesGetter.get_init_people_input_style()))

    def check_coef_input(self):
        input_error_dict = {}
        for coef_name in self.statistic_calculator.coeffs_names_list:
            input_error_dict[coef_name] = coef_name
        try:
            float(self.ui.k1_input.text())
            input_error_dict[self.statistic_calculator.coeffs_names_list[0]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.coeffs_names_list[0]] = 1
        try:
            float(self.ui.k2_input.text())
            input_error_dict[self.statistic_calculator.coeffs_names_list[1]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.coeffs_names_list[1]] = 1
        try:
            float(self.ui.k3_input.text())
            input_error_dict[self.statistic_calculator.coeffs_names_list[2]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.coeffs_names_list[2]] = 1
        try:
            float(self.ui.k4_input.text())
            input_error_dict[self.statistic_calculator.coeffs_names_list[3]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.coeffs_names_list[3]] = 1
        try:
            float(self.ui.k5_input.text())
            input_error_dict[self.statistic_calculator.coeffs_names_list[4]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.coeffs_names_list[4]] = 1
        try:
            float(self.ui.k6_input.text())
            input_error_dict[self.statistic_calculator.coeffs_names_list[5]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.coeffs_names_list[5]] = 1
        try:
            float(self.ui.k7_input.text())
            input_error_dict[self.statistic_calculator.coeffs_names_list[6]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.coeffs_names_list[6]] = 1
        return input_error_dict

    def check_people_input(self):
        input_error_dict = {}
        for coef_name in self.statistic_calculator.people_groups_names_list:
            input_error_dict[coef_name] = coef_name
        try:
            int(self.ui.h1_input.text())
            input_error_dict[self.statistic_calculator.people_groups_names_list[0]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.people_groups_names_list[0]] = 1
        try:
            int(self.ui.h2_input.text())
            input_error_dict[self.statistic_calculator.people_groups_names_list[1]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.people_groups_names_list[1]] = 1
        try:
            int(self.ui.s1_input.text())
            input_error_dict[self.statistic_calculator.people_groups_names_list[2]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.people_groups_names_list[2]] = 1
        try:
            int(self.ui.s2_input.text())
            input_error_dict[self.statistic_calculator.people_groups_names_list[3]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.people_groups_names_list[3]] = 1
        try:
            int(self.ui.d_input.text())
            input_error_dict[self.statistic_calculator.people_groups_names_list[4]] = 0
        except ValueError:
            input_error_dict[self.statistic_calculator.people_groups_names_list[4]] = 1
        return input_error_dict

    def mark_coef_input_error(self, input_error_dict):
        if input_error_dict[self.statistic_calculator.coeffs_names_list[0]] == 1:
            self.ui.k1_input.setStyleSheet((StylesGetter.StylesGetter.get_error_coef_input_style()))
        if input_error_dict[self.statistic_calculator.coeffs_names_list[1]] == 1:
            self.ui.k2_input.setStyleSheet((StylesGetter.StylesGetter.get_error_coef_input_style()))
        if input_error_dict[self.statistic_calculator.coeffs_names_list[2]] == 1:
            self.ui.k3_input.setStyleSheet((StylesGetter.StylesGetter.get_error_coef_input_style()))
        if input_error_dict[self.statistic_calculator.coeffs_names_list[3]] == 1:
            self.ui.k4_input.setStyleSheet((StylesGetter.StylesGetter.get_error_coef_input_style()))
        if input_error_dict[self.statistic_calculator.coeffs_names_list[4]] == 1:
            self.ui.k5_input.setStyleSheet((StylesGetter.StylesGetter.get_error_coef_input_style()))
        if input_error_dict[self.statistic_calculator.coeffs_names_list[5]] == 1:
            self.ui.k6_input.setStyleSheet((StylesGetter.StylesGetter.get_error_coef_input_style()))
        if input_error_dict[self.statistic_calculator.coeffs_names_list[6]] == 1:
            self.ui.k7_input.setStyleSheet((StylesGetter.StylesGetter.get_error_coef_input_style()))

    def mark_people_input_error(self, input_error_dict):
        if input_error_dict[self.statistic_calculator.people_groups_names_list[0]] == 1:
            self.ui.h1_input.setStyleSheet((StylesGetter.StylesGetter.get_error_people_input_style()))
        if input_error_dict[self.statistic_calculator.people_groups_names_list[1]] == 1:
            self.ui.h2_input.setStyleSheet((StylesGetter.StylesGetter.get_error_people_input_style()))
        if input_error_dict[self.statistic_calculator.people_groups_names_list[2]] == 1:
            self.ui.s1_input.setStyleSheet((StylesGetter.StylesGetter.get_error_people_input_style()))
        if input_error_dict[self.statistic_calculator.people_groups_names_list[3]] == 1:
            self.ui.s2_input.setStyleSheet((StylesGetter.StylesGetter.get_error_people_input_style()))
        if input_error_dict[self.statistic_calculator.people_groups_names_list[4]] == 1:
            self.ui.d_input.setStyleSheet((StylesGetter.StylesGetter.get_error_people_input_style()))
