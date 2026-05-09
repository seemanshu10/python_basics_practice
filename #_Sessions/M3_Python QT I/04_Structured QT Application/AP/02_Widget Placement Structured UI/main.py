# PySide2 Window with Custom Widget Placement
import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class MultiButtonGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Multi-Button PySide2 GUI")
        self.setGeometry(100, 100, 300, 200)
        self.label = QLabel("Click a button below", self)
        self.label.move(100, 80)

        self.button1 = QPushButton("Click Me", self)
        self.button1.move(100, 120)

        self.button1.clicked.connect(self.show_button)

    def show_button(self):
        self.label.setText("Button was clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    button = MultiButtonGUI()
    button.show()                
    sys.exit(app.exec_())