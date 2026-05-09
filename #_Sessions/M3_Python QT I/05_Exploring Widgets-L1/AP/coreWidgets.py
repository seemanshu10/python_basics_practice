import sys

from PySide2.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QRadioButton, QCheckBox, QComboBox, QGroupBox, QSlider, QProgressBar, QScrollBar, QListWidget, QTabWidget)

import qdarkstyle, qtawesome
from PySide2.QtCore import Qt

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Core Widgets Practice Tool")
        
        self.apply_dark_theme()
        # tab Widgets creation 
        tabs = QTabWidget(self)
        general_info_tab = QWidget()
        settings_panel_tab = QWidget()

        """
        Tab 1 : General info tabs 
        """
        # 1st tab
        info_tab_layout = QVBoxLayout()

        # Project name widget  
        project_label = QLabel("Project Name")
        project_name = QLineEdit()

        info_tab_layout.addWidget(project_label)
        info_tab_layout.addWidget(project_name)
        general_info_tab.setLayout(info_tab_layout)

        # Notes widget 
        notes_label = QLabel("Notes")
        notes_text = QTextEdit()
        
        info_tab_layout.addWidget(notes_label)
        info_tab_layout.addWidget(notes_text)

        # assets list widget 
        assets_label = QLabel("Assets")
        asset_item_list = QListWidget()
        asset_item_list.addItems(["Asset A", "Asset B", "Asset C"])

        info_tab_layout.addWidget(assets_label)
        info_tab_layout.addWidget(asset_item_list)

        """
        Tab 2 : Setting Panel tabs  
        """

        # 2nd tab 
        setting_panel_layout = QVBoxLayout()

        render_set_grp = QGroupBox("Render Settings")
        render_set_layout = QVBoxLayout()

        low_radio = QRadioButton("Low Quality")
        high_radio = QRadioButton("High Quality")

        fx_chkbox = QCheckBox("Enable FX")
        light_chkbox = QCheckBox("Enable Lighting")

        render_set_layout.addWidget(low_radio)
        render_set_layout.addWidget(high_radio)
        render_set_layout.addWidget(fx_chkbox)
        render_set_layout.addWidget(light_chkbox)

        low_radio.setChecked(True)
        fx_chkbox.setChecked(True)
        # QRadioButton("Low Quality").setChecked(True)

        setting_panel_layout.addWidget(render_set_grp)
        render_set_grp.setLayout(render_set_layout)

        # render engine label
        render_engine_label = QLabel("Render Engine")
        render_engine_types = QComboBox()
        render_engine_types.addItems(["Redshift", "Vray", "Arnold"])

        setting_panel_layout.addWidget(render_engine_label)
        setting_panel_layout.addWidget(render_engine_types)

        # render settings widget 
        settings_panel_tab.setLayout(setting_panel_layout)

        # lighting intensity layout 
        lighting_intensity_label = QLabel("Lighting Intensity")
        lighting_intensity_slider = QSlider(Qt.Horizontal)

        setting_panel_layout.addWidget(lighting_intensity_label)
        setting_panel_layout.addWidget(lighting_intensity_slider)
        
        # render progress layout 
        render_label = QLabel("Render Progress")
        render_progressbar = QProgressBar()
        render_progressbar.setMinimum(0)
        render_progressbar.setMaximum(100)
        render_progressbar.setValue(60)

        setting_panel_layout.addWidget(render_label)
        setting_panel_layout.addWidget(render_progressbar)

        # scroll bar layout 
        scroll_bar = QScrollBar()

        setting_panel_layout.addWidget(scroll_bar)

        # buttons Layout 
        button_layout = QHBoxLayout()
        submit_btn = QPushButton("Submit")
        submit_btn.setIcon(qtawesome.icon('ri.download-line', color = 'black'))
        reset_btn = QPushButton("Reset")
        reset_btn.setIcon(qtawesome.icon('mdi.lock-reset', color = 'black'))

        submit_btn.setStyleSheet("""
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

        reset_btn.setStyleSheet("""
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
            background-color: #A52A2A;
        }
        """)

        button_layout.addWidget(submit_btn)
        button_layout.addWidget(reset_btn)

        setting_panel_layout.addLayout(button_layout)
        
        # tabs Addition 
        tabs.addTab(general_info_tab, "General Info")
        tabs.addTab(settings_panel_tab, "Settings Panel")

        # # Project name label 
        # project_label = QLabel("Project Name")
        # project_name = QLineEdit()
    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Main()
    window.resize(300, 520)
    
    window.show()
    sys.exit(app.exec_())