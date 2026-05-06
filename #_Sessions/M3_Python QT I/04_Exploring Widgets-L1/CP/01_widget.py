import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget Example")
        
        layout = QVBoxLayout()
        label = QLabel("This is a custom widget ")
        layout.addWidget(label)
        
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomWidget()
    
    window.show()
    app.exec_()