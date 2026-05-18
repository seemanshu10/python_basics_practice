import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog Example")
        
        self.button = QPushButton("Open File")
        self.button.clicked.connect(self.open_file_dialog)
        self.setCentralWidget(self.button)

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "All Files (*);;Text Files (*.txt)"
        )
        if file_name:
            print(file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
