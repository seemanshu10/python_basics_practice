import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
import qdarkstyle
from PySide2.QtCore import Qt, Slot, QTimer
from PySide2.QtGui import QFont

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.apply_dark_theme()
        self.setWindowTitle("Complete QProgressBar Example")

         # Main layout
        self.main_layout = QVBoxLayout()        
        self.setLayout(self.main_layout)

        self.progress_bar = QProgressBar()
        self.progress_button = QPushButton("Start Progress")
        self.busy_button = QPushButton("Show Busy Mode")
        self.reset_button = QPushButton("Reset")

        # default values for progress bar 
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(20)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setTextVisible(True)              
        self.progress_bar.setFormat("Progress: %p%")   

        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #2c3e50;
                border-radius: 5px;
                background-color: #2f3640;
                text-align: center;
                color: #ffffff;
            }
            QProgressBar::chunk {
                background-color: #00a8ff;
                width: 5px;
            }
        """)

        # Add widgets to layout
        self.main_layout.addWidget(self.progress_bar)
        self.main_layout.addWidget(self.progress_button)
        self.main_layout.addWidget(self.busy_button)
        self.main_layout.addWidget(self.reset_button)

        # connect buttons 
        self.progress_button.clicked.connect(self.start_progress)
        self.busy_button.clicked.connect(self.busy_progress)
        self.reset_button.clicked.connect(self.reset_progress) 
        
        # timer setup 
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

    def start_progress(self):
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(True)
        self.timer.stop()

        
        self.timer.start(100)

    def update_progress(self):
        current_value = self.progress_bar.value()

        # print(current_value)
        if current_value < 100:
            new_value = current_value + 2
            self.progress_bar.setValue(new_value)
            self.progress_bar.setFormat("Progress: %p%")   
            print(f"Progress: {new_value}%")
        else:
            self.timer.stop()
            self.progress_bar.setVisible(False)
            print("Process Complete")

    def busy_progress(self):
        self.timer.stop()

        self.progress_bar.setRange(0,0)
        self.progress_bar.setTextVisible(True)      

    def reset_progress(self):
        self.progress_bar.setRange(0,100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)              

        self.progress_bar.setFormat("Progress: %p%")   
        print("Progress: 0%")

    @Slot()
    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.setStyleSheet("""
        QPushButton{
            
            border: 2px solid #888888;
            border-radius: 5px;
            color: #ffffff;
            padding: 1px;
            font-size: 20px;
        }
        QPushButton:hover {
            background-color: #555555; 
        }
        QPushButton:pressed {
            background-color: #b91f1f;
            border: 2px solid #ffffff;
        } 
    """)
    window = Main()
    app.styleSheet
    window.resize(500, 300)
    window.show()
    app.exec_()