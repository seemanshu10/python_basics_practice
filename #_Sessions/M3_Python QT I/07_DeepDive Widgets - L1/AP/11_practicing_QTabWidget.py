import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QTabWidget, QLineEdit, QCheckBox
import qdarkstyle
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QFont

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.apply_dark_theme()
        self.setWindowTitle("Complete QTabWidget Example")

         # Main layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Create QTabWidget
        self.tabs = QTabWidget()

        # Enable movable and closable tabs
        self.tabs.setMovable(True)
        self.tabs.setTabsClosable(True)

        # Custom stylesheet
        self.tabs.setStyleSheet("""
            QTabWidget:pane {
                border: 2px solid #444;
                background: #2b2b2b;
                border-radius: 5px;
            }

            QTabBar:tab {
                background: #555;
                color: white;
                padding: 8px 15px;
                margin: 2px;
                border-radius: 4px;
            }

            QTabBar:tab:selected {
                background: #0078d7;
            }

            QTabBar:tab:hover {
                background: #666;
            }
        """)

        # Create initial tabs
        self.create_render_settings_tab()
        self.create_fx_tab()

        # Connect signals
        self.tabs.currentChanged.connect(self.on_tab_changed)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        # Add Metadata Tab button
        self.add_metadata_button = QPushButton("Add Metadata Tab")
        self.add_metadata_button.setStyleSheet("""
        QPushButton{
            
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

        self.add_metadata_button.clicked.connect(self.add_metadata_tab)

        # Add widgets to layout
        self.main_layout.addWidget(self.tabs)
        self.main_layout.addWidget(self.add_metadata_button)

    # Render Settings Tab

    def create_render_settings_tab(self):
        render_tab = QWidget()
        layout = QVBoxLayout()

        render_path = QLineEdit("Render Path")
        motion_blur = QCheckBox("Enable Motion Blur")

        layout.addWidget(render_path)
        layout.addWidget(motion_blur)

        render_tab.setLayout(layout)
 
        self.tabs.addTab(render_tab, "Render Settings")

    # FX Tab
    def create_fx_tab(self):
        fx_tab = QWidget()
        layout = QVBoxLayout()

        label = QLabel("FX Controls coming soon")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)

        fx_tab.setLayout(layout)

        self.tabs.addTab(fx_tab, "FX")

    # Add Metadata Tab
    
    def add_metadata_tab(self):
        metadata_tab = QWidget()
        layout = QVBoxLayout()

        shot_id = QLineEdit()
        shot_id.setPlaceholderText("Shot ID")

        artist = QLineEdit()
        artist.setPlaceholderText("Artist")

        layout.addWidget(shot_id)
        layout.addWidget(artist)

        metadata_tab.setLayout(layout)

        # Insert tab at index 1
        self.tabs.insertTab(1, metadata_tab, "Metadata")

        # Automatically switch to new tab
        self.tabs.setCurrentIndex(1)
    # Signals

    def on_tab_changed(self, index):
        print(f"Switched to tab index: {index}")

    def close_tab(self, index):
        print(f"Closing tab at index: {index}")
        self.tabs.removeTab(index)

    @Slot()
    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(500, 300)
    window.show()
    app.exec_()