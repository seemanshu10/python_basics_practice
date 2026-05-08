import sys
from PySide2.QtWidgets import QApplication, QWidget

# Define a MainWindow class to encapsulate the window logic
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # Initialize the UI

    def initUI(self):
        self.setWindowTitle("Basic PySide2 App")  # Set the window title

# Main block to run the application
if __name__ == "__main__":
    # Create an application instance
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Run the application's event loop
    sys.exit(app.exec_())