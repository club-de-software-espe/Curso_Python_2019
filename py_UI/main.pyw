from windows_views import WindowMain
from PyQt5.QtWidgets import QApplication
import sys


def run():
    app = QApplication(sys.argv)
    win_main = WindowMain()
    win_main.show()
    app.exec_()

if __name__ == "__main__":
    run()
