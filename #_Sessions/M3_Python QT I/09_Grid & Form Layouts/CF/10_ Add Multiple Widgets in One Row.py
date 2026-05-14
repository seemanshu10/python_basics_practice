from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        form_layout = QFormLayout()

        # Create widgets
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()

        # Incorrect way
        form_layout.addRow(self.username_label, self.username_input, self.email_label)

        # # Correct way
        # form_layout.addRow(self.username_label, self.username_input)
        # form_layout.addRow(self.email_label, self.email_input)
        # form_layout.addRow(self.phone_label, self.phone_input)

        # Apply layout
        self.setLayout(form_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()