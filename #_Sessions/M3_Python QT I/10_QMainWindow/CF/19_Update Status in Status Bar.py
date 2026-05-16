from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QToolBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My VFX App")
        self.resize(800, 600)

        label = QLabel("This is a QMainWindow")
        self.setCentralWidget(label)

        # Menu bar and top-level menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")

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

        # Toolbar
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)
        toolbar.addAction(open_action)
        toolbar.addAction(copy_action)

        # Status bar
        self.statusBar().showMessage("Ready")

        # Connect actions to slots
        open_action.triggered.connect(self.open_file)
        copy_action.triggered.connect(self.copy_action)
        exit_action.triggered.connect(self.close)

    def open_file(self):
        print("Open clicked from toolbar")
        self.statusBar().showMessage("Opening file...")

    def copy_action(self):
        print("Copy clicked from toolbar")
        self.statusBar().showMessage("Copied to clipboard")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
