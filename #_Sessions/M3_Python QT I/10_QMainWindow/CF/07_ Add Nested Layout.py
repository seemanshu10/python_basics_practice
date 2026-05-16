from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nested Layout Example")
        self.setGeometry(300, 300, 400, 300)
        self.initUI()
        
    def initUI(self):
        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create a vertical layout
        v_layout = QVBoxLayout()
        
        # Create a horizontal layout for buttons
        h_layout = QHBoxLayout()
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        h_layout.addWidget(button1)
        h_layout.addWidget(button2)
        
        # Add the horizontal layout to the vertical layout
        v_layout.addLayout(h_layout)
        
        # Set the layout for the central widget
        central_widget.setLayout(v_layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())