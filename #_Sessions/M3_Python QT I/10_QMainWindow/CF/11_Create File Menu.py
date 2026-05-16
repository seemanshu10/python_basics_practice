from PySide2.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My VFX App")

        label = QLabel("This is a QMainWindow")
        self.setCentralWidget(label)

        # Create menu bar
        menu_bar = self.menuBar()

        # Add top-level menus
        menu_bar.addMenu("File")
        menu_bar.addMenu("Edit")
        menu_bar.addMenu("View")
        menu_bar.addMenu("Tools")
        menu_bar.addMenu("Help")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
