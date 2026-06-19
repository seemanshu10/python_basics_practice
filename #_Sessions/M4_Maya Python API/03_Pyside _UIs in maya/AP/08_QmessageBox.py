# Practice QMessageBox
import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget, QMainWindow,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QMessageBox
)
from PySide2.QtCore import Slot
from maya import OpenMayaUI as omui
import shiboken2
import maya.cmds as cmds 

def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QWidget)

class MessageBoxWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MessageBoxWindow, self).__init__(parent)

        self.setWindowTitle("QMessage Practice")
        self.resize(500, 150)

        # Layout
        layout = QVBoxLayout()
        self.render_button = QPushButton("Delete Render Cache")

        # Add widgets to layout
        layout.addWidget(self.render_button)
        self.setLayout(layout)

        # Button connection
        self.render_button.clicked.connect(self.show_message_box)

        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

    @Slot()
    def show_message_box(self):
        # Create custom QFileDialog
        dialog = QMessageBox(self)

        #  dialog
        dialog.setText("Delete render cache?")
        dialog.setInformativeText("This action cannot be undone.")
        dialog.setIcon(QMessageBox.Warning)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.No)
        dialog.buttonClicked.connect(lambda b: print("Button clicked:", b.text()))

        dialog.exec_()
def show_messagebox_menu(*args):
    global my_window
    try:
        my_window.close()
        my_window.deleteLater()
    except:
        pass

    maya_main_window = get_maya_main_window()
    my_window = MessageBoxWindow(parent=maya_main_window)
    my_window.show()

def custom_menu():
    if cmds.menu("Main_Window", exists=True):
        cmds.deleteUI("Main_Window", menu=True)

    cmds.menu("Main_Window", label="Input_Tool", parent="MayaWindow")
    cmds.menuItem(label="QmessageBox", command=show_messagebox_menu)

custom_menu()