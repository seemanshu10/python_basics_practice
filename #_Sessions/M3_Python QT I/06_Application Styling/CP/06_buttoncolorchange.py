import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class ButtonClickedApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Color Toggle") 
        self.init_UI()

    def init_UI(self):

        self.main_layout = QVBoxLayout()

        self.button1 = QPushButton("Click Me!") 
        # self.button1.setStyleSheet('color: green; border-radius: red;')
    
        self.main_layout.addWidget(self.button1)

        self.setLayout(self.main_layout)

        self.button1.clicked.connect(self.toggle_bottom_color)

    def toggle_bottom_color(self):

        current_style = self.button1.styleSheet()

        if 'green' in current_style:
            self.button1.setStyleSheet('background-color: red; color: white;')
        else:
            self.button1.setStyleSheet('background-color: green; color: white;')

        print("Button Clicked!")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = ButtonClickedApp()
    window.resize(200, 300)
    window.show()

    sys.exit(app.exec_())