# Choose a Shot Type from Dropdown
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog, QLabel, QWidget


from maya import OpenMayaUI as omui
import shiboken2
import maya.cmds as cmds 

def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QWidget)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Shot Type Dropdown")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Pick Shot Category", self)
        self.button.setGeometry(100, 50, 200, 40)

        self.status_label = QLabel("No Shot Type Selected", self)
        self.status_label.setGeometry(20, 100, 250, 50)

        self.button.clicked.connect(self.pick_shot_category)


    def pick_shot_category(self):
        shot_categories = ["Plate", "Comp", "Matte Painting", "Roto", "Cleanup"]
        tag, ok = QInputDialog.getItem(
            self,
            "Shot Category",
            "Select Shot category:",
            shot_categories,
            0, 
            False
            
        )
        # print(f"{tag},   {ok}")
        if ok:
            self.status_label.setText(f"Selected shot type: {tag}")
        else:
            self.status_label.setText("No Shot Type Selected")

def show_inputdialog_menu(*args):
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
    cmds.menuItem(label="Shot", command=show_inputdialog_menu)

custom_menu()
