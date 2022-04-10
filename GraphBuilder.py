import numpy as np
import matplotlib.pyplot as plt
import time


class GraphBuilder:
    @staticmethod
    def build_animated_graphs(dots_array, speed, points_num):
        """
            Принимает на вход массив вида [[a0, a1, a2, ...], [b0, b1, b2, ...], ...]
            Где a0, b0, ... - значения графиков a, b, ... в нулевой момент времени и тд
            Строит анимированные графики
            Скорость анимирования прямопропорциональна значению 'speed'
        """

        x_left_lim = 0
        x_right_lim = 10
        y_top_lim = 0
        for ar in dots_array:
            y_top_lim += ar[0]
        plt.xlim(x_left_lim, x_right_lim), plt.ylim(0, y_top_lim)
        points_list = list(range(0, points_num))
        colors_list = ['red', 'blue', 'green', 'orange', 'purple', 'black']
        color_num = 0
        for array in dots_array:
            plt.plot(points_list, array, color=colors_list[color_num])
            color_num += 1

        plt.ion()
        plt.show()
        for x in range(points_num - 10):
            time.sleep(1 / speed)
            plt.xlim(x_left_lim + x, x_right_lim + x)
            plt.draw()

            plt.gcf().canvas.flush_events()

        plt.xlim(0, points_num)
        plt.draw()
        plt.gcf().canvas.flush_events()
        plt.ioff()
        plt.show()
