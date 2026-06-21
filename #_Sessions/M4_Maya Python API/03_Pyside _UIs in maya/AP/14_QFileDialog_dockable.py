import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFontDialog, QPushButton, QWidget

from maya import OpenMayaUI as omui
import shiboken2
import maya.cmds as cmds 

def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QWidget)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("QFontDialog Example")
        
        self.button = QPushButton("Choose Font")
        self.button.clicked.connect(self.open_font_dialog)
        self.setCentralWidget(self.button)

    def open_font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            print(font.toString())

def create_dockable_widget():
    """Dockable widget creation """

    dock_name = "FileDialogWidget"

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


def custom_menu():
    menu_name = "CustomToolsMenu"
    menu_label = "Custom_Tools"
    if cmds.menu(menu_name, exists=True):
        cmds.deleteUI(menu_name, menu=True)

    # Add the menu to Maya's main menu bar
    custom_menu = cmds.menu(menu_name, label=menu_label, parent="MayaWindow")
    # Add a menu item to launch the dockable UI
    cmds.menuItem(label="Open Dockable UI", parent=custom_menu, command=lambda _: create_dockable_widget())


custom_menu()

