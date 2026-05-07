import sys

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton)

from PySide2.QtCore import Qt

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Complete QRadioButton Example")

        main_layout = QVBoxLayout()
        
        self.task_label = QLabel("Choose export format:")
        self.task_label.setAlignment(Qt.AlignCenter)
        self.task_label.setStyleSheet("""
        QLabel {
            color: white;
            font-size: 18px     
        }
        
        """)

        self.mp4_rad_btn = QRadioButton("MP4")

        self.mp4_rad_btn.setStyleSheet("""
        QRadioButton {
            color: white;
            font-size: 12px     
        }
        """)

        self.exr_rad_btn = QRadioButton("EXR")
        self.exr_rad_btn.setStyleSheet("""
        QRadioButton {
            color: white;
            font-size: 12px     
        }
        """)
        self.png_rad_btn = QRadioButton("PNG")
        self.png_rad_btn.setStyleSheet("""
        QRadioButton {
            color: white;
            font-size: 12px     
        }
        """)

        self.export_btn = QPushButton("Export")
        
        self.export_btn.setStyleSheet("""
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

        main_layout.addWidget(self.task_label)
        main_layout.addWidget(self.mp4_rad_btn)
        main_layout.addWidget(self.exr_rad_btn)
        main_layout.addWidget(self.png_rad_btn)
        main_layout.addWidget(self.export_btn)
        
        # Set Layout on window
        self.setLayout(main_layout) 

        # connection 
        self.export_btn.clicked.connect(self.on_clicked)
        # self.launch_render_btn.pressed.connect(self.on_pressed)
        # self.launch_render_btn.released.connect(self.on_released)


    def on_clicked(self):
        # task_name = self.task_label.text()
        selected_format = ""
        
        if self.mp4_rad_btn.isChecked():
            selected_format = "MP4"
        elif self.exr_rad_btn.isChecked():
            selected_format = "EXR"
        elif self.png_rad_btn.isChecked():
            selected_format = "PNG"

        text_label_final = "Selected format :" + selected_format
        self.task_label.setText(text_label_final)

        
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