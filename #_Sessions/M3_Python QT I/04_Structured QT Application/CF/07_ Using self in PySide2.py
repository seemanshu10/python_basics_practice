import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Two Buttons Example")
        self.resize(300, 200)

        # Button 1
        self.button1 = QPushButton("Button 1", self)
        self.button1.move(50, 50)
        self.button1.clicked.connect(self.action_button1)

        # Button 2
        self.button2 = QPushButton("Button 2", self)
        self.button2.move(150, 50)
        self.button2.clicked.connect(self.action_button2)

    def action_button1(self):
        print("Button 1 was clicked!")

    def action_button2(self):
        print("Button 2 was clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())