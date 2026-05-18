import sys
from PySide2.QtCore import QStringListModel
from PySide2.QtWidgets import QApplication, QMainWindow, QListView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListView Example")
        
        self.list_view = QListView()
        self.model = QStringListModel(["Item 1", "Item 2", "Item 3"])
        self.list_view.setModel(self.model)
        self.setCentralWidget(self.list_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    