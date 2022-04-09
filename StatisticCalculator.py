class StatisticCalculator:
    def __init__(self):
        self.coefs_dict = {  # словарь коэффицентов
            'k1': 0.02,
            # Коэфицент перехода из группы не вакцинированных в группу впервые заболевшие
            'k2': 0.02,
            # Коэфицент перехода из группы "Впервые заболевшие" в группу "Выздоровевшие"
            'k3': 0.02,  # доля повторно заболевших людей
            'k4': 0.02,  # доля выздоровевших людей после повторного заболевания
            'k5': 0.02,  # доля вакцинированных людей, заболевших впервые
            'k6': 0.02,  # доля умерших людей
            'v': 0.02  # доля людей, которые прошли вакцинацию
        }

    def n1(self, n1_prev):  # формула расчёта количества не болевших и не привитых людей
        return n1_prev \
               - round(self.coefs_dict.get('k1') * n1_prev) \
               - round(self.coefs_dict.get('v') * n1_prev)

    def n2(self, n1_prev, n2_prev, n5_prev):  # формула расчёта количества заболевших впервые людей
        return n2_prev \
               + round(self.coefs_dict.get('k1') * n1_prev) \
               - round(self.coefs_dict.get('k2') * n2_prev) \
               + round(self.coefs_dict.get('k5') * n5_prev) \
               - round(self.coefs_dict.get('k6') * n2_prev)

    def n3(self, n2_prev, n3_prev, n4_prev):  # формула расчёта количества выздоровевших людей
        return n3_prev \
               + round(self.coefs_dict.get('k2') * n2_prev) \
               - round(self.coefs_dict.get('k3') * n3_prev) \
               + round(self.coefs_dict.get('k4') * n4_prev)

    def n4(self, n3_prev, n4_prev):  # формула расчёта количества повторно заболевших людей
        return n4_prev \
               - round(self.coefs_dict.get('k4') * n4_prev) \
               + round(self.coefs_dict.get('k3') * n3_prev) \
               - round(self.coefs_dict.get('k6') * n4_prev)

    def n5(self, n1_prev, n5_prev):  # формула расчёта количества вакцинировавшихся людей
        return n5_prev \
               + round(self.coefs_dict.get('v') * n1_prev) \
               - round(self.coefs_dict.get('k5') * n5_prev)

    def n6(self, n2_prev, n4_prev, n6_prev):  # формула расчёта количества умерших людей
        return n6_prev \
               + round(self.coefs_dict.get('k6') * n2_prev) \
               + round(self.coefs_dict.get('k6') * n4_prev)

    def get_disease_stat_array(self, people_distr_list, number_of_days):
        dots_arrays_list = [[people_distr_list[0]],
                            [people_distr_list[1]],
                            [people_distr_list[2]],
                            [people_distr_list[3]],
                            [people_distr_list[4]],
                            [people_distr_list[5]]]
        people_distr_dict = {
            'n1': people_distr_list[0],  # количество не привитых и не болевших людей
            'n2': people_distr_list[1],  # количество людей заболевших впервые
            'n3': people_distr_list[2],  # количество выздоровевших людей
            'n4': people_distr_list[3],  # количество повторно заболевших людей
            'n5': people_distr_list[4],  # количество вакцинировавшихся людей
            'n6': people_distr_list[5],  # количество умерших людей
        }
        for day_num in range(number_of_days - 1):
            n1_new = self.n1(people_distr_dict.get('n1'))
            n2_new = round(
                self.n2(people_distr_dict.get('n1'), people_distr_dict.get('n2'), people_distr_dict.get('n5')))
            n3_new = round(
                self.n3(people_distr_dict.get('n2'), people_distr_dict.get('n3'), people_distr_dict.get('n4')))
            n4_new = round(self.n4(people_distr_dict.get('n3'), people_distr_dict.get('n4')))
            n5_new = round(self.n5(people_distr_dict.get('n1'), people_distr_dict.get('n5')))
            n6_new = round(
                self.n6(people_distr_dict.get('n2'), people_distr_dict.get('n4'), people_distr_dict.get('n6')))
            new_n_list = [n1_new, n2_new, n3_new, n4_new, n5_new, n6_new]
            k = 0
            for group_name in people_distr_dict:
                people_distr_dict[group_name] = new_n_list[k]
                k += 1
            for dots_array_num in range(len(dots_arrays_list)):
                dots_arrays_list[dots_array_num].append(new_n_list[dots_array_num])
        return dots_arrays_list

    def check_coefs(self, coefs_list):
        pass
