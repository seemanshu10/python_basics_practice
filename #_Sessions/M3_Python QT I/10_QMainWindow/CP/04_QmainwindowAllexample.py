from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,QPushButton, QLabel, QAction, QToolBar, QDockWidget, QLineEdit
)

from PySide2.QtCore import Qt
import sys
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My VFX App")
        self.setGeometry(300, 300, 400, 200)
        self.label = QLabel("This is a QmainWindow")

        # Menu Bar
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.view_menu = self.menu_bar.addMenu("View")
        self.menu_bar.addMenu("Tools")
        self.menu_bar.addMenu("Help")

        # menu bar Actions
        self.open_action = QAction("Open")
        self.file_menu.addAction(self.open_action)
        self.exit_action = QAction("Exit")
        self.file_menu.addAction(self.exit_action)

        self.copy_action = QAction("Copy")
        self.edit_menu.addAction(self.copy_action)
        self.paste_action = QAction("Paste")
        self.edit_menu.addAction(self.paste_action)

        # toolbar 
        self.toolbar = QToolBar("Main ToolBar") # create toolbar
        self.addToolBar(self.toolbar) # adds toolbar to main window

        self.toggle_dock_action = QAction("Toggle Tools Panel")
        self.view_menu.addAction(self.toggle_dock_action)

        self.toolbar.addAction(self.open_action)
        self.toolbar.addAction(self.exit_action)

        # Status BAr 
        self.statusBar().showMessage("Ready")
        
        # central widget set main label
        # central widget 
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()

        self.label_shot = QLabel("Enter Shot Name: ")
        self.line_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")

        self.central_layout.addWidget(self.label_shot)
        self.central_layout.addWidget(self.line_edit)
        self.central_layout.addWidget(self.submit_button)

        self.central_widget.setLayout(self.central_layout)

        self.setCentralWidget(self.central_widget)

        # Dock Toolbar 
        self.dock = QDockWidget("Tools")
        self.dock.setFloating(False)

        self.dock_content = QWidget()
        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(QLabel("Tool 1"))
        self.vbox_layout.addWidget(QLabel("Tool 2"))
        self.dock_content.setLayout(self.vbox_layout)

        self.dock.setWidget(self.dock_content)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)

        # connections Slots 
        self.open_action.triggered.connect(self.open_file)
        self.copy_action.triggered.connect(self.copy_test_action)
        self.exit_action.triggered.connect(self.close)
        self.toggle_dock_action.triggered.connect(self.toggle_tools_panel)

    def open_file(self):
        print("Open Selected")
        self.statusBar().showMessage("Opening File....")

    def copy_test_action(self):
        self.statusBar().showMessage("Copied to clipboard")
        print("Copy Selected")

    def toggle_tools_panel(self):
        is_visible = self.dock.isVisible()
        self.dock.setVisible(not is_visible)

if __name__ == "__main__":

    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())