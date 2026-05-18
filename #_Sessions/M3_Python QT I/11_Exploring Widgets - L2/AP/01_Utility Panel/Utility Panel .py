from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QDockWidget, QToolBar, QAction, QWidget, QSplitter, QSpinBox,
    QStatusBar, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QFormLayout, 
    QListWidget, QTextEdit, QScrollArea, QDoubleSpinBox, QTreeView
)
from PySide2.QtCore import Qt
from PySide2.QtGui import QStandardItemModel, QStandardItem
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("VFX Utility Panel")
        self.setGeometry(200, 200, 820, 650)
        self.menubar()              # menu bar 
        self.toolbar()              # toolbar
        self.central_widget()       # central widget

        self.status_bar()           # status bar

    def menubar(self):
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.open_btn = self.file_menu.addAction("Open")
        self.save_btn = self.file_menu.addAction("Save")
        self.file_menu.addSeparator()
        self.exit_option = self.file_menu.addAction("Exit")

        # shortcuts
        self.open_btn.setShortcut("Ctrl+O")
        self.save_btn.setShortcut("Ctrl+S")

    def toolbar(self):

        self.main_toolbar = QToolBar()
        self.addToolBar(self.main_toolbar)
        
        self.add_exit = QAction("Exit", self)
        self.main_toolbar.addAction(self.add_exit)

    
    def central_widget(self):
        self.splitter_central = QSplitter(Qt.Horizontal)

        self.editor1 = self.main_dock_widget()
        self.editor2 = self.scroll_area_ui()

        self.splitter_central.addWidget(self.editor1)
        self.splitter_central.addWidget(self.editor2)

        self.splitter_central.setSizes([250, 450])

        self.setCentralWidget(self.splitter_central)

    # Left Side Widget 
    def main_dock_widget(self):
        self.dock = QDockWidget("Asset Browser")
        self.dock_widget = QWidget()
        self.dock_layout = QVBoxLayout()

        self.asset_tree()

        self.dock_widget.setLayout(self.dock_layout)
        self.dock.setWidget(self.dock_widget)

        self.splitter_central.addWidget(self.dock)

        return self.dock
    
    def asset_tree(self):

        self.tree_view = QTreeView()
        self.tree_model = QStandardItemModel()
        self.tree_model.setHorizontalHeaderLabels(["Asset Hierarchy"])

        self.tree_view.setModel(self.tree_model)

        self.dock_layout.addWidget(self.tree_model)

    # Right Widget
    def scroll_area_ui(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.right_widget = QWidget()
        self.form_layout = QFormLayout()

        # spin box 
        self.frame_spin_box = QSpinBox()
        self.frame_spin_box.setRange(1, 10000)
        self.frame_spin_box.setValue(100)

        # Double Spin box 
        self.opacity_spin_box = QDoubleSpinBox()
        self.opacity_spin_box.setSingleStep(0.05)

        self.form_layout.addRow("Frame: ", self.frame_spin_box)
        self.form_layout.addRow("Opacity: ", self.opacity_spin_box)

        self.right_widget.setLayout(self.form_layout)
        scroll_area.setWidget(self.right_widget)


        self.button_create()
        self.image_label_create()

        return scroll_area

    def button_create(self):
        
        # button create 
        self.load_image_btn = QPushButton("Load Image")
        self.choose_color_btn = QPushButton("Choose Color")
        self.choose_font_btn = QPushButton("Choose Font")

        self.form_layout.addRow(self.load_image_btn)
        self.form_layout.addRow(self.choose_color_btn)
        self.form_layout.addRow(self.choose_font_btn)

    def image_label_create(self):

        self.image_label = QLabel("No Image Loaded")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(500, 400)
        self.image_label.setStyleSheet("""
            border: 2px solid gray;
            background-color: #222;
            color: white;
        """)

        self.form_layout.addRow(self.image_label)

    def status_bar(self):
        self.statusbar = QStatusBar()
        self.statusbar.showMessage("Ready")
        self.setStatusBar(self.statusbar)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

