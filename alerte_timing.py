import sys
from PyQt6 import QtCore, QtWidgets, uic

class AlerteTiming(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = QtCore.QFileInfo(__file__).absolutePath() + "/alerte_timing.ui"
        uic.loadUi(ui_path, self)

        # Assuming the UI has buttonBox (QDialogButtonBox)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)