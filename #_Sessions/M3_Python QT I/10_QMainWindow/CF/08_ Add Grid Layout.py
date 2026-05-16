from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout Example")
        self.initUI()
        
    def initUI(self):
        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create a grid layout
        layout = QGridLayout()
        
        # Create buttons
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        
        # Add buttons to the grid layout at specific positions
        layout.addWidget(button1, 0, 0)  # Row 0, Column 0
        layout.addWidget(button2, 0, 1)  # Row 0, Column 1
        layout.addWidget(button3, 1, 0)  # Row 1, Column 0
        layout.addWidget(button4, 1, 1)  # Row 1, Column 1
        
        # Set the layout for the central widget
        central_widget.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
