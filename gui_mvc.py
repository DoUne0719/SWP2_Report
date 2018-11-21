import sys
from gui_model import Model
from gui_view import View
from gui_controller import Controller
from PyQt5.QtWidgets import QApplication, QWidget

class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.model, self.controller)

        self.view.startGame()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Start()
    game.view.show()
    sys.exit(app.exec_())
