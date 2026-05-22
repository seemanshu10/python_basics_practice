# Practice QTreeView

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTreeView,
    QPushButton
)
from PySide2.QtCore import Slot
from PySide2.QtGui import QStandardItemModel,QStandardItem

class QlistWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTreeView Practice")
        self.resize(300, 300)

        main_layout = QVBoxLayout()

        self.tree_widget = QTreeView()
        
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Asset Hierarchy"])
        self.tree_widget.setModel(self.model)
        # self.tree_widget(model)
        self.tree_widget.setEditTriggers(QTreeView.DoubleClicked)
        self.tree_widget.setSelectionMode(QTreeView.SingleSelection)
        self.tree_widget.setSelectionBehavior(QTreeView.SelectRows)
        self.tree_widget.setColumnWidth(0, 200)
        self.tree_widget.resizeColumnToContents(0)
        self.tree_widget.expandAll()

        # tree data creation 
        root_node = self.model.invisibleRootItem()
        # Character hierachy 
        character_item = QStandardItem("Character")
        rig_item = QStandardItem("Rig")
        controls_item = QStandardItem("Controls")
        character_item.appendRow(rig_item)
        rig_item.appendRow(controls_item)

        # Environment Hieracrchy 
        environment_item = QStandardItem("Environment")
        terrain_item = QStandardItem("Terrain")
        lighting_item = QStandardItem("Lighting")
        environment_item.appendRow(terrain_item)
        terrain_item.appendRow(lighting_item)

        root_node.appendRow(character_item)
        root_node.appendRow(environment_item)

        self.tree_widget.setStyleSheet("""
        QTreeView {
            background-color: #2b2b2b;
            color: #ffffff;
            font-size: 13px;
            border: 1px solid #444;
        }
        QTreeView::item:selected {
            background-color: #007acc;
        }
        QHeaderView::section {
            background-color: #3c3c3c;
            font-weight: bold;
        }
        """)

        self.expand_btn = QPushButton("Expand All")
        self.collapse_btn = QPushButton("Collapse All")
        main_layout.addWidget(self.tree_widget)
        main_layout.addWidget(self.expand_btn)
        main_layout.addWidget(self.collapse_btn)
        self.setLayout(main_layout)

        # Connections
        self.tree_widget.clicked.connect(self.on_item_clicked)
        self.tree_widget.expanded.connect(self.on_item_expanded)
        self.expand_btn.clicked.connect(self.tree_widget.expandAll)
        self.collapse_btn.clicked.connect(self.tree_widget.collapseAll)

    @Slot()
    def on_item_clicked(self, index):
        item_name = self.model.itemFromIndex(index).text()
        print(f"Clicked item: {item_name}")

    @Slot()
    def on_item_expanded(self, index):
        item_name = self.model.itemFromIndex(index).text()
        print(f"Expanded: {item_name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QlistWindow()
    window.show()

    sys.exit(app.exec_())