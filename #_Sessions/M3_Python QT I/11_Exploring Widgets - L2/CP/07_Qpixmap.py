import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPixmap Example")
        
        pixmap = QPixmap("sample_image.jpg")  # Replace with an actual image path

        label = QLabel()
        label.setPixmap(pixmap)
        label.setScaledContents(True)  # Optional: scale the image to fit label size

        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 300)
    window.show()
    app.exec_()

