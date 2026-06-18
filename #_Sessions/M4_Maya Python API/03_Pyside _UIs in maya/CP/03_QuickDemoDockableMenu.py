from PySide2.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout
import shiboken2
from maya import OpenMayaUI as omui
import maya.cmds as cmds


def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QWidget)

class SimpleDockableWidget(QMainWindow):
    def __init__(self, parent=None):
        super(SimpleDockableWidget, self).__init__(parent)
        self.setWindowTitle("Dockable Pyside UI")

        # Create a basic central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Add a button to the central widget
        button = QPushButton("Click Me", central_widget)

        button.clicked.connect(self.on_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(button)
        central_widget.setLayout(layout)

    def on_button_clicked(self):
        print("Button Clicked! This window is part of maya's UI")

def show_window(*args):
    global my_window
    # checks if window is already open it closes them 
    # method resolution order is 
    # 
    """
    [
    SimpleDockableWidget,
    PySide2.QtWidgets.QMainWindow,
    PySide2.QtWidgets.QWidget,
    PySide2.QtCore.QObject,
    object
    ]
    """
    try:
        my_window.close()
        my_window.deleteLater()
    except:
        pass
    # print(SimpleDockableWidget.mro())
    maya_main_window = get_maya_main_window()
    my_window = SimpleDockableWidget(parent=maya_main_window)
    my_window.show()

def custom_main_menu():
    if cmds.menu("Command_Menu", exists=True):
        cmds.deleteUI("Command_Menu", menu=True)

    cmds.menu("Command_Menu", label="Command Menu", parent="MayaWindow")
    cmds.menuItem(label="Command", command=show_window)

custom_main_menu()