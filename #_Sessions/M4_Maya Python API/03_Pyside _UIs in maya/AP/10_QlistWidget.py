# Practice QListView

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget, QMainWindow,
    QVBoxLayout,
    QLabel,
    QListView,
    QSlider,
    
)
from PySide2.QtCore import Slot, Qt, QStringListModel
from maya import OpenMayaUI as omui
import shiboken2
import maya.cmds as cmds 

def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QWidget)

class QlistWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QlistWindow, self).__init__(parent)

        self.setWindowTitle("QListView Practice")
        self.resize(200, 200)

        main_layout = QVBoxLayout()

        self.qlist_widget = QListView()
        
        model = QStringListModel(["Beauty", "Specular", "Diffuse", "ZDepth", "Shadow"])
        self.qlist_widget.setModel(model)
        # self.qlist_widget(model)
        self.qlist_widget.setViewMode(QListView.ListMode)

        self.label = QLabel("Selected:")
        main_layout.addWidget(self.qlist_widget)
        main_layout.addWidget(self.label)
        self.setLayout(main_layout)
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)

        # Connections
        self.qlist_widget.clicked.connect(self.on_item_clicked)

    @Slot()
    def on_item_clicked(self, index):
        print(f"item Clicked: {index.data()}")
        self.label.setText(f"Selected: {index.data()}")


def show_listwidget_menu(*args):
    global my_window
    try:
        my_window.close()
        my_window.deleteLater()
    except:
        pass

    maya_main_window = get_maya_main_window()
    my_window = QlistWindow(parent=maya_main_window)
    my_window.show()

def custom_menu():
    if cmds.menu("Main_Window", exists=True):
        cmds.deleteUI("Main_Window", menu=True)

    cmds.menu("Main_Window", label="Input_Tool", parent="MayaWindow")
    cmds.menuItem(label="List_View_Tool", command=show_listwidget_menu)

custom_menu()