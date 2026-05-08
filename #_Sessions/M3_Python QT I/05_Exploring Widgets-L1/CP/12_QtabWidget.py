import sys
from PySide2.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget Example")

        tabs = QTabWidget(self)
        tab1 = QWidget()
        tab2 = QWidget()

        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Content of Tab 1"))
        tab1.setLayout(layout1)

        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Content of Tab 2"))
        tab2.setLayout(layout2)

        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")
        tabs.setGeometry(10, 10, 250, 120)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(280, 160)
    window.show()
    app.exec_()