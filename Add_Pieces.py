from PyQt6 import QtCore, QtWidgets, uic
import sqlite3
import sys

class Add_Pieces(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/Add_Pieces.ui"
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Add Pieces")
        self.Exit_Menu.clicked.connect(self.back_to_main_menu)

    def back_to_main_menu(self):
        self.close()
        from Main_menu import Main_menu
        self.create_orders = Main_menu()
        self.create_orders.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Add_Pieces()
    window.show()
    sys.exit(app.exec())