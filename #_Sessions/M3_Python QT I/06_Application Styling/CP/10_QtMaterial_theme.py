import sys, os
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
from qt_material import apply_stylesheet

class MaterialDesignApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Material Design App") 
        self.init_ui()

    def init_ui(self):
        self.apply_material_theme()
        self.main_layout = QVBoxLayout()
        self.label = QLabel("Enter Text Click the button: ") 
        self.line_edit = QLineEdit()
        self.sumbit_btn = QPushButton("Click Me")

        self.line_edit.setPlaceholderText("Type Something...")

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line_edit)
        self.main_layout.addWidget(self.sumbit_btn)

        self.sumbit_btn.clicked.connect(self.on_button_click)

        self.setLayout(self.main_layout)

    def apply_material_theme(self):
        apply_stylesheet(app, theme='dark_cyan.xml')

    def on_button_click(self):

        entered_text = self.line_edit.text()
        self.label.setText(f"You Entered: {entered_text}")
    
if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MaterialDesignApp()
    window.resize(400, 150)
    window.show()

    sys.exit(app.exec_())