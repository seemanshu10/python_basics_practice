from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QTextEdit, QDockWidget,
    QToolBar, QAction, QWidget, QVBoxLayout, QMenuBar, QStatusBar
)
from PySide2.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMainWindow Full Layout Example")
        self.setGeometry(200, 200, 800, 600)

        # --- Menu Bar ---
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Exit")

        # --- Tool Bar ---
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        action_a = QAction("Action A", self)
        toolbar.addAction(action_a)

        action_b = QAction("Action B", self)
        toolbar.addAction(action_b)

        # --- Central Widget ---
        central_widget = QTextEdit()
        central_widget.setPlaceholderText("This is the Central Widget area.")
        self.setCentralWidget(central_widget)

        # --- Dock Widget (Left) ---
        dock = QDockWidget("Dock Panel", self)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dock.setWidget(QLabel("This is a Dock Widget"))
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        # --- Status Bar ---
        status_bar = QStatusBar()
        status_bar.showMessage("Ready")
        self.setStatusBar(status_bar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())