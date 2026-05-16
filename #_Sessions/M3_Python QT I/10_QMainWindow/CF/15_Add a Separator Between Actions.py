from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My VFX App")
        self.resize(800, 600)

        label = QLabel("This is a QMainWindow")
        self.setCentralWidget(label)

        # Menu bar and File menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        open_action = QAction("Open", self)
        exit_action = QAction("Exit", self)
        file_menu.addAction(open_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # Edit menu with two actions
        edit_menu = menu_bar.addMenu("Edit")
        copy_action = QAction("Copy", self)
        paste_action = QAction("Paste", self)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)

        # Connect actions
        open_action.triggered.connect(self.open_file)
        exit_action.triggered.connect(self.close)
        copy_action.triggered.connect(self.copy_action)

    def open_file(self):
        print("Open selected")

    def copy_action(self):
        print("Copy selected")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
