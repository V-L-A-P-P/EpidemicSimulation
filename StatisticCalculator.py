class StatisticCalculator:
    def __init__(self):
        self.coeffs_dict = {  # словарь коэффицентов
            # Коэффицент перехода из группы "Здоровые невакцинированные" в группу "Больные невакцинированные"
            'k1': 0.02,
            # Коэффицент перехода из группы "Больные невакцинированные" в группу "Здоровые невакцинированные"
            'k2': 0.02,
            # Коэффицент перехода из группы "Здоровые вакцинированные" в группу "Больные вакцинированные"
            'k3': 0.02,
            # Коэффицент перехода из группы "Больные вакцинированные" в группу "Здоровые вакцинированные"
            'k4': 0.02,
            # Коэффицент перехода из группы "Здоровые невакцинированные" в группу "Здоровые вакцинированные"
            'k5': 0.02,
            # Коэффицент перехода из группы "Больные невакцинированные" в группу "Умершие"
            'k6': 0.02,
            # Коэффицент перехода из группы "Больные вакцинированные" в группу "Умершие"
            'k7': 0.02
        }

    def calculate_h1(self, h1_prev, s1_prev):  # формула расчёта количества не болевших и не привитых людей
        return h1_prev \
               + round(self.coeffs_dict['k2'] * s1_prev) \
               - round(self.coeffs_dict['k5'] * h1_prev) \
               - round(self.coeffs_dict['k1'] * h1_prev)

    def calculate_h2(self, h1_prev, h2_prev, s2_prev):  # формула расчёта количества заболевших впервые людей
        return h2_prev \
               + round(self.coeffs_dict['k5'] * h1_prev) \
               + round(self.coeffs_dict['k4'] * s2_prev) \
               - round(self.coeffs_dict['k3'] * h2_prev)

    def calculate_s1(self, s1_prev, h1_prev):  # формула расчёта количества выздоровевших людей
        return s1_prev \
               + round(self.coeffs_dict['k1'] * h1_prev) \
               - round(self.coeffs_dict['k2'] * s1_prev) \
               - round(self.coeffs_dict['k6'] * s1_prev)

    def calculate_s2(self, s2_prev, h2_prev):  # формула расчёта количества повторно заболевших людей
        return s2_prev \
               + round(self.coeffs_dict['k3'] * h2_prev) \
               - round(self.coeffs_dict['k4'] * s2_prev) \
               - round(self.coeffs_dict['k7'] * s2_prev)

    def calculate_d(self, d_prev, s1_prev, s2_prev):  # формула расчёта количества вакцинировавшихся людей
        return d_prev \
               + round(self.coeffs_dict['k6'] * s1_prev) \
               + round(self.coeffs_dict['k7'] * s2_prev)

    def get_disease_stat_array(self, people_distr_list, number_of_days):
        dots_arrays_list = [[people_distr_list[0]],
                            [people_distr_list[1]],
                            [people_distr_list[2]],
                            [people_distr_list[3]],
                            [people_distr_list[4]]]
        people_distr_dict = {
            'h1': people_distr_list[0],  # количество непривитых здоровых
            'h2': people_distr_list[1],  # количество привитых здоровых
            's1': people_distr_list[2],  # количество непривитых больных
            's2': people_distr_list[3],  # количество привитых больных
            'd': people_distr_list[4],  # количество умерших людей
        }
        for day_num in range(number_of_days - 1):
            h1_new = self.calculate_h1(people_distr_dict['h1'], people_distr_dict['s1'])
            h2_new = round(
                self.calculate_h2(people_distr_dict['h1'], people_distr_dict['h2'],
                                  people_distr_dict['s2']))
            s1_new = round(self.calculate_s1(people_distr_dict['s1'], people_distr_dict['h1']))
            s2_new = round(self.calculate_s2(people_distr_dict['s2'], people_distr_dict['h2']))
            d_new = round(
                self.calculate_d(people_distr_dict['d'], people_distr_dict['s1'], people_distr_dict['s1']))
            new_people_distr_list = [h1_new, h2_new, s1_new, s2_new, d_new]
            k = 0
            for group_name in people_distr_dict:
                people_distr_dict[group_name] = new_people_distr_list[k]
                k += 1
            for dots_array_num in range(len(dots_arrays_list)):
                dots_arrays_list[dots_array_num].append(new_people_distr_list[dots_array_num])
        return dots_arrays_list

    def check_coeffs(self):
        check_coeffs_dict = {}
        for coeff_name in self.coeffs_dict:
            check_coeffs_dict[coeff_name] = True

        if self.coeffs_dict['k1'] + self.coeffs_dict['k5'] >= 1:
            check_coeffs_dict['k1'] = False
            check_coeffs_dict['k5'] = False
        if self.coeffs_dict['k2'] + self.coeffs_dict['k6'] >= 1:
            check_coeffs_dict['k2'] = False
            check_coeffs_dict['k6'] = False
        if self.coeffs_dict['k4'] + self.coeffs_dict['k7'] >= 1:
            check_coeffs_dict['k4'] = False
            check_coeffs_dict['k7'] = False
        if self.coeffs_dict['k3'] >= 1:
            check_coeffs_dict['k3'] = False
        return check_coeffs_dict

