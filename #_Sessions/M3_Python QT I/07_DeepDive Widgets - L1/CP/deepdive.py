import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QCheckBox, QComboBox, QGroupBox, QSlider, QListWidget, QProgressBar

from PySide2.QtCore import Qt
import qdarkstyle, qtawesome

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Tool") 
        self.init_UI()

    def init_UI(self):
        self.apply_dark_theme()

        
        self.main_layout = QVBoxLayout()
        self.run_button = QPushButton("Run")
        self.label = QLabel("Enter Name")
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter Your Name:")
        self.text_edit = QTextEdit()

        # check box 
        self.checkbox = QCheckBox("Enable FX", self)
        self.checkbox.setChecked(True)
        if self.checkbox.isChecked():
            print("Effect enabled")
        self.checkbox.setText("Use Compositing FX")

        # Qcombobox 
        self.combo = QComboBox()
        self.combo.addItem("Low Quality")   
        self.combo.addItems(["Medium", "High", "Ultra"])          
        # self.combo.setEditable(True)                            
        self.combo.setCurrentIndex(2)                      
                                     
        # Qgroupbox 
        self.group = QGroupBox("Render Settings")
        # self.group.setCheckable(True)
        # self.group.setChecked(True)

        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Enable Motion Blur"))
        layout.addWidget(QCheckBox("Enable AO"))

        self.group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #00a8ff;
                border-radius: 5px;
                margin-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 5px;
            }
        """)

        self.group.setLayout(layout)

        # slider button 

        self.slider_layout = QHBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        opacity_label = QLabel("Opacity: 0%")

        self.slider_layout.addWidget(opacity_label)
        self.slider_layout.addWidget(self.slider)

        self.slider.valueChanged.connect(lambda v: opacity_label.setText(f"Opacity: {v}%"))

        # QList Widget Examples 
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Frame 001", "Frame 002", "Frame 003"])

        # submit_btn = QPushButton("Submit")
        # submit_btn.clicked.connect(lambda: print("Selected:", self.list_widget.currentItem().text()))

        self.list_widget.setStyleSheet("""
            QListWidget {
                background-color: #2c3e50;
                color: #ecf0f1;
                font-size: 14px;
                border: 1px solid #34495e;
            }
            QListWidget::item:selected {
                background-color: #00a8ff;
                color: white;
            }
        """)

        layout.addWidget(self.list_widget)
        # layout.addWidget(submit_btn)

    
        # Qpush Button 
        self.run_button.setText("Launch Render")
        self.run_button.setToolTip("Click to start rendering")

        progress = QProgressBar()
        button = QPushButton("Start")
        button.clicked.connect(lambda: progress.setValue(100))
        progress.setStyleSheet("""
            QProgressBar {
                border: 1px solid #2c3e50;
                border-radius: 5px;
                background-color: #2f3640;
                text-align: center;
                color: #ffffff;
            }
            QProgressBar::chunk {
                background-color: #00a8ff;
                width: 20px;
            }
        """)

        # connections 
        self.run_button.clicked.connect(self.on_button_clicked)

        # layout setup 
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line_edit)
        self.main_layout.addWidget(self.text_edit)
        self.main_layout.addWidget(self.checkbox)
        self.main_layout.addWidget(self.combo)
        self.main_layout.addWidget(self.group)
        self.main_layout.addLayout(self.slider_layout)
        self.main_layout.addWidget(self.list_widget)
        self.main_layout.addWidget(self.run_button)
        self.main_layout.addWidget(progress)
        self.main_layout.addWidget(button)
        
        self.setLayout(self.main_layout)

        self.run_button.setStyleSheet("""
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

    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)

    def on_button_clicked(self):
        print("Button Clicked!")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())