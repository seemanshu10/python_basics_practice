import sys
from PySide2.QtWidgets import QApplication, QWidget, QScrollBar, QVBoxLayout
from PySide2.QtCore import Qt

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QScrollBar Example")

        layout = QVBoxLayout()
        scroll_v = QScrollBar(Qt.Vertical, self) 
        scroll_v.setMinimum(0)
        scroll_v.setMaximum(100)
        scroll_v.setValue(30)
        # scroll_v.setGeometry(30, 20, 20, 100)

        scroll_h = QScrollBar(Qt.Horizontal, self)  
        scroll_h.setMinimum(0)
        scroll_h.setMaximum(100)
        scroll_h.setValue(30)
        # scroll_h.setGeometry(30, 20, 20, 100)

        layout.addWidget(scroll_h)
        layout.addWidget(scroll_v)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(100, 150)
    window.show()
    app.exec_()
