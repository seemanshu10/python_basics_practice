from PySide2.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QStatusBar,
    QDockWidget, QLabel, QWidget, QVBoxLayout, QAction
)
from PySide2.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Full QMainWindow Layout Example")
        self.setGeometry(200, 150, 800, 500)
        self.initUI()

    def initUI(self):
        # --- Menu Bar ---
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        help_menu = menu_bar.addMenu("Help")

        # --- Actions ---
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # --- Tool Bar ---
        tool_bar = QToolBar("Main Toolbar")
        self.addToolBar(tool_bar)
        tool_bar.addAction(open_action)
        tool_bar.addAction(save_action)

        # --- Status Bar ---
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Ready")

        # --- Central Widget ---
        central_label = QLabel("This is the Central Widget Area")
        central_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(central_label)

        # --- Dock Widget ---
        dock = QDockWidget("Tools Panel", self)
        dock.setFloating(False)

        dock_content = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tool Option 1"))
        layout.addWidget(QLabel("Tool Option 2"))
        layout.addWidget(QLabel("Tool Option 3"))
        dock_content.setLayout(layout)

        dock.setWidget(dock_content)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())