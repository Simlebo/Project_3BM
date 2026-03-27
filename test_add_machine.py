from PyQt6 import QtCore, QtWidgets, uic
import sqlite3
import sys

class AddMachine(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/Add_machine.ui"
        ui_file_info = QtCore.QFileInfo(ui_path) 
        if not ui_file_info.exists(): 
            print(f"Error: UI file not found at {ui_path}") 
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Add Machine")

        self.Enter_machine.clicked.connect(self.add_machine_to_db)
        self.Exit_main_menu.clicked.connect(self.back_to_main_menu)

    def back_to_main_menu(self):
        self.close()
        from Main_menu import Main_menu
        self.create_orders = Main_menu()
        self.create_orders.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AddMachine()
    window.show()
    sys.exit(app.exec())
