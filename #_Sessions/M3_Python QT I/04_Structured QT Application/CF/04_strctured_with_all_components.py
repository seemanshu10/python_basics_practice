import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() 

    def initUI(self):
        self.setWindowTitle("PySide2 Vertical Layout Example")

        # Create a vertical layout
        layout = QVBoxLayout()

        # Create and add a label to the layout
        self.label = QLabel("Click the button to update this text.")
        layout.addWidget(self.label)

        # Create and add a button to the layout
        button = QPushButton("Click Me")
        button.setToolTip("This is a button!")  # Set a tooltip
        button.setEnabled(True)  # Enable the button
        button.clicked.connect(self.on_button_clicked)  # Connect signal to slot
        layout.addWidget(button)

        # Set the layout for the main window
        self.setLayout(layout)

    def on_button_clicked(self):
        self.label.setText("Button clicked!")  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
