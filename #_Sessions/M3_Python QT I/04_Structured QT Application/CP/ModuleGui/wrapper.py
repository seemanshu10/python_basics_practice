import sys
from PySide2. QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from mainWindow import MainWindow

class WrapperWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("Structured Example") 
        self.mainLayout = QVBoxLayout()

        self.header = QLabel("This is a tool using mainWindow UI below")
        self.mainLayout.addWidget(self.header)
        
        self.main_ui = MainWindow()
        self.mainLayout.addWidget(self.main_ui)

        self.setLayout(self.mainLayout)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WrapperWindow()
    window.resize(300, 200)
    window.show()

    sys.exit(app.exec_())