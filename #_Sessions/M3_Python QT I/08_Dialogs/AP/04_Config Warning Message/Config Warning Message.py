# Warn About Overwriting Config
from PySide2.QtWidgets import QApplication, QMessageBox, QPushButton, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Iver Write config Window")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Attempt Overwrite", self)
        self.button.setGeometry(100, 50, 200, 40)

        self.status_label = QLabel("Review Label Here", self)
        self.status_label.setGeometry(20, 100, 250, 50)

        self.button.clicked.connect(self.confirm_overwrite)

    def confirm_overwrite(self):
        response = QMessageBox.question(
            None,
            "Overwrite File",
            "Are you sure you want to delete this file?"
        )

        if response == QMessageBox.Yes:
            print("User confirmed Overwrite.")
            self.status_label.setText("User Choosen to Overwrite Config.")
        else:
            print("User declined Overwrite.")
            self.status_label.setText("User Choosen to cancel Overwrite Config.")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
