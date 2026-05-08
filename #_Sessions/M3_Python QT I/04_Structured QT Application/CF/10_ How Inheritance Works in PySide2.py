import sys
from PySide2.QtWidgets import QApplication, QPushButton

class MyButton(QPushButton):
    def __init__(self, label):
        super().__init__(label)                     # Inherits constructor
        self.clicked.connect(self.on_click)         # Signal from QObject

    def on_click(self):
        print(f"Button '{self.text()}' was clicked!")  # Method from QPushButton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    button = MyButton("Click Me")
    button.resize(200, 50)        # Method from QWidget
    button.show()                 # Method from QWidget
    sys.exit(app.exec_())