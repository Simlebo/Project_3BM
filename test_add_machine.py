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
        self.combobox()

        self.Enter_machine.clicked.connect(self.add_machine_to_db)
        self.Exit_main_menu.clicked.connect(self.back_to_main_menu)
    
    def combobox(self):
        self.Agreed_machinist.addItem("Option 1")
        self.Agreed_machinist.addItem("Option 2")
        self.Agreed_machinist.addItem("11")

    def add_machine_to_db(self):
        machine_id = self.Machine_name.toPlainText()
        #machine_consumption = self.Machine_consumption.value()
        #user_id = self.Agreed_machinist.currentText()

        from dB_3BM_Project import insert_machine
        insert_machine(machine_id, user_id, machine_consumption)


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
