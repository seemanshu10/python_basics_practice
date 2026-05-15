from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class GridWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.main_layout = QGridLayout()
        self.createwidgets()
        self.setLayout(self.main_layout)

    def createwidgets(self):

        # create button widgets 
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("button 3")
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")
        button6 = QPushButton("Button 6")
        button7 = QPushButton("Button 7")
        button8 = QPushButton("Button 8")

        # add buttons in rows 
        self.main_layout.addWidget(button1, 0, 0)
        self.main_layout.addWidget(button2, 0, 1)
        self.main_layout.addWidget(button3, 0, 2)

        self.main_layout.addWidget(button4, 1, 0)
        self.main_layout.addWidget(button5, 1, 1, 1, 2)
        self.main_layout.addWidget(button6, 2, 0)
        self.main_layout.addWidget(button7, 2, 1, 2, 2)
        self.main_layout.addWidget(button8, 3,0)

        # self.main_layout.setRowStretch(2, 2)

# TODO: create as capture

if __name__ == "__main__":

    app = QApplication()

    window = GridWindow()
    window.show()

    app.exec_()