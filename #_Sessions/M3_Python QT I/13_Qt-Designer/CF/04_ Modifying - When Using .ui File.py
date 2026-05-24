import sys
import os
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PySide2.QtUiTools import QUiLoader
class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file directly using QUiLoader
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_path = os.path.join(script_dir, "simple_ui.ui")
        
        # Use QUiLoader to load the UI from the .ui file directly
        loader = QUiLoader()
        self.ui = loader.load(ui_file_path, self)

           
        
        self.setup_ui()
    
    def setup_ui(self):
        layout_widget = self.ui.findChild(QWidget, "verticalLayoutWidget")
        if layout_widget:
            layout = layout_widget.findChild(QVBoxLayout, "verticalLayout")
            if layout:
                layout_widget.setLayout(layout)
        
        # Modify UI elements and connect slots
        self.modify_label_text()
        self.toggle_button_visibility()
        self.enable_disable_button()
        self.add_button_click_handler()
        
        self.add_new_widget()
    
    # Changing the text of a label
    def modify_label_text(self):
        label = self.ui.findChild(QLabel, "label_name")
        if label:
            label.setText("Please enter your Name :")
    
    # Changing widget visibility
    def toggle_button_visibility(self):
        button = self.ui.findChild(QPushButton, "button_name")
        if button:
            button.setVisible(True)  # Ensure the button is visible
    
    # Enabling/disabling widgets
    def enable_disable_button(self):
        button = self.ui.findChild(QPushButton, "button_name")
        if button:
            button.setEnabled(True)  # Ensure the button is enabled
    
    # Adding button click handler (Signal & Slot)
    def add_button_click_handler(self):
        button = self.ui.findChild(QPushButton, "button_name")
        if button:
            button.clicked.connect(self.on_button_click)
    
    # Adding a new widget to the UI dynamically
    def add_new_widget(self):
        new_button = QPushButton("New Button")
        
        layout_widget = self.ui.findChild(QWidget, "verticalLayoutWidget")

        if layout_widget:
            layout = layout_widget.findChild(QVBoxLayout, "verticalLayout")
            if layout:
                layout.addWidget(new_button)


    def on_button_click(self):
        print("Button was clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())