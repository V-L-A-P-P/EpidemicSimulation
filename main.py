class EquationsSimulator:
    @staticmethod
    def N1(n1_prev, k1, v):
        return n1_prev - k1 * n1_prev - v * n1_prev
    @staticmethod
    def N2(n1_prev, n2_prev, n5_prev, k1, k2, k5, k6):
        return n2_prev + k1 * n1_prev - k2 * n2_prev + k5 * n5_prev - k6 * n2_prev
    @staticmethod
    def N3(n2_prev, n3_prev, n4_prev, k2, k3, k4):
        return n3_prev + k2 * n2_prev - k3 * n3_prev + k4 * n4_prev
    @staticmethod
    def N4(n3_prev, n4_prev, k3, k4, k6):
        return n4_prev - k4 * n4_prev + k3 * n3_prev - k6 * n4_prev
    @staticmethod
    def N5(n1_prev, n5_prev, k5, v):
        return n5_prev + v * n1_prev - k5 * n5_prev
    @staticmethod
    def N6(n2_prev, n4_prev, n6_prev, k6):
        return n6_prev + k6 * n2_prev + k6 * n4_prev


class StatisticCalculator:  # Класс принимающию на вход ко - ны.
    def __init__(self):
        self.k1 = 0.2
        self.k2 = 0.2
        self.k3 = 0.2
        self.k4 = 0.2
        self.k5 = 0.2
        self.k6 = 0.2
        self.v = 0.2
        
    def set_coefs(self):
        self.k1 = int(input())
        self.k2 = int(input())
        self.k3 = int(input())
        self.k4 = int(input())
        self.k5 = int(input())
        self.k6 = int(input())
        self.v = int(input())
        
    def calculate_disease_stat(self, number_of_people, number_of_days):
        n1 = number_of_people  # Незаболевшие, непривитые
        n2 = 0                 # Заболевшие впервые
        n3 = 0                 # Выздоровевшие
        n4 = 0                 # Повторно заболевшие
        n5 = 0                 # Вакцинировавшиеся
        n6 = 0                 # Умершие
        #self.set_coefs()
        for i in range(number_of_days):
            self.print_interm_results(i, n1, n2, n3, n4, n5, n6)
            n1 = round(EquationsSimulator.N1(n1, self.k1, self.v))
            n2 = round(EquationsSimulator.N2(n1, n2, n5, self.k1, self.k2, self.k5, self.k6))
            n3 = round(EquationsSimulator.N3(n2, n3, n4, self.k2, self.k3, self.k4))
            n4 = round(EquationsSimulator.N4(n3, n4, self.k3, self.k4, self.k6))
            n5 = round(EquationsSimulator.N5(n1, n5, self.k5, self.v))
            n6 = round(EquationsSimulator.N6(n2, n4, n6, self.k6))


    def print_interm_results(self, day, n1, n2, n3, n4, n5, n6):
        print(day)
        print(f'n1 : {n1}')
        print(f'n2 : {n2}')
        print(f'n3 : {n3}')
        print(f'n4 : {n4}')
        print(f'n5 : {n5}')
        print(f'n6 : {n6}')
        print(f'Check sum :  {n1 + n2 + n3 + n4 + n5 + n6}')
        print('---')

class GraphBuilder:
    pass


if __name__ == "__main__":
    stat_calculator = StatisticCalculator()
    stat_calculator.calculate_disease_stat(100, 10)