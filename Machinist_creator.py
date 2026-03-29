from PyQt6 import QtCore, QtWidgets, uic
import sqlite3
import sys

class Machinist_creator(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/Machinist_creator.ui"
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Add Machinist")

        self.Enter.clicked.connect(self.add_machinist_to_db)
        self.Exit_menu.clicked.connect(self.back_to_main_menu)
    

    def add_machinist_to_db(self):
        from dB_3BM_Project import select_users
        from dB_3BM_Project import select_customer_number_users
        
        machinist_name = self.Machinist_name.toPlainText()
        machinist_email = self.Email_adress.toPlainText()

        rows = select_customer_number_users()
        rows = float([x[0] for x in rows][0])
        machinist_id = rows + 1
    

        from dB_3BM_Project import insert_users
        insert_users(machinist_id, machinist_name, machinist_email)




    def back_to_main_menu(self):
        self.close()
        from Main_menu import Main_menu
        self.create_orders = Main_menu()
        self.create_orders.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Machinist_creator()
    window.show()
    sys.exit(app.exec())