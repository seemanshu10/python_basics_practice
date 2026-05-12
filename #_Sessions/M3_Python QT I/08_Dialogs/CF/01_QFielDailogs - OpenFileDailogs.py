from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Open File")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Select File", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.button.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            "",
            "Images (*.png *.jpg *.exr)"
        )
        if file_path:
            print(f"Selected file: {file_path}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
