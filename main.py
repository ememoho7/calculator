# ch 4.2.1 main.py
import sys
from ui import View # add View class of ui.py
from ctrl import Control    # add Control class of ctrl.py
from PyQt5.QtWidgets import QApplication

def main(): # function for program excution(Application)
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View()
    Control(view = view)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()