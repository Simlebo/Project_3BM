from PyQt6 import QtCore, QtWidgets, uic
import sqlite3
import sys

class Main_menu(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/Main_menu.ui"
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Main Menu")
        self.Add_machine.clicked.connect(self.add_machine)
        self.Add_pieces.clicked.connect(self.add_pieces)
        self.Create_order.clicked.connect(self.Chart_creator)
        self.Add_machinist.clicked.connect(self.Machinist_creator)

    def add_machine(self):
        self.close()
        from test_add_machine import AddMachine
        self.create_orders = AddMachine()
        self.create_orders.show()
    
    def add_pieces(self):
        self.close()
        from Add_Pieces import Add_Pieces
        self.create_orders = Add_Pieces()
        self.create_orders.show()   

    def Chart_creator(self):
        self.close()
        from Chart_creator import Chart_creator
        self.create_orders = Chart_creator()
        self.create_orders.show()   

    def Machinist_creator(self):
        self.close()
        from Machinist_creator import Machinist_creator
        self.create_orders = Machinist_creator()
        self.create_orders.show()
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Main_menu()
    window.show()
    sys.exit(app.exec())