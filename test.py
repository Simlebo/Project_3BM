
import sys
import matplotlib
matplotlib.use('QtAgg')
from matplotlib import container
import matplotlib.dates as mdates
from PyQt6 import QtCore, QtWidgets, uic
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

    def plot_price_data(self, data):
        self.axes.cla()

        self.axes.step(data.index, data.values, where='mid', color='teal', linewidth=2)

        self.axes.xaxis.set_major_locator(mdates.HourLocator(interval=2))
        self.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        self.axes.figure.autofmt_xdate(rotation=0, ha='center')

        self.axes.set_title(f'Belgian Electricity Prices from 'f'{data.index[0].strftime("%d/%m/%Y")} to 'f'{data.index[-1].strftime("%d/%m/%Y")}')
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Price (€/MWh)')
        self.axes.grid(True, linestyle='--', alpha=0.4)

        self.axes.figure.tight_layout()
        self.draw()


class Electric_price(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/electricprice.ui"
        uic.loadUi(ui_path, self)

        self.pushButton.clicked.connect(self.back_to_main_menu)
        self.pushButton_2.clicked.connect(self.calc_price)

        sc = MplCanvas(self, width=5, height=4, dpi=100)

        from daily_elec_price import create_entsoe_price_plot
        data = create_entsoe_price_plot()
        sc.plot_price_data(data)
    
        layout = QtWidgets.QVBoxLayout(self.plotLayout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(sc)

    def calc_price(self):
        from dB_3BM_Project import select_electricity_price
        rows = select_electricity_price("price < 95")
        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(container)

        for date, price in rows:
            label_1 = QtWidgets.QLabel(f"Price: {price} €/MWh, Date: {date}")
            layout.addWidget(label_1)


        self.scrollArea.setWidget(container)
        self.scrollArea.setWidgetResizable(True)

    def back_to_main_menu(self):
        from dB_3BM_Project import insert_electricity_price
        from daily_elec_price import create_entsoe_price_plot
        data = create_entsoe_price_plot()

        for timestamp, price in data.items():
            insert_electricity_price(timestamp, price)

        self.close()
        from Main_menu import Main_menu
        self.create_orders = Main_menu()
        self.create_orders.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Electric_price()
    window.show()
    sys.exit(app.exec())