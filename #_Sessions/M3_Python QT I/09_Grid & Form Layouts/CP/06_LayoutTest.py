from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTabWidget,
    QLabel, 
    QPushButton, 
    QGridLayout, 
    QGroupBox, 
    QLineEdit, 
    QTextEdit,
    QFormLayout,
    QComboBox, 
    QSpinBox,
    QSizePolicy
)

import qdarkstyle
class GridWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.apply_dark_theme()
        self.setWindowTitle("File TabWidget")
        
        self.tabs = QTabWidget(self)
        self.file_tab = QWidget()
        self.main_layout = QVBoxLayout()

        # Add QLabel widget
        label = QLabel("Horizontal Layout")
        grid_label = QLabel("Grid Layout")
        form_label = QLabel("Form Layout")

        # create and add widgets to main layout
        self.main_layout.addWidget(label)
        self.horizontal_layout_func()
        self.main_layout.addWidget(grid_label)
        self.grid_layout_func()
        self.main_layout.addWidget(form_label)
        self.form_layout_func()
        self.last_widget()
        self.bottom_button()

        # Set layout to file tab
        self.file_tab.setLayout(self.main_layout)
        
        # Add tab to tab widget
        self.tabs.addTab(self.file_tab, "File")
        
    def horizontal_layout_func(self):
        
        self.layout1 = QHBoxLayout()
        
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")
        self.button4 = QPushButton("Button 4")

        self.layout1.addWidget(self.button1)
        self.layout1.addWidget(self.button2)
        self.layout1.addWidget(self.button3)
        self.layout1.addWidget(self.button4)

        self.main_layout.addLayout(self.layout1)

    def grid_layout_func(self):
        self.grid_layout = QGridLayout()

        # creating Widgets 
        self.label_line1 = QLabel("Line 1: ")
        self.line_line1 = QLineEdit()
        self.label_line2 = QLabel("Line 2: ")
        self.line_line2 = QLineEdit()
        self.label_line3 = QLabel("Line 3: ")
        self.line_line3 = QLineEdit()
        
        self.text_box = QTextEdit()
        self.text_box.setPlaceholderText("This widget takes up about two\n"
            "thirds of the grid layout.")

        self.grid_layout.addWidget(self.label_line1, 0, 0)
        self.grid_layout.addWidget(self.line_line1, 0, 1)
        self.grid_layout.addWidget(self.label_line2, 1, 0)
        self.grid_layout.addWidget(self.line_line2, 1, 1)
        self.grid_layout.addWidget(self.label_line3, 2, 0)
        self.grid_layout.addWidget(self.line_line3, 2, 1)

        self.grid_layout.addWidget(self.text_box, 0, 2, 3, 1)

        self.main_layout.addLayout(self.grid_layout)

    def form_layout_func(self):

        # Initialize the form layout
        self.form_layout = QFormLayout()

        # Create widgets 
        self.line1_label = QLabel("Line 1:")
        self.line1_input = QLineEdit()

        self.line2_label = QLabel("Line 2, Long Text:")
        self.line2_input = QComboBox()

        self.line3_label = QLabel("Line 3: ")
        self.line3_spin = QSpinBox()

        # add Widgets 
        self.form_layout.addRow(self.line1_label, self.line1_input)
        self.form_layout.addRow(self.line2_label, self.line2_input)
        self.form_layout.addRow(self.line3_label, self.line3_spin)
        
        self.main_layout.addLayout(self.form_layout)

    def last_widget(self):
        self.bottom_text = QTextEdit()
        self.bottom_text.setPlainText(
            "This widget takes up all the remaining space "
            "in the top-level layout."
        )

        self.bottom_text.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        self.main_layout.addWidget(self.bottom_text)

    def bottom_button(self):
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")

        button_layout.addWidget(ok_btn)
        button_layout.addWidget(cancel_btn)

        self.main_layout.addLayout(button_layout)

    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)

if __name__ == "__main__":

    app = QApplication([])

    window = GridWindow()
    window.setFixedSize(460, 510)
    window.show()

    app.exec_()