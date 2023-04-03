# ch 4.2.1 main.py

# add library which needs for the application
import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QMessageBox) # QMessageBox : MessageBox Widget
from PyQt5.QtGui import QIcon   # library to add icon

class Calculator(QWidget):  # define a class inherited QWidget class

    def __init__(self):
        super().__init__()  # initialize QWidget parent class
        self.initUI()   # initialize remains in initUI function

    def initUI(self):
        self.btn1 = QPushButton('Message', self)    # add button
        self.btn1.clicked.connect(self.activateMessage) # connect handler function when button clicked

        vbox=QVBoxLayout()  # create vertical layout widget
        vbox.addStretch(1)  # empty space
        vbox.addWidget(self.btn1)   # button location
        vbox.addStretch(1)  # empty space

        self.setLayout(vbox)    # empty space - button - empty space

        self.setWindowTitle('Calculator')   # sete the window title
        self.setWindowIcon(QIcon('icon.png'))   # add window icon
        self.resize(256, 256)   # window size
        self.show() # call for window display

    def activateMessage(self): # function when button clicked: Message Box output
        QMessageBox.information(self, "information", "Button clicked!")


if __name__ == '__main__':  # pyqt needs 1 QApplication per appplication
    app = QApplication(sys.argv)    # create QApplication instance
    view = Calculator() # create Calculator window instance
    sys.exit(app.exec_())   # loop for application event handling