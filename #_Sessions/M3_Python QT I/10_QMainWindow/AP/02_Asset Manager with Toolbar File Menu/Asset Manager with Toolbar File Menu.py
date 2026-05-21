# File Menu with Open & Save Options
# Toolbar with Actions for Asset Management
import sys
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QStatusBar, QWidget, QVBoxLayout
)

from PySide2.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Asset Management")
        self.setGeometry(200, 200, 800, 600)

        # menu bar 
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.open_btn = self.file_menu.addAction("Open")
        self.save_btn = self.file_menu.addAction("Save")

        # shortcuts
        self.open_btn.setShortcut("Ctrl+O")
        self.save_btn.setShortcut("Ctrl+S")

        # central widget 
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.label_widget = QLabel("Asset Manager Dashboard")

        self.central_layout.addWidget(self.label_widget)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        # Status bar  
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Ready")
        self.setStatusBar(self.status_bar)

        # connections 
        self.open_btn.triggered.connect(self.open_asset)
        self.save_btn.triggered.connect(self.save_asset)

    @Slot()
    def open_asset(self):
        print("Opening Asset...")
        self.status_bar.showMessage("Opening Asset...")

    @Slot()
    def save_asset(self):
        print("Save Asset.")
        self.status_bar.showMessage("Saving Asset")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())