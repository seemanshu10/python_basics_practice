from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QDockWidget, QToolBar, QAction, QWidget,
    QStatusBar, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QLineEdit, QFormLayout, 
    QListWidget
)

from PySide2.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Asset Manager")
        self.setGeometry(200, 200, 800, 600)

        # menu bar 
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.open_btn = self.file_menu.addAction("Open")
        self.file_menu.addSeparator()
        self.save_btn = self.file_menu.addAction("Save")
        self.file_menu.addAction("Exit")

        # shortcuts
        self.open_btn.setShortcut("Ctrl+O")
        self.save_btn.setShortcut("Ctrl+S")

        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.copy_btn = self.edit_menu.addAction("Copy")
        self.paste_btn = self.edit_menu.addAction("Paste")

        self.view_menu = self.menu_bar.addMenu("View")
        self.toggle_dock = self.view_menu.addAction("Toggle Dock")

        # shortcuts
        self.copy_btn.setShortcut("Ctrl+C")
        self.paste_btn.setShortcut("Ctrl+V")

        # Tool bar 
        self.toolbar = QToolBar() 
        # self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

        self.add_asset = QAction("Add Asset", self)
        self.toolbar.addAction(self.add_asset)

        self.delete_asset = QAction("Delete Asset", self)
        self.toolbar.addAction(self.delete_asset)

        self.update_asset = QAction("Update Asset", self)
        self.toolbar.addAction(self.update_asset)

        # central widget 
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # nested layout 
        self.widget_layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        self.asset_label = QLabel("Asset Name:")
        self.asset_line = QLineEdit()
        self.asset_line.setPlaceholderText("Enter Asset Name..")

        self.type_label = QLabel("Asset type:")
        self.type_line = QLineEdit()
        self.type_line.setPlaceholderText("Enter Asset Type..")

        self.form_layout.addRow(self.asset_label, self.asset_line)
        self.form_layout.addRow(self.type_label, self.type_line)
        
        self.widget_layout.addLayout(self.form_layout)

        # button submit
        self.submit_btn = QPushButton("Submit")  
        self.widget_layout.addWidget(self.submit_btn)

        self.central_widget.setLayout(self.widget_layout)

        # connection 
        self.open_btn.triggered.connect(self.open_file)
        self.save_btn.triggered.connect(self.save_file)
        self.copy_btn.triggered.connect(self.copy_action)

        self.add_asset.triggered.connect(self.add_asset_ui)
        self.delete_asset.triggered.connect(self.delete_asset_ui)
        self.update_asset.triggered.connect(self.update_asset_ui)

        self.submit_btn.clicked.connect(self.submit_asset_ui)
        self.toggle_dock.triggered.connect(self.toggle_dock_ui)
        
        # dock toolbar
        self.dock = QDockWidget("Asset List", self)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.BottomDockWidgetArea | Qt.TopDockWidgetArea)
        # self.dock.setWidget(QLabel("This is a Dock Widget"))

        self.dock_list = QListWidget()
        self.dock_list.addItems(["Tree", "Character", "Vehicle"])
        self.dock.setWidget(self.dock_list)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)

        # status bar  widget 
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Ready")
        self.setStatusBar(self.status_bar)

    def submit_asset(self):
        print("Asset Submitted")
    
    def open_file(self):
        print("File is opening")
        self.status_bar.showMessage("File is opening")

    def save_file(self):
        print("File is saved.")
        self.status_bar.showMessage("File is saving..")

    def copy_action(self):
        print("Copied to clipboard.")
        self.status_bar.showMessage("Copied to Clipboard")
    
    def add_asset_ui(self):
        print("Asset Added.")
        self.status_bar.showMessage("Asset is created.")

    def delete_asset_ui(self):
        print("Asset Deleted .")
        self.status_bar.showMessage("Asset is deleted.")

    def update_asset_ui(self):
        print("Asset Updated.")
        self.status_bar.showMessage("Asset is Updated.")

    def submit_asset_ui(self):

        asset = self.asset_line.text()
        type = self.type_line.text()
        print("Asset Submited")
        self.status_bar.showMessage(f"Asset {asset} of type {type} is submitted.")

    def toggle_dock_ui(self):
        is_visible = self.dock.isVisible()
        self.dock.setVisible(not is_visible)
        self.status_bar.showMessage("Dock is Toggled")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())