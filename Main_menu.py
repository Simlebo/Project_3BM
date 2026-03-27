from PyQt6 import QtCore, QtWidgets, uic
import sqlite3
import sys

class Main_menu(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/Main_menu.ui"
        ui_file_info = QtCore.QFileInfo(ui_path) #Crée un objet qui contient des informations du path car .exists() a besoin d'un objet QFileInfo pour vérifier l'existence du fichier
        if not ui_file_info.exists(): 
            print(f"Error: UI file not found at {ui_path}") #Renvois une Error si le fichier n'existe pas
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Add Machine")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Main_menu()
    window.show()
    sys.exit(app.exec())