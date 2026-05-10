import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLabel, QSlider
import qdarkstyle
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QFont

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.apply_dark_theme()
        self.setWindowTitle("Complete QSlider Example")

        # Create widgets
        self.status_label = QLabel("Opacity: 50%")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))

        # Buttons added
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(100)
        self.slider.setMinimum(0)
        self.slider.setValue(50)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksAbove)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.slider)
        self.setLayout(main_layout)

        # connections 
        self.slider.sliderReleased.connect(self.released_slider)
        self.slider.sliderPressed.connect(self.pressed_slider)
        self.slider.valueChanged.connect(self.update_slider)
        self.slider.sliderMoved.connect(self.moved_slider)

    def released_slider(self):
        print("Slider Released..")

    def pressed_slider(self):
        print("Slider Pressed.")

    def update_slider(self, value):
        self.status_label.setText(f"Opacity: {value}%")
        print(f"Value Changed: {value}")
    
    def moved_slider(self, value):
        # self.status_label.setText(f"Opacity: {value}%")
        print(f"Slider Moved To: {value}")

    @Slot()
    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(400, 200)
    window.show()
    app.exec_()