import sys, os

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QScrollBar, QLabel)

from PySide2.QtCore import Qt, Slot
from qt_material import apply_stylesheet
from PySide2.QtGui import QFont

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):    
        # Window creating
        self.apply_material_theme()
        self.setWindowTitle("Complete QScrollBar Example")

        # Create widgets
        self.status_label = QLabel("Scroll value: 30")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))

        # scroll bar 
        self.scroll_v = QScrollBar(Qt.Vertical, self) 
        self.scroll_v.setMinimum(0)
        self.scroll_v.setMaximum(100)
        self.scroll_v.setValue(30)
        self.scroll_v.setPageStep(5)
        self.scroll_v.setStyleSheet("""
            QScrollBar:horizontal {
                background: #2c3e50;
                height: 12px;
                margin: 0px 20px 0 20px;
            }
            QScrollBar::handle:horizontal {
                background: #00a8ff;
                border-radius: 6px;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                background: none;
            }
        """)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.scroll_v)

        # Connections scroll
        self.scroll_v.valueChanged.connect(lambda v: print("New value:", v))
        self.scroll_v.valueChanged.connect(lambda v: self.status_label.setText(f"Scroll value: {v}"))
        self.scroll_v.sliderPressed.connect(self.scroll_start)
        self.scroll_v.sliderReleased.connect(self.scroll_release)

        self.setLayout(main_layout)

    def scroll_start(self):
        print("Slider drag started")

    def scroll_release(self):
         print("Slider drag finished")

    @Slot()
    def apply_material_theme(self):
        apply_stylesheet(app, theme='dark_blue.xml')

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Main()
    window.resize(200, 300)
    
    window.show()
    sys.exit(app.exec_())