import sys
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QAction,
    QToolBar,
    QDockWidget,
    QLabel,
    QStatusBar
)
from PySide2.QtCore import Qt
import qdarkstyle

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.apply_dark_theme()

        # Window setup
        self.setWindowTitle("Studio Editor")
        self.resize(900, 600)

        # Central Widget
        self.text_editor = QTextEdit()
        self.text_editor.setPlaceholderText("Type something here...")
        self.setCentralWidget(self.text_editor)

        self.clear_action = QAction("Clear", self)
        self.exit_action = QAction("Exit", self)

        self.clear_action.triggered.connect(self.clear_editor)
        self.exit_action.triggered.connect(self.close)

        # Menu Bar

        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(self.clear_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        view_menu = menu_bar.addMenu("View")
        self.toggle_dock = view_menu.addAction("Toggle Dock")

        # Toolbar
        
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        toolbar.addAction(self.clear_action)
        toolbar.addAction(self.exit_action)

        # Dock Widget

        self.dock = QDockWidget("Inspector", self)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        inspector_label = QLabel("Properties Panel")
        inspector_label.setAlignment(Qt.AlignCenter)

        self.dock.setWidget(inspector_label)

        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # Status Bar
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)

        self.statusBar().showMessage("Ready")

        # Connections
        self.toggle_dock.triggered.connect(self.toggle_dock_ui)

    def toggle_dock_ui(self):
        is_visible = self.dock.isVisible()
        self.dock.setVisible(not is_visible)
        self.statusBar().showMessage("Dock is toggled.")

    def clear_editor(self):
        self.text_editor.clear()
        self.statusBar().showMessage("Editor cleared")

    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())