from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QTextEdit, QDockWidget, QToolBar, QAction, QWidget,
    QStatusBar, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout
)

from PySide2.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Layout All Example")
        self.setGeometry(200, 200, 800, 600)

        # menu bar 
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.open_btn = self.file_menu.addAction("Open")
        self.file_menu.addSeparator()
        self.save_btn = self.file_menu.addAction("Save")
        self.file_menu.addAction("Exit")

        # shortcuts
        self.open_btn.setShortcut("Ctrl+O")
        self.save_btn.setShortcut("Ctrl+S")

        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.copy_btn = self.edit_menu.addAction("Copy")
        self.paste_btn = self.edit_menu.addAction("Paste")

        self.view_menu = self.menu_bar.addMenu("View")
        self.toggle_dock = self.view_menu.addAction("Toggle Dock")

        # shortcuts
        self.copy_btn.setShortcut("Ctrl+C")
        self.paste_btn.setShortcut("Ctrl+V")

        # Tool bar 
        self.toolbar = QToolBar("Main Toolbar") 
        # self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

        action_a = QAction("Action A", self)
        self.toolbar.addAction(action_a)

        action_b = QAction("Action B", self)
        self.toolbar.addAction(action_b)

        # central widget 
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # nested layout 
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")

        self.h_layout.addWidget(self.button1)
        self.h_layout.addWidget(self.button2)

        self.v_layout.addLayout(self.h_layout)

        # grid Layout 
        self.grid_layout = QGridLayout()
        
        button3 = QPushButton("Spanning Button")
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")
        button6 = QPushButton("Button 6")

        self.grid_layout.addWidget(button3, 0, 0)
        self.grid_layout.addWidget(button4, 0, 1)
        self.grid_layout.addWidget(button5, 1, 0)
        self.grid_layout.addWidget(button6, 1, 1)

        self.v_layout.addLayout(self.grid_layout)

        self.central_widget.setLayout(self.v_layout)

        # connection 
        self.open_btn.triggered.connect(self.open_file)
        self.copy_btn.triggered.connect(self.copy_action)
        self.toggle_dock.triggered.connect(self.copy_action)
        
        # dock toolbar
        self.dock = QDockWidget("Dock Panel", self)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.BottomDockWidgetArea | Qt.TopDockWidgetArea)
        self.dock.setWidget(QLabel("This is a Dock Widget"))
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # status bar  widget 
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Ready")
        self.setStatusBar(self.status_bar)
    
    def open_file(self):
        print("File is opening")
        self.status_bar.showMessage("File is opening")

    def copy_action(self):
        print("Copied to clipboard.")
        self.status_bar.showMessage("Copied to Clipboard")

    def copy_action(self):
        is_visible = self.dock.isVisible()
        self.dock.setVisible(not is_visible)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())