from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My VFX App")

        label = QLabel("This is a QMainWindow")
        self.setCentralWidget(label)

        # Create menu bar
        menu_bar = self.menuBar()

        # Add top-level menus
        file_menu = menu_bar.addMenu("File")
        menu_bar.addMenu("Edit")
        menu_bar.addMenu("View")
        menu_bar.addMenu("Tools")
        menu_bar.addMenu("Help")

        # Create actions for File menu
        open_action = QAction("Open", self)
        exit_action = QAction("Exit", self)

        # Add actions to File menu
        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
