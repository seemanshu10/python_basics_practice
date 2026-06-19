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

def font_dialog_menu(*args):
    global my_window
    my_window.close()
    my_window.deleteLater()
    
    maya_main_window = get_maya_main_window()
    my_window = MainWindow(parent=maya_main_window)
    my_window.show()

def custom_menu():
    if cmds.menu("Font_Dialog", exists=True):
        cmds.deleteUI("Font_Dialog", menu=True)

    cmds.menu("Font_Dialog", label="FontGui", parent="MayaWindow")
    cmds.menuItem(label="Font", command=font_dialog_menu)

custom_menu()

