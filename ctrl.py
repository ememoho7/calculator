# ch 6.2.2 ctrl.py
class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):    # add calculate method
        pass

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)  # bind button1
        self.view.btn2.clicked.connect(self.view.clearMessage)