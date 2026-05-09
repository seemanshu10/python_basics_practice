import sys
from PySide2. QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("Structured Example") 

        layout = QVBoxLayout()

        self.label = QLabel("Click the button to update this text.")
        layout.addWidget(self.label)

        button = QPushButton("Click Me")
        
        button.setToolTip("This is a button!")
        button.setEnabled(True)
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)

        self.setLayout(layout)

    def on_button_clicked(self):
        self.label.setText("Button Clicked")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(300, 200)
    window.show()

    sys.exit(app.exec_())