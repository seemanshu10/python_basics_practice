from PySide2.QtWidgets import QApplication, QInputDialog, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Open Input Dialog")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Open Input Dialog", self)
        self.button1 = QPushButton("Open Integer Dialog", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.button.clicked.connect(self.get_text)
        self.button1.setGeometry(100, 100, 200, 40)
        self.button1.clicked.connect(self.get_integer)

    #  --------------- Text Input Dialog ---------------
    def get_text(self):
        text, ok = QInputDialog.getText(None, "Input Dialog", "Enter your name:")
        if ok and text:
            print(f"User entered: {text}")


    # --------------- Integer Input Dialog ---------------
    def get_integer(self):
        number, ok = QInputDialog.getInt(None, "Input Dialog", "Enter a number:", min=0, max=100)
        if ok:
            print(f"User entered: {number}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
