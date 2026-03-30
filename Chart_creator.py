from datetime import datetime
from unicodedata import name

from PyQt6 import QtCore, QtWidgets, uic
import sqlite3
import sys
import pandas as pd

from dB_3BM_Project import select_customer_order

import start_time

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
        from dB_3BM_Project import select_product, select_fabrication_step, select_machine
        total_price = 0
        total_elec_cost = 0
        
        now = datetime.now()
        selected_time = self.comboBox_11.currentText()
        hour, minute = map(int, selected_time.split(':'))
        start_datetime = datetime(now.year, now.month, now.day, hour, minute, 0)
        if start_datetime < now:
            start_datetime = start_datetime.replace(day=now.day + 1) #Si la journée est finie le calcule prendras le pris de demain

        base_time = pd.Timestamp(start_datetime, tz='Europe/Brussels')
        
        current_time_offset = 0
        
        for i in range(1,9):
            combo = getattr(self, f"spinBox_{i}")
            if combo.value() != 0:
                product_id = getattr(self, f"comboBox_{i}").currentData()
                number = getattr(self, f"spinBox_{i}").value()
                rows = select_product(f"product_id = {product_id}")
                price = float([x[1] for x in rows][0])
                total_price += price * number
                
                # Get fabrication steps for this product, ordered by step
                fab_rows = select_fabrication_step(f"product_id = {product_id} ORDER BY fabrication_step")
                for fab_row in fab_rows:
                    machine_id = fab_row[2]
                    time_min = fab_row[4]  # time per unit
                    duration = time_min * number  # total time for this step
                    
                    mach_rows = select_machine(f"machine_id = {machine_id}")
                    if mach_rows:
                        consumption = float(mach_rows[0][2]) 
                        
                        from daily_elec_price import get_average_electricity_price_over_period
                        avg_price = get_average_electricity_price_over_period(current_time_offset, duration, base_time)
                        
                        if avg_price is not None:
                            energy_kwh = consumption * (duration / 60)
                            cost = energy_kwh * (avg_price / 1000)
                            total_elec_cost += cost
                    
                    current_time_offset += duration

        if current_time_offset > 0:
            from daily_elec_price import get_average_electricity_price
            overall_avg_price = get_average_electricity_price(current_time_offset, base_time)
            self.Total_price.setText(f"Total price: {total_price:.2f}€\nElectricity cost: {total_elec_cost:.2f}€\nOverall average electricity price: {overall_avg_price:.2f} €/MWh")
        else:
            self.Total_price.setText(f"Total price: {total_price:.2f}€")
    
    def combobox(self):
        from dB_3BM_Project import select_product
        rows = select_product("")
        
        for product_id, price,price_brut,name in rows:
            self.comboBox_1.addItem(f"{name} - {price}€", product_id)
            self.comboBox_2.addItem(f"{name} - {price}€", product_id)
            self.comboBox_3.addItem(f"{name} - {price}€", product_id)
            self.comboBox_4.addItem(f"{name} - {price}€", product_id)
            self.comboBox_5.addItem(f"{name} - {price}€", product_id)
            self.comboBox_6.addItem(f"{name} - {price}€", product_id)
            self.comboBox_7.addItem(f"{name} - {price}€", product_id)
            self.comboBox_8.addItem(f"{name} - {price}€", product_id)
        
        slots = start_time.gen_slot()
        for slot in slots:
            self.comboBox_11.addItem(slot)


    def place_chart(self):
        from dB_3BM_Project import insert_order_details
        from dB_3BM_Project import insert_customer
        from dB_3BM_Project import insert_customer_order
        from dB_3BM_Project import select_order_details_number
        from dB_3BM_Project import select_customer_number
        from dB_3BM_Project import select_customer_order_number
        from dB_3BM_Project import select_customer
        from dB_3BM_Project import select_order_details
        from dB_3BM_Project import select_fabrication_step


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
        
        from dB_3BM_Project import select_product
        total_time = 0
        for i in range(1,9):
            combo = getattr(self, f"spinBox_{i}")
            if combo.value() != 0:
                product_id = getattr(self, f"comboBox_{i}").currentData()
                rows = select_fabrication_step(f"product_id = {product_id}")
                time = sum(rows[4] for rows in rows)   
                number = getattr(self, f"spinBox_{i}").value()
                total_time += time * number

        now = datetime.now()
        selected_time = self.comboBox_11.currentText()
        hour, minute = map(int, selected_time.split(':'))
        start_time = datetime(now.year, now.month, now.day, hour, minute, 0)
        if start_time < now:
            start_time = start_time.replace(day=now.day + 1)
        deadline = datetime(start_time.year, start_time.month, start_time.day, 17, 0, 0)
        time_available = (deadline - start_time).total_seconds() / 60

        if total_time > time_available:
            from alerte_timing import AlerteTiming
            dialog = AlerteTiming()
            result = dialog.exec()
            if result == QtWidgets.QDialog.DialogCode.Rejected:  # Assuming Cancel is Reject
                return



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