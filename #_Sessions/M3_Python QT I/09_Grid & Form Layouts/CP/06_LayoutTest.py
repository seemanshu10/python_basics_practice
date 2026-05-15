from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTabWidget,
    QLabel
)

import qdarkstyle
class GridWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.apply_dark_theme()
        self.setWindowTitle("File TabWidget")
        self.main_tab()
        self.hor_layout()

    def main_tab(self):
        self.main_layout = QVBoxLayout(self)

        # Create empty tab widget
        self.file_tab = QTabWidget()

        # Add empty tabs
        self.file_tab.addTab(QWidget(), "File")

        # Add tab widget to main layout
        self.main_layout.addWidget(self.file_tab)

    def hor_layout(self):
        self.hor_widget = QWidget()
        self.horizon_layout = QHBoxLayout()

        self.label = QLabel("Horizontal Layout")

        self.horizon_layout.addWidget(self.label)
        # Add tab widget to tab file
        
        self.hor_widget.setLayout(self.file_tab)
        # self.file_tab.addLayout(self.horizon_layout)
        # self.hor_widget.

    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)

if __name__ == "__main__":

    app = QApplication([])

    window = GridWindow()
    window.resize(600, 400)
    window.show()

    app.exec_()