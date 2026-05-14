from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Create buttons
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Spanning Button")
        button4 = QPushButton("Button 4")

        # Add buttons to the grid layout
        self.layout.addWidget(button1, 0, 0)  # Row 0, Column 0
        self.layout.addWidget(button2, 0, 1)  # Row 0, Column 1
        self.layout.addWidget(button3, 1, 0, 2, 2)  
        self.layout.addWidget(button4, 2, 0) 

if __name__ == "__main__":
    app = QApplication([])

    window = MyWindow()
    window.show()

    app.exec_()