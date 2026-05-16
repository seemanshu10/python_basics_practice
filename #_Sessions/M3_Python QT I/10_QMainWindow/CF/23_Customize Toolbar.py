from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QAction, QToolBar, QDockWidget
)
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My VFX App")
        self.resize(800, 600)

        # Central widget layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter Shot Name:"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QPushButton("Submit"))
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        view_menu = menu_bar.addMenu("View")

        # File menu actions
        open_action = QAction("Open", self)
        exit_action = QAction("Exit", self)
        file_menu.addAction(open_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # Edit menu actions
        copy_action = QAction("Copy", self)
        paste_action = QAction("Paste", self)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)

        # View menu action
        toggle_dock_action = QAction("Toggle Tools Panel", self)
        view_menu.addAction(toggle_dock_action)

        # Toolbar
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)
        toolbar.setMovable(False)  # Make toolbar fixed

        toolbar.addAction(open_action)
        toolbar.addAction(copy_action)

        # Add custom widget to toolbar
        search_box = QLineEdit()
        search_box.setPlaceholderText("Search")
        toolbar.addWidget(search_box)

        # Status bar
        self.statusBar().showMessage("Ready")

        # Dock widget
        self.dock = QDockWidget("Tools", self)
        self.dock.setWidget(QLabel("This is a dockable panel"))
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # Connect actions
        open_action.triggered.connect(self.open_file)
        copy_action.triggered.connect(self.copy_action)
        exit_action.triggered.connect(self.close)
        toggle_dock_action.triggered.connect(self.toggle_tools_panel)

    def open_file(self):
        print("Open clicked from toolbar")
        self.statusBar().showMessage("Opening file...")

    def copy_action(self):
        print("Copy clicked from toolbar")
        self.statusBar().showMessage("Copied to clipboard")

    def toggle_tools_panel(self):
        is_visible = self.dock.isVisible()
        self.dock.setVisible(not is_visible)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
