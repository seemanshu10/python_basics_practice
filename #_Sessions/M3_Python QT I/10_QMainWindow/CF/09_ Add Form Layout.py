from PySide2.QtWidgets import QApplication, QMainWindow, QFormLayout, QLabel, QLineEdit, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout Example")
        self.setGeometry(300, 300, 400, 300)
        self.initUI()
        
    def initUI(self):
        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create a form layout
        layout = QFormLayout()
        
        # Create widgets
        label1 = QLabel("Name:")
        input1 = QLineEdit()
        label2 = QLabel("Email:")
        input2 = QLineEdit()
        
        # Add rows to the form layout
        layout.addRow(label1, input1)
        layout.addRow(label2, input2)
        
        # Set the layout for the central widget
        central_widget.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())