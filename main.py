import MyWin
from PyQt5 import QtWidgets
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin.MyWin()
    myapp.show()
    sys.exit(app.exec_())