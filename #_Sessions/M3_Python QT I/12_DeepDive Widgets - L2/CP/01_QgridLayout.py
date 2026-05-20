import sys
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        
        layout = QGridLayout()
        layout.addWidget(QPushButton("Button"), 0, 0)   
        layout.addWidget(QLineEdit(), 0, 1, 1, 2)           
        layout.setRowStretch(1, 1)                       
        layout.setColumnStretch(2, 2)                        
        layout.setSpacing(10)                                
        layout.setContentsMargins(10, 10, 10, 10)  
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(250, 150)
    window.show()
    app.exec_()