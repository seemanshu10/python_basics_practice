import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
import qdarkstyle
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QFont

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.apply_dark_theme()
        self.setWindowTitle("Complete QListWidget Example")

        # Create widgets
        self.status_label = QLabel("Select a shot:")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))

        # QListWidget
        self.list_widget = QListWidget()
        self.list_widget.addItems([
            "Shot001",
            "Shot002",
            "Shot003"
        ])

        # enable muiltiselection
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)
        
        # Button Added 
        
        self.state_button = QPushButton("Print Selected Items")
        self.clear_button = QPushButton("Clear List")

        self.state_button.setStyleSheet("""
        QPushButton{
            
            border: 2px solid #888888;
            border-radius: 5px;
            color: #ffffff;
            padding: 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #555555; 
        }
        QPushButton:pressed {
            background-color: #b91f1f;
            border: 2px solid #ffffff;
        }                                     
        """)

        self.clear_button.setStyleSheet("""
        QPushButton{
            background-color: red;
            border: 2px solid #888888;
            border-radius: 5px;
            color: #ffffff;
            padding: 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #555555; 
        }
        QPushButton:pressed {
            background-color: #b91f1f;
            border: 2px solid #ffffff;
        }                                     
        """)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.list_widget)
        main_layout.addWidget(self.state_button)
        main_layout.addWidget(self.clear_button)
        self.setLayout(main_layout)

        # connections 
        self.list_widget.itemClicked.connect(self.selected_item)
        self.list_widget.itemDoubleClicked.connect(self.selected_multiple_item)
        self.state_button.clicked.connect(self.print_selected_items)
        self.clear_button.clicked.connect(self.clear_list)
    
    def selected_multiple_item(self, value):
        value_item = value.text()
        self.status_label.setText(f"Double-clicked: {value_item}")
        print(f"Clicked: {value_item}")

    def selected_item(self, value):
        value_item = value.text()
        self.status_label.setText(f"Selected Item: {value_item}")
        print(f"Clicked: {value_item}")

    def clear_list(self):
        print("List Cleared.")
        self.list_widget.clear()
        self.status_label.setText("List Cleared")

    def print_selected_items(self):
        selected_items = self.list_widget.selectedItems()

        if selected_items:
            names = []

            for item in selected_items:
                names.append(item.text())

            print("Selected Items:")
            for name in names:
                print(name)

            self.status_label.setText(f"Printed: {names}")

        else:
            print("No items selected.")
            self.status_label.setText("No items selected.")

    def pressed_slider(self):
        print("Slider Pressed.")

    def update_slider(self, value):
        self.status_label.setText(f"Opacity: {value}%")
        print(f"Value Changed: {value}")
    
    def moved_slider(self, value):
        # self.status_label.setText(f"Opacity: {value}%")
        print(f"Slider Moved To: {value}")

    @Slot()
    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(400, 200)
    window.show()
    app.exec_()