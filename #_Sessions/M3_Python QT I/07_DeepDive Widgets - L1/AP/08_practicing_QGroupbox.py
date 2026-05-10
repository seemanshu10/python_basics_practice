import sys
from PySide2.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QRadioButton, QLabel, QPushButton
import qdarkstyle
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QFont

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.apply_dark_theme()
        self.setWindowTitle("CompleteQGroupBoxExample")

        # Create widgets
        self.status_label = QLabel("Select a quality setting:")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))

        self.group_box = QGroupBox("Render Settings", self)
        self.grp_layout = QVBoxLayout()
        self.enable_ao = QRadioButton("Enable Ambient Occlusion")
        self.enable_mb = QRadioButton("Enable Motion Blur")
        self.grp_layout.addWidget(self.enable_ao)
        self.grp_layout.addWidget(self.enable_mb)
        self.group_box.setCheckable(True)
        self.group_box.setChecked(True)
        self.group_box.setLayout(self.grp_layout)

        self.group_box.setStyleSheet("""
        QGroupBox {
            font-weight: bold;
            border: 2px solid #00a8ff;
            border-radius: 5px;
            margin-top: 10px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 10;
        }
        """)

        # Buttons added
        self.grp_button = QPushButton("Check Group State")
        self.grp_button.setStyleSheet("""
        QPushButton{
            background-color: green;
            border: 2px solid #888888;
            border-radius: 5px;
            color: #ffffff;
            padding: 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #555555; 
        }
        QPushButton:pressed {
            background-color: #b91f1f;
            border: 2px solid #ffffff;
        }                                     
        """)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.group_box)
        main_layout.addWidget(self.grp_button)

        # connections logic 
        self.group_box.toggled.connect(self.group_toggled)
        self.enable_ao.clicked.connect(self.get_selected)
        self.enable_mb.clicked.connect(self.get_selected)
        self.grp_button.clicked.connect(self.button_clicked)

        self.setLayout(main_layout)
    
    @Slot()
    def button_clicked(self):
        
        var = self.group_box.isChecked()
        self.status_label.setText(f"Group Checked?: {var}")

        print(f"Checked: {var}")

    @Slot()
    def get_selected(self):
        if self.enable_ao.isChecked():
            print("Enable AO : checked")
            self.status_label.setText(f"Ambient Occlusion Toggled: True")
        elif self.enable_mb.isChecked():
            print("Enable MB : checked")
            self.status_label.setText(f"Motion Blur Toggled: True")

    @Slot()
    def group_toggled(self):
        
        var = self.group_box.isChecked()
        self.status_label.setText(f"Group Toggled: {var}")

        print(f"Group Toggled: {var}")

    @Slot()
    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(500, 500)
    window.show()
    app.exec_()