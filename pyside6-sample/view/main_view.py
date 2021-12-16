from PySide6.QtWidgets import QMainWindow

from ui.compiled.main_window import Ui_thing


class View(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_thing()
        self.ui.setupUi(self)

        self.ui.COOLBUTTON.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.ui.COOLBUTTON.setText("HELLO")

        
