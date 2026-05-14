from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        button6 = QPushButton("Button 6")
    
        self.layout.addWidget(button1, 0, 0)  
        self.layout.addWidget(button2, 0, 1)  
        self.layout.addWidget(button3, 1, 0, 6, 1)  
        self.layout.addWidget(button4, 1, 1)  
        self.layout.addWidget(button6, 6, 1)

if __name__ == "__main__":
    app = QApplication([])

    window = MyWindow()
    window.show()
    app.exec_()