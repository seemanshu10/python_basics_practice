import sys
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QApplication, QMainWindow, QTableView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableView Example")
        
        self.table_view = QTableView()
        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        self.table_view.setModel(self.model)
        
        for row in range(8):
            for column in range(5):
                item = QStandardItem(f"Item {row},{column}")
                self.model.setItem(row, column, item)
                
        self.setCentralWidget(self.table_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
