import sys
from PySide2.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLineEdit, QLabel, QPushButton
)
from PySide2.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("QGridLayout Example")
        self.resize(400, 200)

        self.name_label = QLabel("Name", self)
        self.email_label = QLabel("Email", self)

        self.name_input = QLineEdit()
        self.email_input = QLineEdit()

        submit_button = QPushButton("Submit")

        # Placeholder text
        self.name_input.setPlaceholderText("Enter your name")
        self.email_input.setPlaceholderText("Enter your email")

        # Grid Layout
        layout = QGridLayout()

        # Add widgets to layout
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.name_input, 0, 1)

        layout.addWidget(self.email_label, 1, 0)
        layout.addWidget(self.email_input, 1, 1)
        layout.addWidget(submit_button, 2, 0, 1, 2)

        layout.setHorizontalSpacing(15)
        layout.setVerticalSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Stretch columns for responsiveness
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 3)


        # Stretch last row
        layout.setRowStretch(3, 1)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet("""
    QLineEdit{
            background-color: #2e2e20; 
            color: #ffffff;
            font-size: 10px;
    }
    """)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())