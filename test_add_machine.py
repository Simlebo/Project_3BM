from PyQt6 import QtCore, QtWidgets, uic
import sqlite3
import sys

class AddMachine(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/Add_machine.ui"
        ui_file_info = QtCore.QFileInfo(ui_path) #Crée un objet qui contient des informations du path car .exists() a besoin d'un objet QFileInfo pour vérifier l'existence du fichier
        if not ui_file_info.exists(): 
            print(f"Error: UI file not found at {ui_path}") #Renvois une Error si le fichier n'existe pas
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Add Machine")

        self.Enter_machine.clicked.connect(self.add_machine_to_db)
        self.Exit_main_menu.clicked.connect(self.back_to_main_menu)

    def back_to_main_menu(self):
        self.close()
        from Main_menu import Main_menu
        self.create_orders = Main_menu()
        self.create_orders.show()

    def add_machine_to_db(self):
        machine_name = self.Machine_name.text()
        machine_type = self.Machine_type.text()
        machine_status = self.Machine_status.text()

        conn = sqlite3.connect("dB_3BM_Project.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Machines (name, type, status) VALUES (?, ?, ?)", (machine_name, machine_type, machine_status))
        conn.commit()
        conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AddMachine()
    window.show()
    sys.exit(app.exec())
