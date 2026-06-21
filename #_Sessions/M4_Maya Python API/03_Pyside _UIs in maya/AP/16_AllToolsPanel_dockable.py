# Tool Configuration Panel
from PySide2.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow,
    QFileDialog, QMessageBox, QColorDialog, QFontDialog, QInputDialog, QLabel
)
from PySide2.QtGui import QFont, QColor
import sys

from maya import OpenMayaUI as omui
import shiboken2
import maya.cmds as cmds 

def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QWidget)

class DialogTool(QMainWindow):
    def __init__(self, parent=None):
        super(DialogTool, self).__init__(parent)
        self.setWindowTitle("AllTools- panel")
        self.resize(200, 200)

        # Initialize variables
        self.file_path = None
        self.name = None
        self.color = None
        self.font = None

        # Label to show selected name and styling
        self.display_label = QLabel("Your output will appear here.")
        self.display_label.setWordWrap(True)

        # Buttons to trigger each dialog
        self.pick_folder_btn = QPushButton("Pick Folder")
        self.choose_color_btn = QPushButton("Choose Color")
        self.review_note_btn = QPushButton("Enter Review Note")
        self.font_btn = QPushButton("Choose Font")
        self.confirm_btn = QPushButton("Confirm Settings")

        # Connect buttons to functions
        self.pick_folder_btn.clicked.connect(self.open_file_dialog)
        self.choose_color_btn.clicked.connect(self.pick_color)
        self.review_note_btn.clicked.connect(self.get_user_input)
        self.font_btn.clicked.connect(self.pick_font)
        self.confirm_btn.clicked.connect(self.show_confirmation)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.pick_folder_btn)
        layout.addWidget(self.choose_color_btn)
        layout.addWidget(self.review_note_btn)
        layout.addWidget(self.font_btn)
        layout.addWidget(self.confirm_btn)
        layout.addWidget(self.display_label)
        self.setLayout(layout)
        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

    def open_file_dialog(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Images (*.png *.jpg *.exr)")
        if self.file_path:
            self.display_label.setText(f"Selected file:\n{self.file_path}")

    def show_confirmation(self):
        response = QMessageBox.question(self, "Confirm Settings", "Are you sure you want to apply the settings")
        if response == QMessageBox.Yes:
            # File check path
            file_text = self.file_path if self.file_path else "No file selected"

            # Note if entered 
            note_text = self.name if self.name else "No note entered"

            # Color is selected 
            if self.color and self.color.isValid():
                color_text = self.color.name()
            else:
                color_text = "No color selected"

            # Font
            if self.font:
                font_text = f"{self.font.family()} ({self.font.pointSize()}pt)"
            else:
                font_text = "No font selected"

            summary = f"""\nSettings Applied:\nPreview Folder:{file_text}\nNote: {note_text}\nColor: {color_text}\nFont: {font_text} """
            self.display_label.setText(summary)

        else:
            self.display_label.setText("User canceled deletion.")

    def pick_color(self):
        self.color = QColorDialog.getColor()
        if self.color.isValid():
            self.display_label.setStyleSheet(f"color: {self.color.name()}")
            self.display_label.setText(f"Selected color: {self.color.name()}")

    def pick_font(self):
        ok, self.font = QFontDialog.getFont()
        # print(self.font)
        # print(ok)
        if ok:
            # self.display_label.setFont(self.font)
            self.display_label.setText(f"Selected font: {self.font.family()} ({self.font.pointSize()}pt)")

    def get_user_input(self):
        self.name, ok = QInputDialog.getText(self, "Enter Review Note", "Write Note?")
        if ok:
            self.display_label.setText(f"Hello, {self.name}!")
            print(self.name)

def show_inputdialog_menu(*args):
    global my_window
    try:
        my_window.close()
        my_window.deleteLater()
    except:
        pass

    maya_main_window = get_maya_main_window()
    my_window = DialogTool(parent=maya_main_window)
    my_window.show()

def create_dockable_widget():
    global dock_widget

    dock_name = "FileDialogWidget"

    # Remove old dock
    if cmds.workspaceControl(dock_name, exists=True):
        cmds.deleteUI(dock_name)

    workspace_control = cmds.workspaceControl(dock_name, label="My Dockable Widget", retain=False)
    cmds.workspaceControl(workspace_control, edit=True, dockToControl=("Outliner", "right"))

    ptr = omui.MQtUtil.findControl(workspace_control)
    workspace_control_widget = shiboken2.wrapInstance(int(ptr), QWidget)
    dock_widget = DialogTool()

    layout = workspace_control_widget.layout()
    if layout:
        layout.addWidget(dock_widget)

    return dock_widget

def custom_menu():
    menu_name = "AllToolsMenu"
    menu_label = "All_Tools"
    if cmds.menu(menu_name, exists=True):
        cmds.deleteUI(menu_name, menu=True)
    
    custom_menu = cmds.menu(menu_name, label=menu_label, parent="MayaWindow")
    cmds.menuItem(label="All Tools Panel", parent=custom_menu, command=lambda _: create_dockable_widget())

custom_menu()
