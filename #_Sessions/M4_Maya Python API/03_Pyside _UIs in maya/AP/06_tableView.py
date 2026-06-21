# Practice QTableView

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget, QMainWindow,
    QVBoxLayout,
    QLabel,
    QTableView,
)
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QStandardItemModel, QStandardItem

from maya import OpenMayaUI as omui
import shiboken2
import maya.cmds as cmds 

def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QWidget)

class QtableWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QtableWindow, self).__init__(parent)

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
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)

        # Connections
        self.qtable_widget.clicked.connect(self.on_item_clicked)

    @Slot()
    def on_item_clicked(self, index):
        print(f"Clicked cell at row: ", index.row(), "Column: ", index.column())

def show_table_menu(*args):
    global my_window
    try:
        my_window.close()
        my_window.deleteLater()
    except:
        pass

    maya_main_window = get_maya_main_window()
    my_window = QtableWindow(parent=maya_main_window)
    my_window.show()

def custom_menu():
    if cmds.menu("Main_Window", exists=True):
        cmds.deleteUI("Main_Window", menu=True)

    cmds.menu("Main_Window", label="Window_Tool", parent="MayaWindow")
    cmds.menuItem(label="QTable Window", command=show_table_menu)

custom_menu()