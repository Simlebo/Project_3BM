
import sys
import matplotlib
matplotlib.use('QtAgg')
from PyQt6 import QtCore, QtWidgets, uic
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class Electric_price(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/electricprice.ui"
        uic.loadUi(ui_path, self)

        self.pushButton.clicked.connect(self.back_to_main_menu)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        layout = QtWidgets.QVBoxLayout(self.plotLayout)
        layout.addWidget(sc)

    def back_to_main_menu(self):
        self.close()
        from Main_menu import Main_menu
        self.create_orders = Main_menu()
        self.create_orders.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Electric_price()
    window.show()
    sys.exit(app.exec())