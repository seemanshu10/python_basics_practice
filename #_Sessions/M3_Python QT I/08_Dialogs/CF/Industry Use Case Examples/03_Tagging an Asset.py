from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Tag Asset with Category")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Tag Asset", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.button.clicked.connect(self.select_category)

    def select_category(self):
        categories = ["Environment", "Character", "FX", "Props", "Vehicles"]
        tag, ok = QInputDialog.getItem(
            self,
            "Tag Asset",
            "Select asset category:",
            categories,
            0,
            False
        )
        if ok:
            print("Selected category:", tag)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
