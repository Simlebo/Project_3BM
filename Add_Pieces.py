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
        for machine_id,user_id,consumption in rows:
            self.Machine_combo_1.addItem(str(machine_id), user_id)
            self.Machine_combo_2.addItem(str(machine_id), user_id)
            self.Machine_combo_3.addItem(str(machine_id), user_id)



    def add_pieces_to_db(self):
        from dB_3BM_Project import insert_product
        from dB_3BM_Project import select_product
        from dB_3BM_Project import insert_fabrication_step
        from dB_3BM_Project import select_fabrication_step_number

        rows = select_product("")
        product_id = len(rows) + 1
        name = self.Piece_name.toPlainText()
        price = float(self.Piece_Price.toPlainText())
        price_brut = float(self.Piece_Price_brut.toPlainText())
        insert_product(product_id,price,price_brut,name)

        
        
        rows_step = select_fabrication_step_number()
        rows_step = float([x[0] for x in rows_step][0])
        step_id_1 = rows_step + 1
        machine_id_1 = float(self.Machine_combo_1.currentText())
        time_1 = float(self.Time_1.toPlainText())
        step_name_1 = self.Process_name_1.toPlainText()
        fabrication_step_1 = 1
        insert_fabrication_step(step_id_1,product_id,machine_id_1,fabrication_step_1,time_1,step_name_1)
        
        if self.Process_name_2.toPlainText() != "":
            step_id_2 = step_id_1 + 1
            machine_id_2 = float(self.Machine_combo_2.currentText())
            time_2 = float(self.Time_2.toPlainText())
            step_name_2 = self.Process_name_2.toPlainText()
            fabrication_step_2 = fabrication_step_1 + 1
            insert_fabrication_step(step_id_2,product_id,machine_id_2,fabrication_step_2,time_2,step_name_2)

        if self.Process_name_3.toPlainText() != "":
            step_id_3 = step_id_2 + 1
            machine_id_3 = float(self.Machine_combo_3.currentText())
            time_3 = float(self.Time_3.toPlainText())
            step_name_3 = self.Process_name_3.toPlainText()
            fabrication_step_3 = fabrication_step_2 + 1
            insert_fabrication_step(step_id_3,product_id,machine_id_3,fabrication_step_3,time_3,step_name_3)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Add_Pieces()
    window.show()
    sys.exit(app.exec())