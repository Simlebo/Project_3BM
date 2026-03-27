from PyQt6 import QtCore, QtWidgets, uic
import sqlite3
import sys

class Chart_creator(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/Chart_creator.ui"
        uic.loadUi(ui_path, self)
        self.Exit_menu.clicked.connect(self.back_to_main_menu)
    
    def back_to_main_menu(self):
        self.close()
        from Main_menu import Main_menu
        self.create_orders = Main_menu()
        self.create_orders.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Chart_creator()
    window.show()
    sys.exit(app.exec())