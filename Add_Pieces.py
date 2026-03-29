from PyQt6 import QtCore, QtWidgets, uic
import sqlite3
import sys

from dB_3BM_Project import insert_fabrication_step

class Add_Pieces(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/Add_Pieces.ui"
        uic.loadUi(ui_path, self)

        self.combobox()
        self.setWindowTitle("Add Pieces")
        self.Exit_Menu.clicked.connect(self.back_to_main_menu)
        self.Add_pieces.clicked.connect(self.add_pieces_to_db)
   
    def back_to_main_menu(self):
        self.close()
        from Main_menu import Main_menu
        self.create_orders = Main_menu()
        self.create_orders.show()
    
    
    def combobox(self):
        from dB_3BM_Project import select_machine
        rows = select_machine("")
        for machine_id in rows:
            self.Machine_combo_1.addItem(str(machine_id))
            self.Machine_combo_2.addItem(str(machine_id))
            self.Machine_combo_3.addItem(str(machine_id))



    def add_pieces_to_db(self):
        from dB_3BM_Project import insert_product
        from dB_3BM_Project import select_product
        from dB_3BM_Project import insert_fabrication_step
        from dB_3BM_Project import select_fabrication_step

        rows = select_product("")
        product_id = len(rows) + 1
        name = self.Piece_name.toPlainText()
        price = float(self.Piece_Price.toPlainText())
        price_brut = float(self.Piece_Price_brut.toPlainText())

        len = select_fabrication_step("")
        step_id = len + 1
        machine_id = float(self.Machine_combo_1.currentText())
        time = float(self.Time_1.toPlainText())
        step_name = self.Process_name_1.toPlainText()
        fabrication_step = 1
        insert_fabrication_step(step_id,product_id,machine_id,fabrication_step,time,step_name)
        
        if self.Process_name_2.toPlainText() != "":
            step_id = step_id + 1
            machine_id = float(self.Machine_combo_2.currentText())
            time = float(self.Time_2.toPlainText())
            step_name = self.Process_name_2.toPlainText()
            fabrication_step = fabrication_step + 1
            insert_fabrication_step(step_id,product_id,machine_id,fabrication_step,time,step_name)

        if self.Process_name_3.toPlainText() != "":
            step_id = step_id + 1
            machine_id = float(self.Machine_combo_3.currentText())
            time = float(self.Time_3.toPlainText())
            step_name = self.Process_name_3.toPlainText()
            fabrication_step = fabrication_step + 1
            insert_fabrication_step(step_id,product_id,machine_id,fabrication_step,time,step_name)                
        
        insert_product(product_id,price,price_brut,name)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Add_Pieces()
    window.show()
    sys.exit(app.exec())