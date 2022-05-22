import MyWin  # Модуль
from PyQt5 import QtWidgets  # Модуль позволяет работать с графическим   интерфесом.
import sys  # обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.
import traceback  # предоставляет стандартный интерфейс для извлечения, форматирования и вывода на печать трассировок
# стека программ.

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin.MyWin()
        myapp.show()
        sys.exit(app.exec_())
    except Exception as _ex:
        print(traceback.format_exc())
