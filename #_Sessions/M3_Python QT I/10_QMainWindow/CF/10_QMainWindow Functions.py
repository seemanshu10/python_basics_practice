import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("QMainWindow Functions Demo")

        # Set window position and size
        self.setGeometry(100, 100, 800, 600)

        # Set application window icon
        self.setWindowIcon(QIcon("fire.jpg"))

        # Resize window 
        self.resize(1024, 768)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
