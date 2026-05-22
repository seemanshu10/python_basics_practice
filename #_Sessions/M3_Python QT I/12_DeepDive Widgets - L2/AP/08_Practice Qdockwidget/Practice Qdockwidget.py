# Practice QDockWidget
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,QPushButton, QLabel, QAction, QToolBar, QDockWidget, QLineEdit
)

from PySide2.QtCore import Qt, Slot
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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

        
if __name__ == "__main__":

    app = QApplication()
    window = MainWindow()
    window.show()
    # window.resize()
    sys.exit(app.exec_())