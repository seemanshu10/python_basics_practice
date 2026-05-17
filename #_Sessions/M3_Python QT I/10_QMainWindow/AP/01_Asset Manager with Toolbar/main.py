# Toolbar with Actions for Asset Management
import sys
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QTextEdit, QDockWidget, QToolBar, QAction, QStatusBar
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Asset Manager")
        self.setGeometry(200, 200, 800, 600)

        # tool bar 
        self.tool_bar = QToolBar("Main Toolbar", self)
        self.add_asset = QAction("Add Asset", self)
        self.delete_asset = QAction("Delete Asset", self)

        self.addToolBar(self.tool_bar)
        self.tool_bar.addAction(self.add_asset)
        self.tool_bar.addAction(self.delete_asset)

        # central widget 
        self.central_widget = QLabel("Welcome to the Asset Manager")
        self.setCentralWidget(self.central_widget)

        # Status bar  
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Ready")
        self.setStatusBar(self.status_bar)

        # connections 
        self.add_asset.triggered.connect(self.addasset)
        self.delete_asset.triggered.connect(self.deleteasset)

    def addasset(self):
        print("Asset is Added.")
        self.status_bar.showMessage("Asset Added")

    def deleteasset(self):
        print("Asset is Deleted.")
        self.status_bar.showMessage("Asse Deleted")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())