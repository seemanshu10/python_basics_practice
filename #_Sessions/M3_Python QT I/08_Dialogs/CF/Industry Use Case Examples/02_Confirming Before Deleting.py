from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Delete Temp Renders")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Delete Temp Renders", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.button.clicked.connect(self.confirm_delete)

    def confirm_delete(self):
        response = QMessageBox.question(
            self,
            "Delete Render",
            "Are you sure you want to delete the temp renders?"
        )
        if response == QMessageBox.Yes:
            print("User confirmed deletion")
        else:
            print("User cancelled")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
