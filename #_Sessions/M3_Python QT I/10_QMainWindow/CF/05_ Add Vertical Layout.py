from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Layout Example")
        self.setGeometry(300, 300, 400, 300)
        self.initUI()
        
    def initUI(self):
        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create a vertical layout
        layout = QVBoxLayout()
        
        # Create widgets
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")
        
        # Add widgets to the layout
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        
        # Set the layout for the central widget
        central_widget.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())