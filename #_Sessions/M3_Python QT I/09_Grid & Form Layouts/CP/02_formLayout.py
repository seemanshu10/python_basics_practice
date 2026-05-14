from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the form layout
        form_layout = QFormLayout()

        # Create widgets 
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        # Add widgets 
        form_layout.addRow(self.username_label, self.username_input)
        form_layout.addRow(self.email_label, self.email_input)

        # Set the form layout to the window
        self.setLayout(form_layout)

if __name__ == "__main__":
    app = QApplication()

    window = MyWindow()
    window.show()

    app.exec_()