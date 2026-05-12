from PySide2.QtWidgets import QApplication, QFontDialog, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Font Picker")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Open Font Dialog", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.button.clicked.connect(self.pick_font)

    def pick_font(self):
        ok, font = QFontDialog.getFont()
        if ok:
            print(f"Selected font: {font.family()} at size {font.pointSize()}")
        else:
            print("Font selection canceled.")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
