# ch 6.2.1 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout,
                             QLineEdit, QComboBox) # add QLineEdit, QComboBox 
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore # add module

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.le1 = QLineEdit('0', self) # add line edit1
        self.le1.setAlignment(QtCore.Qt.AlignRight) # set align of line edit1

        self.le2 = QLineEdit('0', self) # add line edit2
        self.le2.setAlignment(QtCore.Qt.AlignRight) # set align of line edit2

        self.cb = QComboBox(self) # add combo box
        self.cb.addItems(['+', '-', '*', '/']) # add items to combo box (use as operators)

        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        self.btn1 = QPushButton('Message', self)
        self.btn2 = QPushButton('Clear', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)   # place hbox_formular
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self):
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):
        self.te1.clear()