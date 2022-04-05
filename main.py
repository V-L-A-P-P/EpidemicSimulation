class StatisticCalculator:
    def __init__(self):
        self.coefs_dict = {
            'k1': 0.2,  #
            'k2': 0.2,  #
            'k3': 0.2,  #
            'k4': 0.2,  #
            'k5': 0.2,  #
            'k6': 0.2,  #
            'v': 0.2    # коофицент вакцинировавшихся
        }

    def set_coefs_dict(self):
        for key in self.coefs_dict:
            print('k1 : ', end='')
            self.coefs_dict[key] = float(input())

    def n1(self, n1_prev):
        return n1_prev \
               - round(self.coefs_dict.get('k1') * n1_prev)\
               - round(self.coefs_dict.get('v') * n1_prev)

    def n2(self, n1_prev, n2_prev, n5_prev):
        return n2_prev \
               + round(self.coefs_dict.get('k1') * n1_prev) \
               - round(self.coefs_dict.get('k2') * n2_prev) \
               + round(self.coefs_dict.get('k5') * n5_prev)\
               - round(self.coefs_dict.get('k6') * n2_prev)

    def n3(self, n2_prev, n3_prev, n4_prev):
        return n3_prev \
               + round(self.coefs_dict.get('k2') * n2_prev)\
               - round(self.coefs_dict.get('k3') * n3_prev)\
               + round(self.coefs_dict.get('k4') * n4_prev)

    def n4(self, n3_prev, n4_prev):
        return n4_prev \
               - round(self.coefs_dict.get('k4') * n4_prev)\
               + round(self.coefs_dict.get('k3') * n3_prev)\
               - round(self.coefs_dict.get('k6') * n4_prev)

    def n5(self, n1_prev, n5_prev):
        return n5_prev \
               + round(self.coefs_dict.get('v') * n1_prev)\
               - round(self.coefs_dict.get('k5') * n5_prev)

    def n6(self, n2_prev, n4_prev, n6_prev):
        return n6_prev \
               + round(self.coefs_dict.get('k6') * n2_prev)\
               + round(self.coefs_dict.get('k6') * n4_prev)

    def calculate_disease_stat(self, number_of_people, number_of_days):
        groups_of_people = {
            'n1': number_of_people,  # количество не привитых и не болевших людей
            'n2': 0,                 # количество людей заболевших впервые
            'n3': 0,                 # количество выздоровевших людей
            'n4': 0,                 # количество повторно заболевшиз людей
            'n5': 0,                 # количество вакцинировавшихся людей
            'n6': 0,                 # количество умерших людей
        }
        # self.set_coefs_dict()
        for i in range(number_of_days):
            self.print_interm_results(i, groups_of_people.get('n1'),
                                      groups_of_people.get('n2'),
                                      groups_of_people.get('n3'),
                                      groups_of_people.get('n4'),
                                      groups_of_people.get('n5'),
                                      groups_of_people.get('n6'))
            n1_new = self.n1(groups_of_people.get('n1'))
            n2_new = round(self.n2(groups_of_people.get('n1'), groups_of_people.get('n2'), groups_of_people.get('n5')))
            n3_new = round(self.n3(groups_of_people.get('n2'), groups_of_people.get('n3'), groups_of_people.get('n4')))
            n4_new = round(self.n4(groups_of_people.get('n3'), groups_of_people.get('n4')))
            n5_new = round(self.n5(groups_of_people.get('n1'), groups_of_people.get('n5')))
            n6_new = round(self.n6(groups_of_people.get('n2'), groups_of_people.get('n4'), groups_of_people.get('n6')))

            new_n_list = [n1_new, n2_new, n3_new, n4_new, n5_new, n6_new]
            k = 0
            for key in groups_of_people:
                groups_of_people[key] = new_n_list[k]
                k += 1

    def print_interm_results(self, day, n1, n2, n3, n4, n5, n6):
        print(day)
        print(f'n1 : {n1}')
        print(f'n2 : {n2}')
        print(f'n3 : {n3}')
        print(f'n4 : {n4}')
        print(f'n5 : {n5}')
        print(f'n6 : {n6}')
        print(f'Check sum :  {n1 + n2 + n3 + n4 + n5 + n6}')


class GraphBuilder:
    pass


if __name__ == "__main__":
    stat_calculator = StatisticCalculator()
    stat_calculator.calculate_disease_stat(1000000, 10)
