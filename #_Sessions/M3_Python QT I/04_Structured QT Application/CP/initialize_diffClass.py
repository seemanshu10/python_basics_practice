import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Structured Example")

        self.main_layout = QVBoxLayout()

        self.label = QLabel("Click the button to update this text.")
        self.button = QPushButton("Click Me")

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.button)

        self.button.setToolTip("This is a button!")
        self.button.clicked.connect(self.on_button_clicked)

        self.setLayout(self.main_layout)

    def on_button_clicked(self):
        self.label.setText("Button Triggered")

class WrapperWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Customized Window Example")

        self.mainLayout = QVBoxLayout()

        self.header = QLabel("This is a tool using MainWindow UI below")
        self.mainLayout.addWidget(self.header)

        self.main_ui = MainWindow()
        self.mainLayout.addWidget(self.main_ui)

        # Override button behavior
        self.main_ui.button.clicked.disconnect()
        self.main_ui.button.clicked.connect(self.on_button_clicked)

        self.setLayout(self.mainLayout)

    def on_button_clicked(self):
        self.main_ui.label.setText("Customized Action Triggered!")
        print("Custom Behaviour executed!")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WrapperWindow()
    window.resize(300, 200)
    window.show()

    sys.exit(app.exec_())