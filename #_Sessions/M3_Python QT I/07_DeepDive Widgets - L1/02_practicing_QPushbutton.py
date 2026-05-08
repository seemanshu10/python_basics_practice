import sys

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit)

from PySide2.QtCore import Qt

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Complete QPushButton Example")

        main_layout = QVBoxLayout()
        
        self.task_line = QLineEdit()
        self.task_line.setPlaceholderText("Enter task name")
        
        self.launch_render_btn = QPushButton("Launch Render")
        
        self.launch_render_btn.setStyleSheet("""
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

        main_layout.addWidget(self.task_line)
        main_layout.addWidget(self.launch_render_btn)
        
        
        # Set Layout on window
        self.setLayout(main_layout) 

        # connection 
        self.launch_render_btn.clicked.connect(self.on_clicked)
        self.launch_render_btn.pressed.connect(self.on_pressed)
        self.launch_render_btn.released.connect(self.on_released)


    def on_clicked(self):
        task_name = self.task_line.text()

        print("Task Name:", task_name)

    def on_pressed(self):
        print("Button Pressed")

    def on_released(self):
        print("Button Released")
        

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