# Set Default Light Color
from PySide2.QtWidgets import QApplication, QColorDialog, QPushButton, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Set Default Light Color ")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Pick Light Color", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.status_label = QLabel("Review Label Here", self)
        self.status_label.setGeometry(20, 100, 250, 50)
        self.button.clicked.connect(self.pick_color)

    def pick_color(self):
        color = QColorDialog.getColor()
        # print(color)
        # print(dir(color))
        if color.isValid():
            color_hex = color.name()
            if color_hex != "#ffffff":

                # print(f"Selected color: {color.name()}")
                # print(f"RGB: {color.red()}, {color.green()}, {color.blue()}")
                # print(f"Alpha: {color.alpha()}")
                # print(f"HSL: {color.hue()}, {color.saturation()}, {color.lightness()}")
                self.status_label.setText(f"Light Color Set To: {color_hex}")
                self.status_label.setStyleSheet(f"color:  {color_hex}")
            else:
                print("No color chosen.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
