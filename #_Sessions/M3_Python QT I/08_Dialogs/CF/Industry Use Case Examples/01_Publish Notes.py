from PySide2.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication

class PublishNotesDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Publish Notes")

        self.label = QLabel("Describe this publish:")
        self.input_field = QLineEdit()
        self.submit_button = QPushButton("Submit")

        self.submit_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def get_notes(self):
        return self.input_field.text()

# Usage
if __name__ == "__main__":
    app = QApplication([])
    dialog = PublishNotesDialog()
    if dialog.exec_():
        print("Publish Notes:", dialog.get_notes())