from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Save File")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Save File As", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.button.clicked.connect(self.save_file_dialog)

    def save_file_dialog(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            print(f"File to save: {file_path}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
