import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDockWidget Example")

        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        self.dock = QDockWidget("Dockable Panel", self)
        self.dock.setWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()