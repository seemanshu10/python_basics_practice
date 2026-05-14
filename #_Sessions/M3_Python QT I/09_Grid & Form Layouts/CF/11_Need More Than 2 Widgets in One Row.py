from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QHBoxLayout, QLineEdit, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        form_layout = QFormLayout()

        # Create a horizontal layout to hold two widgets
        row_layout = QHBoxLayout()
        row_layout.addWidget(QLineEdit("First Name"))
        row_layout.addWidget(QLineEdit("Last Name"))

        # Add row: one label, one horizontal layout
        form_layout.addRow(QLabel("Full Name:"), row_layout)

        self.setLayout(form_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()