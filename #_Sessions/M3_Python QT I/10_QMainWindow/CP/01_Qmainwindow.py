from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QTextEdit, QDockWidget, QToolBar, QAction, QWidget,
    QStatusBar
)

from PySide2.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Layout All Example")
        self.setGeometry(200, 200, 800, 600)

        # menu bar 
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.file_menu.addAction("Open")
        self.file_menu.addAction("Save")
        self.file_menu.addAction("Exit")

        # Tool bar 
        self.toolbar = QToolBar("Main Toolbar") 
        # self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

        action_a = QAction("Action A", self)
        self.toolbar.addAction(action_a)

        action_b = QAction("Action B", self)
        self.toolbar.addAction(action_b)

        # central widget 
        self.central_widget = QTextEdit()
        self.central_widget.setPlaceholderText("This is the central Widget Area.")
        self.setCentralWidget(self.central_widget)

        # dock toolbar
        dock = QDockWidget("Dock Panel", self)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.BottomDockWidgetArea | Qt.TopDockWidgetArea)
        dock.setWidget(QLabel("This is a Dock Widget"))
        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        # status bar  widget 
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Ready")
        self.setStatusBar(self.status_bar)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())