from PyQt6 import QtWidgets, uic

import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interface.ui", self)

        self.incButton.clicked.connect(self.increment)

        self.counter = 0
        self.update_counter()

    def increment(self):
        self.counter += 1
        self.update_counter()

    def update_counter(self):
        self.compteurField.setText(str(self.counter))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())