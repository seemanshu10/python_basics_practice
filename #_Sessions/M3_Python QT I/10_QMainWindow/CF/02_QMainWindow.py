from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMainWindow Example")

        # Create a basic central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Add a button to the central widget
        QPushButton("Click Me", central_widget)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()