# Practice QInputDialog

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QInputDialog
)
from PySide2.QtCore import Slot

class InputDialogWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qinput Dialog Example")
        self.resize(300, 400)
        self.main_layout = QVBoxLayout()
        # buittons
        self.name_button = QPushButton("Enter Name")
        self.frame_button = QPushButton("Enter Frame Number")
        self.opacity_button = QPushButton("Enter Opacity")
        self.render_button = QPushButton("Select Render Engine")
        self.enter_shot_button = QPushButton("Enter Shot Number")
        
        # line edit
        self.name_line = QLineEdit()
        self.frame_line = QLineEdit() 
        self.opacity_line = QLineEdit()
        self.render_line = QLineEdit()

        self.main_layout.addWidget(self.name_button)
        self.main_layout.addWidget(self.name_line)
        self.main_layout.addWidget(self.frame_button)
        self.main_layout.addWidget(self.frame_line)
        self.main_layout.addWidget(self.opacity_button)
        self.main_layout.addWidget(self.opacity_line)
        self.main_layout.addWidget(self.render_button)
        self.main_layout.addWidget(self.render_line)
        self.main_layout.addWidget(self.enter_shot_button)

        # Input Dialog 

        self.name_button.clicked.connect(self.ask_for_name)
        self.frame_button.clicked.connect(self.ask_for_frame)
        self.opacity_button.clicked.connect(self.ask_for_opacity)
        self.render_button.clicked.connect(self.ask_for_render_engine)
        self.enter_shot_button.clicked.connect(self.ask_for_shot)

        # getItem
        # item, ok = QInputDialog.getItem(self, "Select Engine", "Choose Render Engine:", ["Arnold", "Redshift", "VRay"])

        self.setLayout(self.main_layout)
    
    @Slot()
    def ask_for_name(self):
        # getText
        text, ok = QInputDialog.getText(self, "Input", "Enter your name:")
        
        if ok:
            print(f"Name : {text}")
            self.name_line.setText(f"{text}")
        else:
            print("File Input Canceled ")

    @Slot()
    def ask_for_frame(self):
        frame, ok = QInputDialog.getInt(self, "Input", "Enter Frame Number:")
    
        if ok:
            print(f"Frame Number : {frame}")
            self.frame_line.setText(f"{frame}")
        else:
            print("Frame Input Canceled ")

    @Slot()
    def ask_for_opacity(self):
        opacity, ok = QInputDialog.getDouble(self,  "Input", "Enter opacity value:")
    
        if ok:
            print(f"Opacity : {opacity}")
            self.opacity_line.setText(f"{opacity}")
        else:
            print("Opacity Input Canceled ")

    @Slot()
    def ask_for_render_engine(self):
        item, ok = QInputDialog.getItem(self, "Select Engine", "Choose Render Engine:", ["Arnold", "Redshift", "VRay"])
    
        if ok:
            print(f"Render Engine : {item}")
            self.render_line.setText(f"{item}")
        else:
            print("Render Engine Input Canceled ")

    @Slot()
    def ask_for_shot(self):
        dialog = QInputDialog(self)
        dialog.setLabelText("Enter shot number:")
        dialog.textValueChanged.connect(lambda text: print("Changed:", text))  # textValueChanged
        dialog.textValueSelected.connect(lambda text: print("Selected:", text))  # textValueSelected
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = InputDialogWindow()
    window.show()

    sys.exit(app.exec_())