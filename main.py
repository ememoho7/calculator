# ch 4.2.1 main.py

# add library which needs for the application
import sys

from PyQt5.QtWidgets import QApplication, QWidget   # application handler and blank GUI widget

class Calculator(QWidget):  # define a class inherited QWidget class

    def __init__(self):
        super().__init__()  # initialize QWidget parent class
        self.initUI()   # initialize remains in initUI function

    def initUI(self):
        self.setWindowTitle('Calculator')   # sete the window title
        self.resize(256, 256)   # window size
        self.show() # call for window display


if __name__ == '__main__':  # pyqt needs 1 QApplication per appplication
    app = QApplication(sys.argv)    # create QApplication instance
    view = Calculator() # create Calculator window instance
    sys.exit(app.exec_())   # loop for application event handling