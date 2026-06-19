from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QDockWidget, QToolBar, QAction, QWidget, QSplitter, QSpinBox,QStatusBar, QVBoxLayout, QPushButton, QFormLayout, QScrollArea, QDoubleSpinBox, QTreeView, QListView, QTableView, QFileDialog, QColorDialog, QFontDialog
)
from PySide2.QtCore import Qt, QStringListModel, Slot
from PySide2.QtGui import QStandardItemModel, QStandardItem, QPixmap
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
        self.setWindowTitle("VFX Utility Panel")
        self.setGeometry(200, 200, 820, 650)
        self.menubar()                      # menu bar 
        self.toolbar()                      # toolbar
        self.central_main_widget()          # central widget

        self.status_bar()                   # status bar   

    def menubar(self):
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.open_btn = self.file_menu.addAction("Open")
        self.save_btn = self.file_menu.addAction("Save")
        self.file_menu.addSeparator()
        self.exit_option = self.file_menu.addAction("Exit")

        # shortcuts
        self.open_btn.setShortcut("Ctrl+O")
        self.save_btn.setShortcut("Ctrl+S")

        # connections 
        self.exit_option.triggered.connect(self.close)

    def toolbar(self):

        self.main_toolbar = QToolBar()
        self.addToolBar(self.main_toolbar)
        
        self.add_exit = QAction("Exit", self)
        self.main_toolbar.addAction(self.add_exit)

        # connections 
        self.add_exit.triggered.connect(self.close)

    def central_main_widget(self):
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()

        self.splitter_central = QSplitter(Qt.Horizontal)

        self.editor1 = self.main_dock_widget()
        self.editor2 = self.scroll_area_widget()

        self.splitter_central.addWidget(self.editor1)
        self.splitter_central.addWidget(self.editor2)

        self.splitter_central.setSizes([250, 450])
        self.central_layout.addWidget(self.splitter_central)

        self.central_widget.setLayout(self.central_layout)

        self.setCentralWidget(self.central_widget)

    # Left Side Widget 
    def main_dock_widget(self):
        self.dock = QDockWidget("Asset Browser")
        self.dock_widget = QWidget()
        self.dock_layout = QVBoxLayout()

        self.asset_tree()
        self.asset_list()
        self.asset_table()

        self.dock_widget.setLayout(self.dock_layout)
        self.dock.setWidget(self.dock_widget)

        self.splitter_central.addWidget(self.dock)

        return self.dock
    
    def asset_tree(self):

        self.tree_view = QTreeView()
        self.tree_model = QStandardItemModel()
        self.tree_model.setHorizontalHeaderLabels(["Asset Hierarchy"])
        
        self.characters_item = QStandardItem("Character")
        self.characters_item.appendRow(QStandardItem("Assets"))
        self.characters_item.appendRow(QStandardItem("Scripts"))

        self.environment_item = QStandardItem("Environment")
        self.environment_item.appendRows([QStandardItem("Forest"), QStandardItem("City")])

        self.tree_model.appendRow(self.characters_item)
        self.tree_model.appendRow(self.environment_item)
        self.tree_view.setModel(self.tree_model)

        self.dock_layout.addWidget(self.tree_view)

    def asset_list(self):

        self.list_view = QListView()
        self.list_asset_item = QStringListModel(["Characters", "Props", "Environments"])
    
        self.list_view.setModel(self.list_asset_item)
        self.dock_layout.addWidget(self.list_view)

    def asset_table(self):
        self.table_view = QTableView()

        self.table_model = QStandardItemModel(3, 3)
        self.table_model.setHorizontalHeaderLabels(["Name", "Version", "Status"])
        self.table_view.setModel(self.table_model)

        mock_data = [
            ["Hero", "v001", "Approved"],
            ["City", "v003", "Pending"],
            ["ExplosionFX", "v002", "In Progress"],
            ["FireFX", "v006", "Approved"],
            ["Pipe Wet", "v005", "Pending"]
        ]

        for row, data in enumerate(mock_data):
            for column, value in enumerate(data):
                item = QStandardItem(value)
                self.table_model.setItem(row, column, item)

        self.dock_layout.addWidget(self.table_view)

    # Right Widget
    def scroll_area_widget(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.right_widget = QWidget()
        self.form_layout = QFormLayout()

        # spin box 
        self.frame_spin_box = QSpinBox()
        self.frame_spin_box.setRange(1, 10000)
        self.frame_spin_box.setValue(100)

        # Double Spin box 
        self.opacity_spin_box = QDoubleSpinBox()
        self.opacity_spin_box.setSingleStep(0.05)

        self.form_layout.addRow("Frame: ", self.frame_spin_box)
        self.form_layout.addRow("Opacity: ", self.opacity_spin_box)

        self.right_widget.setLayout(self.form_layout)
        scroll_area.setWidget(self.right_widget)

        self.button_create()
        self.form_layout.setSpacing(20) # set spacing for buttons 
        self.image_label_create()

        return scroll_area

    def button_create(self):
        
        # button create 
        self.load_image_btn = QPushButton("Load Image")
        self.choose_color_btn = QPushButton("Choose Color")
        self.choose_font_btn = QPushButton("Choose Font")

        self.form_layout.addRow(self.load_image_btn)
        self.form_layout.addRow(self.choose_color_btn)
        self.form_layout.addRow(self.choose_font_btn)

        # button connection 
        self.load_image_btn.clicked.connect(self.load_image)        # load image function
        self.choose_color_btn.clicked.connect(self.select_color)  
        self.choose_font_btn.clicked.connect(self.select_font)  

    @Slot()
    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if file_name: 
            pixmap = QPixmap(file_name)

            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    self.image_label.width(),
                    self.image_label.height(),
                )
                self.image_label.setPixmap(scaled_pixmap)
                print(f"Loaded File: {file_name}")
                self.statusbar.showMessage(f"Loaded File: {file_name}")

    @Slot()
    def select_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.image_label.setStyleSheet(f"color: {color.name()}")

            print(f"Selected color: {color.name()}")
            # self.statusbar.showMessage(f"Border Color: {color.name()}")

            self.image_label.setStyleSheet(f"""
            border: 5px solid {color.name()};
            background-color: #222;
            color: white;
            """)
            print(f"Selected font: {color.name()}")


            self.statusBar().showMessage(f"Color Applied {color.name()}")

    @Slot()
    def select_font(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.image_label.setFont(font)

            print(f"Selected font: {font.toString()}")
            self.statusBar().showMessage("Font Applied")

    def image_label_create(self):

        self.image_label = QLabel("No Image Loaded")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(500, 400)
        self.image_label.setStyleSheet("""
            border: 5px solid green;
            background-color: #222;
            color: white;
        """)

        self.form_layout.addRow(self.image_label)

    def status_bar(self):
        self.statusbar = QStatusBar()
        self.statusbar.showMessage("Ready")
        self.setStatusBar(self.statusbar)

def show_utility_menu(*args):
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

    cmds.menu("Main_Window", label="Window_Tool", parent="MayaWindow")
    cmds.menuItem(label="VFX App", command=show_utility_menu)

custom_menu()

