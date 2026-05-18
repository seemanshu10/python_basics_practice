import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFontDialog, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog Example")
        
        self.button = QPushButton("Choose Font")
        self.button.clicked.connect(self.open_font_dialog)
        self.setCentralWidget(self.button)

    def open_font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            print(font.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
