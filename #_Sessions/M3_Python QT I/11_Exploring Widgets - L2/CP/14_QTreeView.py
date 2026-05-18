import sys
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTreeView Example")
        
        self.tree_view = QTreeView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Header"])
        self.tree_view.setModel(self.model)
        
        root_node = self.model.invisibleRootItem()
        item0 = QStandardItem("Item 0")
        item1 = QStandardItem("Item 1")
        item0.appendRow(QStandardItem("Subitem 0"))
        item1.appendRow(QStandardItem("Subitem 1"))
        
        root_node.appendRow(item0)
        root_node.appendRow(item1)
        
        self.setCentralWidget(self.tree_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
