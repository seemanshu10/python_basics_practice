import sys, os
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
import qdarkstyle, qtawesome

class IconApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QtAwesome Icons in Pyside2") 
        self.init_ui()

    def init_ui(self):
        self.apply_dark_theme()
        self.main_layout = QVBoxLayout()
        self.label = QLabel("Enter Text Click the button: ") 
        self.line_edit = QLineEdit()
        self.sumbit_btn = QPushButton("Click Me")
        self.play_btn = QPushButton("Play")
        self.play_btn.setIcon(qtawesome.icon('fa6s.play', color='green'))
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.setIcon(qtawesome.icon('fa6s.stop', color='red'))
        self.home_btn = QPushButton("Home")
        self.home_btn.setIcon(qtawesome.icon('mdi.home', color='blue'))

        self.line_edit.setPlaceholderText("Type Something...")

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line_edit)
        self.main_layout.addWidget(self.sumbit_btn)
        self.main_layout.addWidget(self.play_btn)
        self.main_layout.addWidget(self.stop_btn)
        self.main_layout.addWidget(self.home_btn)

        self.sumbit_btn.clicked.connect(self.on_button_click)

        self.setLayout(self.main_layout)

    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)

    def on_button_click(self):

        entered_text = self.line_edit.text()
        self.label.setText(f"You Entered: {entered_text}")
    
if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = IconApp()
    window.resize(400, 300)
    window.show()

    sys.exit(app.exec_())