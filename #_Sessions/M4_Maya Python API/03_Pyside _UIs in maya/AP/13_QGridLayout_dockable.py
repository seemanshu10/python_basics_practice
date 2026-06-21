from PySide2.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLineEdit, QLabel, QPushButton, QMainWindow
)
from PySide2.QtCore import Qt
from maya import OpenMayaUI as omui
import shiboken2
import maya.cmds as cmds 

def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QWidget)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Window setup
        self.setWindowTitle("QGridLayout Integrated")
        self.resize(400, 200)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.name_label = QLabel("Name", self)
        self.email_label = QLabel("Email", self)

        self.name_input = QLineEdit()
        self.email_input = QLineEdit()

        submit_button = QPushButton("Submit")

        # Placeholder text
        self.name_input.setPlaceholderText("Enter your name")
        self.email_input.setPlaceholderText("Enter your email")

        # Grid Layout
        layout = QGridLayout()

        # Add widgets to layout
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.name_input, 0, 1)

        layout.addWidget(self.email_label, 1, 0)
        layout.addWidget(self.email_input, 1, 1)
        layout.addWidget(submit_button, 2, 0, 1, 2)

        layout.setHorizontalSpacing(15)
        layout.setVerticalSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Stretch columns for responsiveness
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 3)

        # Stretch last row
        layout.setRowStretch(3, 1)
        centralWidget.setLayout(layout)

def show_grid_window(*args):
    global my_window
    try:
        my_window.close()
        my_window.deleteLater()
    except:
        pass

    maya_main_window = get_maya_main_window()
    my_window = MainWindow(parent=maya_main_window)
    my_window.show()

def create_dockable_widget():
    """Dockable widget creation """

    dock_name = "GridLayoutWidget"

    if cmds.workspaceControl(dock_name, query=True, exists=True):
        cmds.workspaceControl(dock_name, edit=True, restore=True)
        return
    
    # convert the Qwidget to a maya workspace control
    workspace_control = cmds.workspaceControl(dock_name, label="My Dockable Widget",retain=False)

    workspace_control_ptr = omui.MQtUtil.findControl(workspace_control)
    # Find the control layout and add the Qwidget
    workspace_control_widget = shiboken2.wrapInstance(int(workspace_control_ptr), QMainWindow)

    # create the custom widget 
    dock_widget = MainWindow()
    workspace_control_widget.layout().addWidget(dock_widget)
    return dock_widget


def custom_main_menu():
    menu_name = "CustomGridMenu"
    menu_label = "Grid_Tools"
    if cmds.menu(menu_name, exists=True):
        cmds.deleteUI(menu_name, menu=True)

    custom_menu = cmds.menu(menu_name, label=menu_label, parent="MayaWindow")
    cmds.menuItem(label="Grid Layout", parent=custom_menu, command=lambda _: create_dockable_widget())

custom_main_menu()