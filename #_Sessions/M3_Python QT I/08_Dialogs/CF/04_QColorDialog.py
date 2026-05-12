from PySide2.QtWidgets import QApplication, QColorDialog, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Color Picker")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Select File", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.button.clicked.connect(self.pick_color)

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print(f"Selected color: {color.name()}")
            print(f"RGB: {color.red()}, {color.green()}, {color.blue()}")
            print(f"Alpha: {color.alpha()}")
            print(f"HSL: {color.hue()}, {color.saturation()}, {color.lightness()}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
