# Practice QTableView

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableView,
)
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QStandardItemModel, QStandardItem

class QtableWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTableView Practice")
        self.resize(200, 200)

        main_layout = QVBoxLayout()

        self.qtable_widget = QTableView()
        
        model = QStandardItemModel(3, 2)
        self.qtable_widget.setModel(model)
        # self.qlist_widget(model)
        # self.qtable_widget.setViewMode(QTableView.ListMode)
        model.setHorizontalHeaderLabels(["Shot", "Status"])
        self.qtable_widget.selectRow(1)
        self.qtable_widget.setSortingEnabled(True)
        self.qtable_widget.setColumnWidth(0, 150)
        self.qtable_widget.setEditTriggers(QTableView.DoubleClicked)
        self.qtable_widget.setSelectionBehavior(QTableView.SelectRows)
        self.qtable_widget.setStyleSheet("""
        QTableView {
            background-color: #2e2e2e;
            color: #f1f1f1;
            gridline-color: #444;
            font-size: 13px;
        }
        QHeaderView::section {
            background-color: #3c3c3c;
            padding: 4px;
            font-weight: bold;
            border: 1px solid #222;
        }
        QTableView::item:selected {
            background-color: #007acc;
        }
        """)
        shot_data = [["Shot001", "Queued"], ["Shot002", "Rendering"], ["Shot003", "Completed"]]
        for row, row_data in enumerate(shot_data):
            for column, value in enumerate(row_data):
                item = QStandardItem(value)
                model.setItem(row, column, item)

        self.label = QLabel("Selected:")
        main_layout.addWidget(self.qtable_widget)
        main_layout.addWidget(self.label)
        self.setLayout(main_layout)

        # Connections
        self.qtable_widget.clicked.connect(self.on_item_clicked)

    @Slot()
    def on_item_clicked(self, index):
        print(f"Clicked cell at row: ", index.row(), "Column: ", index.column())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QtableWindow()
    window.show()

    sys.exit(app.exec_())