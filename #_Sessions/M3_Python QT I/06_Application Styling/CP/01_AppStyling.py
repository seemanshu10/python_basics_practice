import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class AppStylingDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App Styling Demo") 
        self.setGeometry(100, 180, 400, 200)
        self.init_ui()

    def init_ui(self):
       
        main_layout = QVBoxLayout()

        button1 = QPushButton("Click Me 1") 
        button2 = QPushButton("Click Me 2")
        button3 = QPushButton("Click Me 3")

        main_layout.addWidget(button1)
        main_layout.addWidget(button2)
        main_layout.addWidget(button3)
        self.setLayout(main_layout)

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
    window = AppStylingDemo()
    window.resize(300, 200)
    window.show()

    sys.exit(app.exec_())