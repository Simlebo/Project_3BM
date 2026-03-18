from PyQt6 import QtCore, QtWidgets, uic
import sys
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/interface.ui"
        uic.loadUi(ui_path, self)

        self.pushButton.clicked.connect(self.say_hello)
    def say_hello(self):
        self.label.setText("Hello, World!")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()   
    sys.exit(app.exec())