import MyWin
from PyQt5 import QtWidgets
import sys
import traceback

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin.MyWin()
        myapp.show()
        sys.exit(app.exec_())
    except Exception as _ex:
        print(traceback.format_exc())
