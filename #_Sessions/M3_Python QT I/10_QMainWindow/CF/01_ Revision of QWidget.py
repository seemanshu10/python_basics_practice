from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Simple QWidget Window")

        # Initialize layout
        layout = QVBoxLayout()

        # Add a button
        button = QPushButton("Click Me")
        layout.addWidget(button)

        # Set layout to the window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])

    # Create and show the window
    window = SimpleWindow()
    window.show()

    app.exec_()