from PySide2.QtWidgets import QApplication, QWidget
import sys

# Create an application instance
app = QApplication(sys.argv)

# Create a main window using QWidget
window = QWidget()
window.setWindowTitle("Basic PySide2 App")  # Set the window title

# Show the window
window.show()

# Run the application's event loop
app.exec_()