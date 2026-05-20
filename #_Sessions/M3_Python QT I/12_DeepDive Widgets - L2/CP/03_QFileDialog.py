import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog Example")
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFiles) 

        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.exec_()    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
