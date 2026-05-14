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
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Spanning Button")
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")
        button6 = QPushButton("Button 6")

        # add Button in rows 
        self.main_layout.addWidget(button1, 0, 0)
        self.main_layout.addWidget(button2, 0, 1)
        self.main_layout.addWidget(button3, 1, 0, 1, 6) # spans 1 row 2 
        self.main_layout.addWidget(button4, 2, 1)
        self.main_layout.addWidget(button5, 2, 0, 6, 1)  
        self.main_layout.addWidget(button6, 6, 3)

if __name__ == "__main__":

    app = QApplication()

    window = GridWindow()
    window.show()

    app.exec_()