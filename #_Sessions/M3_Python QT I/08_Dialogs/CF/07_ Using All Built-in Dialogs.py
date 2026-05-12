from PySide2.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QFileDialog, QMessageBox, QColorDialog, QFontDialog, QInputDialog, QLabel
)
from PySide2.QtGui import QFont, QColor
import sys


class DialogTool(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VFX Dialog Demo Tool")

        # Label to show selected name and styling
        self.display_label = QLabel("Your output will appear here.")
        self.display_label.setWordWrap(True)

        # Buttons to trigger each dialog
        self.file_button = QPushButton("Pick a File")
        self.confirm_button = QPushButton("Confirm Action")
        self.color_button = QPushButton("Pick a Color")
        self.font_button = QPushButton("Pick a Font")
        self.input_button = QPushButton("Enter Name")

        # Connect buttons to functions
        self.file_button.clicked.connect(self.open_file_dialog)
        self.confirm_button.clicked.connect(self.show_confirmation)
        self.color_button.clicked.connect(self.pick_color)
        self.font_button.clicked.connect(self.pick_font)
        self.input_button.clicked.connect(self.get_user_input)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.file_button)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.color_button)
        layout.addWidget(self.font_button)
        layout.addWidget(self.input_button)
        layout.addWidget(self.display_label)
        self.setLayout(layout)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Images (*.png *.jpg *.exr)")
        if file_path:
            self.display_label.setText(f"Selected file:\n{file_path}")

    def show_confirmation(self):
        response = QMessageBox.question(self, "Delete File", "Are you sure you want to delete this file?")
        if response == QMessageBox.Yes:
            self.display_label.setText("User confirmed deletion.")
        else:
            self.display_label.setText("User canceled deletion.")

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.display_label.setStyleSheet(f"color: {color.name()}")
            self.display_label.setText(f"Selected color: {color.name()}")

    def pick_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.display_label.setFont(font)
            self.display_label.setText(f"Selected font: {font.family()} ({font.pointSize()}pt)")

    def get_user_input(self):
        name, ok = QInputDialog.getText(self, "Enter Name", "What's your name?")
        if ok:
            self.display_label.setText(f"Hello, {name}!")


# Run the tool
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DialogTool()
    window.show()
    sys.exit(app.exec_())