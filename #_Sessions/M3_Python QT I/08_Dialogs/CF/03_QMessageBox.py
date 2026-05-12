from PySide2.QtWidgets import QApplication, QMessageBox, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Open File")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Select File", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.button.clicked.connect(self.confirm_delete)

    def confirm_delete(self):
        response = QMessageBox.question(
            None,
            "Delete File",
            "Are you sure you want to delete this file?"
        )

        if response == QMessageBox.Yes:
            print("User confirmed deletion")
        else:
            print("User canceled")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
