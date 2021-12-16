import sys


from PySide6.QtWidgets import QApplication


from view.main_view import View



if __name__ == "__main__":

    app = QApplication(sys.argv)
    view = View()
    view.show()
    sys.exit(app.exec())


    
