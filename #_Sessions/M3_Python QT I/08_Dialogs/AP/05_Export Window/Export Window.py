# Save an Exported Preview
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Save File")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Choose Save Location", self)
        self.button.setGeometry(100, 50, 200, 40)

        self.status_label = QLabel("No File Selected", self)
        self.status_label.setGeometry(20, 100, 250, 50)
        self.button.clicked.connect(self.save_file_dialog)

    def save_file_dialog(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "video File (*.mov, *.mp4)"
        )
        if file_path:
            print(f"File to save: {file_path}")
            self.status_label(f"Export Path: {file_path}")
        else:
            print("No file choosen")
            self.status_label(f"No file choosen")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
