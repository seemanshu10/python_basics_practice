# Practice QDockWidget
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,QPushButton, QLabel, QAction, QToolBar, QDockWidget, QLineEdit
)

from PySide2.QtCore import Qt, Slot
import sys

from maya import OpenMayaUI as omui
import shiboken2
import maya.cmds as cmds 

def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QWidget)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QdockWidget Example")
        self.setGeometry(300, 300, 500, 500)

        # Menu Bar
        self.menu_bar = self.menuBar()
        self.view_menu = self.menu_bar.addMenu("View")

        self.toggle_action = QAction("Inspector Panel")
        self.view_menu.addAction(self.toggle_action)

        # Status BAr 
        self.statusBar().showMessage("Ready")

        # Dock Toolbar
        self.dock = QDockWidget("Inspector Panel")
        self.dock.setFloating(False)

        self.dock_content = QWidget()
        self.vbox_layout = QVBoxLayout()
        self.label_dock = QLabel("Properties go here")

        self.vbox_layout.addWidget(self.label_dock)
        self.dock_content.setLayout(self.vbox_layout)

        self.dock.setWidget(self.dock_content)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)
        self.dock.setStyleSheet("""
        QDockWidget {
            background-color: #2b2b2b;
            color: #ffffff;
        }
        QDockWidget::title {
            background-color: #444444;
            padding: 6px;
        }
        """)

        # central Widget 
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()

        self.main_label = QLabel("Main Content")
        self.central_layout.addWidget(self.main_label)

        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        self.toggle_action.triggered.connect(self.dock_visibilty_action)
        self.dock.topLevelChanged.connect(lambda f: print("Floating: ", f))
        self.dock.dockLocationChanged.connect(lambda a: print("Moved to area: ", a))

    @Slot()
    def dock_visibilty_action(self):
        is_visible = self.dock.isVisible()
        self.dock.setVisible(not is_visible)
        print("Dock Visible:", is_visible )

        
def show_dock_menu(*args):
    global my_window
    try:
        my_window.close()
        my_window.deleteLater()
    except:
        pass

    maya_main_window = get_maya_main_window()
    my_window = MainWindow(parent=maya_main_window)
    my_window.show()

def custom_menu():
    if cmds.menu("Main_Window", exists=True):
        cmds.deleteUI("Main_Window", menu=True)

    cmds.menu("Main_Window", label="Input_Tool", parent="MayaWindow")
    cmds.menuItem(label="DockWidget_tool", command=show_dock_menu)

custom_menu()