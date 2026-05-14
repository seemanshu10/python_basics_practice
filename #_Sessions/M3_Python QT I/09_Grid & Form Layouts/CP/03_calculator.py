from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class GridWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.main_layout = QGridLayout()
        # create buttons 
        self.createwidgets()

        self.setLayout(self.main_layout)


    def createwidgets(self):

        # create biutton widgets 
        button1 = QPushButton("Cls")
        button2 = QPushButton("Bck")
        button3 = QPushButton("Close")
        button4 = QPushButton("7")
        button5 = QPushButton("8")
        button6 = QPushButton("9")
        button7 = QPushButton("/")
        button8 = QPushButton("4")
        button9 = QPushButton("5")
        button10 = QPushButton("6")
        button11 = QPushButton("*")
        button12 = QPushButton("1")
        button13 = QPushButton("2")
        button14 = QPushButton("3")
        button15 = QPushButton("-")
        button16 = QPushButton("0")
        button17 = QPushButton(".")
        button18 = QPushButton("=")
        button19 = QPushButton("+")
        
        # add Button in rows 
        self.main_layout.addWidget(button1, 0, 0)
        self.main_layout.addWidget(button2, 0, 1)
        self.main_layout.addWidget(button3, 0, 3) 
        self.main_layout.addWidget(button4, 1, 0)
        self.main_layout.addWidget(button5, 1, 1)  
        self.main_layout.addWidget(button6, 1, 2)
        self.main_layout.addWidget(button7, 1, 3)

        self.main_layout.addWidget(button8, 2, 0)
        self.main_layout.addWidget(button9, 2, 1)  
        self.main_layout.addWidget(button10, 2, 2)
        self.main_layout.addWidget(button11, 2, 3)

        self.main_layout.addWidget(button12, 3, 0)
        self.main_layout.addWidget(button13, 3, 1)  
        self.main_layout.addWidget(button14, 3, 2)
        self.main_layout.addWidget(button15, 3, 3)

        self.main_layout.addWidget(button16, 4, 0)
        self.main_layout.addWidget(button17, 4, 1)
        self.main_layout.addWidget(button18, 4, 2)
        self.main_layout.addWidget(button19, 4, 3)

if __name__ == "__main__":

    app = QApplication()

    window = GridWindow()
    window.show()

    app.exec_()