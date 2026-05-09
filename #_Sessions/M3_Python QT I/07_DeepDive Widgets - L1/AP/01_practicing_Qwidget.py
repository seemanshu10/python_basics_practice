import sys

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton)

from PySide2.QtCore import Qt

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Complete QWidget Example")

        main_layout = QVBoxLayout()
        
        label_text = QLabel("Press a button:")
        
        label_text.setAlignment(Qt.AlignCenter)
        label_text.setStyleSheet("""
            QLabel{
                border :2px solid white;
                color: white;
                font-size: 12px         
            }
        """)

        greet_btn = QPushButton("Greet")
        clear_btn = QPushButton("Clear")
        hide_btn = QPushButton("Hide Label")
        show_btn = QPushButton("Show Label")

        greet_btn.setStyleSheet("""
        QPushButton {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 8px 16px;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #1c5980;
        }
        """)

        clear_btn.setStyleSheet("""
        QPushButton {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 8px 16px;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #1c5980;
        }
        """)

        hide_btn.setStyleSheet("""
        QPushButton {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 8px 16px;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #1c5980;
        }
        """)

        show_btn.setStyleSheet("""
        QPushButton {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 8px 16px;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #1c5980;
        }
        """)

        main_layout.addWidget(label_text)
        main_layout.addWidget(greet_btn)
        main_layout.addWidget(clear_btn)
        main_layout.addWidget(hide_btn)
        main_layout.addWidget(show_btn)
        
        # Set Layout on window
        self.setLayout(main_layout) 

        greet_btn.clicked.connect(lambda: label_text.setText("Hello, VFX Artist!"))
        clear_btn.clicked.connect(lambda: label_text.setText("Press a button:"))
        hide_btn.clicked.connect(label_text.hide)
        show_btn.clicked.connect(label_text.show)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Main()
    window.resize(300, 200)

    window.setStyleSheet("""
    Main {
            background-color:#113784;
            border-radius: 5px;
            padding: 8px 16px;
        }  
    """)
    
    window.show()
    sys.exit(app.exec_())