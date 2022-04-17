import matplotlib.pyplot as plt
import time


class GraphBuilder:
    @staticmethod
    def build_animated_graphs(dots_array, speed, passes_num, graphs_names_list=None):
        """
            Принимает на вход массив вида [[a0, a1, a2, ...], [b0, b1, b2, ...], ...]
            Где a0, b0, ... - значения графиков a, b, ... в нулевой момент времени и тд
            Строит анимированные графики
            Скорость анимирования прямопропорциональна значению 'speed'
            graphs_names_list хранит обозначения для графиков
        """

        x_left_lim = 0
        x_right_lim = 10
        y_top_lim = 0
        for ar in dots_array:
            y_top_lim += ar[0]
        fig, ax = plt.subplots()
        ax.set_xlim(x_left_lim, x_right_lim), plt.ylim(0, y_top_lim)

        points_list = list(range(0, passes_num))
        colors_list = ['red', 'blue', 'green', 'orange', 'purple', 'magenta', 'cyan', 'yellow']
        if len(colors_list) < len(dots_array):
            for i in range(len(dots_array) - len(colors_list)):
                colors_list.append('black')
        color_num = 0
        for array in dots_array:
            if graphs_names_list is not None:
                ax.plot(points_list, array, color=colors_list[color_num], label=graphs_names_list[color_num])
                ax.legend()
            else:
                ax.plot(points_list, array, color=colors_list[color_num])
            color_num += 1

        plt.ion()
        plt.show()
        for x in range(passes_num - 10):
            time.sleep(1 / speed)
            ax.set_xlim(x_left_lim, x_right_lim + x)
            fig.canvas.draw()
            fig.canvas.flush_events()

        ax.set_xlim(0, passes_num)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.ioff()
        plt.show()
