from PySide2.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout

class SimpleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMainWindow Example")

        # Create a basic central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Add a button to the central widget
        button = QPushButton("Click Me", central_widget)

        button.clicked.connect(self.on_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(button)
        central_widget.setLayout(layout)

    def on_button_clicked(self):
        print("Button Clicked! Hello from Pyside2!")

def show_window():
    global my_window
    my_window = SimpleWindow()
    my_window.show()

show_window()