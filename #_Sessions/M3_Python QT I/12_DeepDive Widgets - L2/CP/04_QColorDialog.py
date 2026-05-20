import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QColorDialog, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog Example")
        
        self.button = QPushButton("Choose Color")
        self.button.clicked.connect(self.open_color_dialog)
        self.setCentralWidget(self.button)

    def open_color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    