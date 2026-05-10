import sys, os

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QLabel)

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
        self.setWindowTitle("Complete QCheckBox Example")

        # Create widgets
        self.status_label = QLabel("Toggle settings below:")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))

        self.check_box = QCheckBox("Enable Shadows")
        self.check_box.setTristate(True)

        # Buttons added
        self.state_button = QPushButton("Check State")
        self.rename_button = QPushButton("Rename Checkbox")
    
        # Connect signals
        self.rename_button.clicked.connect(self.on_clicked_rename)
        self.state_button.clicked.connect(self.submit_state)
        
        self.check_box.toggled.connect(self.on_checkbox_toggled)
        self.check_box.stateChanged.connect(self.handle_state_changed)
        
        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.check_box)
        main_layout.addWidget(self.state_button)
        main_layout.addWidget(self.rename_button)
        
        self.setLayout(main_layout)

    def on_checkbox_toggled(self):
        
        # if state == 0:
        #     selected_state = "Unchecked"
        # elif state == 1:
        #     selected_state = "Partially Checked" 
        # elif state == 2:
        #     selected_state = "Checked" 

        check_status = self.check_box.isChecked()
                
        self.status_label.setText(f"Checked : {check_status}")
        print(f"Checkbox is: {check_status}")

    def handle_state_changed(self, state):
        
        if state == 0:
            selected_state = "Unchecked"
        elif state == 1:
            selected_state = "Partially Checked" 
        elif state == 2:
            selected_state = "Checked" 
                
        self.status_label.setText(f"Checkbox is now: {selected_state}")
        print(f"Checkbox is now: {selected_state}")

    def on_clicked_rename(self):
        self.check_box.setText("Use Compositing FX")
        self.status_label.setText("Label updated.")
        print("Checkbox name changed")
    
    def submit_state(self):
        status_chk = self.check_box.checkState()
        print(f"Using checkState(): ", status_chk)
        status = self.check_box.isChecked()
        print(f"Using isChecked(): ", status)

    @Slot()
    def apply_material_theme(self):
        apply_stylesheet(app, theme='dark_blue.xml')

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Main()
    window.resize(400, 250)
    
    window.show()
    sys.exit(app.exec_())