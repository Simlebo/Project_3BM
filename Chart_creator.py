from datetime import datetime
from unicodedata import name

from PyQt6 import QtCore, QtWidgets, uic
import sqlite3
import sys

class Chart_creator(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/Chart_creator.ui"
        uic.loadUi(ui_path, self)

        self.setWindowTitle("Chart Creator")
        self.combobox()
        
        self.Place_order.clicked.connect(self.place_chart)
        self.Exit_menu.clicked.connect(self.back_to_main_menu)
        self.Show_price.clicked.connect(self.show_price)


    def show_price(self):
        from dB_3BM_Project import select_product
        total_price = 0
        for i in range(1,9):
            combo = getattr(self, f"spinBox_{i}")
            if combo.value() != 0:
                product_id = getattr(self, f"comboBox_{i}").currentData()
                number = getattr(self, f"spinBox_{i}").value()
                rows = select_product(f"product_id = {product_id}")
                price = float([x[1] for x in rows][0])
                total_price += price * number
        self.Total_price.setText(f"Total price: {total_price}€")
    
    def combobox(self):
        from dB_3BM_Project import select_product
        rows = select_product("")
        
        for product_id, price,price_brut,name in rows:
            self.comboBox_8.addItem(name, product_id)
            self.comboBox_7.addItem(name, product_id)
            self.comboBox_6.addItem(name, product_id)
            self.comboBox_5.addItem(name, product_id)
            self.comboBox_4.addItem(name, product_id)
            self.comboBox_3.addItem(name, product_id)
            self.comboBox_2.addItem(name, product_id)
            self.comboBox_1.addItem(name, product_id)
            self.comboBox_9.addItem(name, product_id)


    def place_chart(self):
        from dB_3BM_Project import insert_order_details
        from dB_3BM_Project import insert_customer
        from dB_3BM_Project import insert_customer_order
        from dB_3BM_Project import select_order_details_number
        from dB_3BM_Project import select_customer_number
        from dB_3BM_Project import select_customer_order_number
        from dB_3BM_Project import select_customer

        rows_order= select_customer_order_number()
        rows_order = float([x[0] for x in rows_order][0])
        order_id = rows_order + 1


        rows_customers = select_customer_number()
        rows_customers = float([x[0] for x in rows_customers][0])

        rows = select_customer("")

        for account_number in rows:

            if self.Edit_Account_number.toPlainText() not in account_number:
                customer_id = rows_customers + 1
                name = self.Edit_first_name.toPlainText() + " " + self.Edit_last_name.toPlainText()
                account_number = self.Edit_Account_number.toPlainText()
                insert_customer(customer_id,order_id,name,account_number)
                break
        
        rows_customers = select_customer_number()
        customer_id = float([x[0] for x in rows_customers][0])
        insert_customer_order(order_id,customer_id,datetime.now())

        for i in range(1,9):
            combo = getattr(self, f"spinBox_{i}")
            if combo.value() != 0:
                product_id = getattr(self, f"comboBox_{i}").currentData()
                number = getattr(self, f"spinBox_{i}").value()
                rows_order_details = select_order_details_number()
                rows_order_details = float([x[0] for x in rows_order_details][0])
                order_detail_id = rows_order_details + 1
            insert_order_details(order_detail_id,order_id,product_id,number)
        
        self.Edit_first_name.clear()
        self.Edit_last_name.clear()
        self.Edit_Account_number.clear()
        for i in range(1,9):
            combo = getattr(self, f"spinBox_{i}")
            combo.setValue(0)

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