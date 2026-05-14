from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel
from PySide2.QtCore import Qt  #

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        form_layout = QFormLayout()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        # Customize label alignment
        self.username_label.setAlignment(Qt.AlignBottom)  
        self.email_label.setAlignment(Qt.AlignBottom)  

        # Add widgets to the form layout
        form_layout.addRow(self.username_label, self.username_input)
        form_layout.addRow(self.email_label, self.email_input)

        # Set the form layout to the window
        self.setLayout(form_layout)

if __name__ == "__main__":
    app = QApplication([])

    window = MyWindow()
    window.show()

    app.exec_()