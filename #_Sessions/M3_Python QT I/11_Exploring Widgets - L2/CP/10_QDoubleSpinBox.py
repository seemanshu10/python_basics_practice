import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox Example")
        
        self.double_spin_box = QDoubleSpinBox()
        self.double_spin_box.setRange(0.0, 100.0)
        self.double_spin_box.setValue(10.5)
        
        self.setCentralWidget(self.double_spin_box)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

