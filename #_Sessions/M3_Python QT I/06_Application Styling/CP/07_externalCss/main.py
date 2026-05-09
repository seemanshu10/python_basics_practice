import sys, os
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("External Styling Demo") 
        self.setGeometry(300, 300, 400, 300)
        self.init_ui()

    def init_ui(self):
    
        label = QLabel("Enter Text: ", self) 
        line_edit = QLineEdit(self)
        sumbit_btn = QPushButton("Submit", self)

        line_edit.setPlaceholderText("Type Something...")

        label.setGeometry(50, 50, 200, 40)
        line_edit.setGeometry(50, 100, 200, 40)
        sumbit_btn.setGeometry(50, 150, 200, 40)

        self.apply_stylesheet()

    def apply_stylesheet(self):

        stylesheet_path = os.path.dirname(os.path.abspath(__file__))

        stylesheet_path = os.path.join(stylesheet_path, "style.css")

        with open(stylesheet_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)
    

    
if __name__ == "__main__":

    app = QApplication(sys.argv)

    app.setStyleSheet("""
    QWidget{
            background-color: #2e2e20; 
            color: #ffffff;
            font-size: 14px;
    }
    QPushButton{
        background-color: #444444;
        border: 2px solid #888888;
        border-radius: 5px;
        color: #ffffff;
        padding: 10px;
        font-size: 14px;
    }
    QPushButton:hover {
        background-color: #555555; 
    }
    """)
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())