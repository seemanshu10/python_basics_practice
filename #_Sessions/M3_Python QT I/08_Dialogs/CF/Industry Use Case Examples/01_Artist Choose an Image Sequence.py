from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Select Image Sequence")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Select Image", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.button.clicked.connect(self.select_image_sequence)

    def select_image_sequence(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image Sequence",
            "",
            "Images (*.exr *.png *.jpg)"
        )
        if file_path:
            print("Selected file:", file_path)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
