from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.cmds as cmds
import maya.OpenMayaUI as omui
class SimpleDockableWidget(QtWidgets.QWidget):
    """A simple dockable widget."""
    def __init__(self, parent=None):
        super(SimpleDockableWidget, self).__init__(parent)
        self.setWindowTitle("Dockable PySide UI")
        self.setObjectName("SimpleDockableWidget")
        # Set a layout for the widget
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        # Add example UI elements
        label = QtWidgets.QLabel("Hello, Maya!")
        layout.addWidget(label)

def create_dockable_widget():
    """Create a dockable widget on the right side of the Maya UI."""
    dock_name = "MyDockableWidget"
    # If the dock exists, raise it instead of creating a new one
    if cmds.workspaceControl(dock_name, query=True, exists=True):
        cmds.workspaceControl(dock_name, edit=True, restore=True)
        return
    # Convert the QWidget to a Maya workspace control
    workspace_control = cmds.workspaceControl(dock_name, label="My PySide Dock", retain=False)
    # Find the control layout and add the QWidget
    workspace_control_ptr = omui.MQtUtil.findControl(workspace_control)
    workspace_control_widget = wrapInstance(int(workspace_control_ptr), QtWidgets.QWidget)
    # Create the custom widget
    dock_widget = SimpleDockableWidget()
    workspace_control_widget.layout().addWidget(dock_widget)
    return dock_widget
        
                             
def create_custom_menu():
    """Creates a custom menu in Maya to launch the dockable UI."""
    menu_name = "CustomToolsMenu"
    menu_label = "Custom Tools"
    # If the menu already exists, delete it first
    if cmds.menu(menu_name, exists=True):
        cmds.deleteUI(menu_name)
    # Add the menu to Maya's main menu bar
    custom_menu = cmds.menu(menu_name, label=menu_label, parent="MayaWindow")
    # Add a menu item to launch the dockable UI
    cmds.menuItem(label="Open Dockable UI", parent=custom_menu, command=lambda _: create_dockable_widget())
# Run the function to create the menu

create_custom_menu()