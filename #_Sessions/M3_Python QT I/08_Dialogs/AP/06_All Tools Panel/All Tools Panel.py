# Tool Configuration Panel
from PySide2.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QFileDialog, QMessageBox, QColorDialog, QFontDialog, QInputDialog, QLabel
)
from PySide2.QtGui import QFont, QColor
import sys


class DialogTool(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget-based panel")
        self.resize(200, 200)

        # Label to show selected name and styling
        self.display_label = QLabel("Your output will appear here.")
        self.display_label.setWordWrap(True)

        # Buttons to trigger each dialog
        self.pick_folder_btn = QPushButton("Pick Folder")
        self.choose_color_btn = QPushButton("Choose Color")
        self.review_note_btn = QPushButton("Enter Review Note")
        self.font_btn = QPushButton("Choose Font")
        self.confirm_btn = QPushButton("Confirm Settings")

        # Connect buttons to functions
        self.pick_folder_btn.clicked.connect(self.open_file_dialog)
        self.choose_color_btn.clicked.connect(self.pick_color)
        self.review_note_btn.clicked.connect(self.get_user_input)
        self.font_btn.clicked.connect(self.pick_font)
        self.confirm_btn.clicked.connect(self.show_confirmation)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.pick_folder_btn)
        layout.addWidget(self.choose_color_btn)
        layout.addWidget(self.review_note_btn)
        layout.addWidget(self.font_btn)
        layout.addWidget(self.confirm_btn)
        layout.addWidget(self.display_label)
        self.setLayout(layout)

    def open_file_dialog(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Images (*.png *.jpg *.exr)")
        if self.file_path:
            self.display_label.setText(f"Selected file:\n{self.file_path}")

    def show_confirmation(self):
        response = QMessageBox.question(self, "Confirm Settings", "Are you sure you want to apply the settings")
        if response == QMessageBox.Yes:
            
            summary = f"""\n✅ Settings Applied:\nPreview Folder:{self.file_path}\nNote: {self.name}\nColor: {self.color.name()}\n Font """
            self.display_label.setText(summary)
        else:
            self.display_label.setText("User canceled deletion.")

    def pick_color(self):
        self.color = QColorDialog.getColor()
        if self.color.isValid():
            # self.display_label.setStyleSheet(f"color: {color.name()}")
            self.display_label.setText(f"Selected color: {self.color.name()}")

    def pick_font(self):
        self.font, ok = QFontDialog.getFont()
        if ok:
            self.display_label.setFont(self.font)
            self.display_label.setText(f"Selected font: {self.font.family()} ({self.font.pointSize()}pt)")

    def get_user_input(self):
        self.name, ok = QInputDialog.getText(self, "Enter Review Note", "Write Note?")
        if ok:
            self.display_label.setText(f"Hello, {self.name}!")
            print(self.name)
# TODO: Handle Edge case when some inputs are missing 
# Run the tool
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DialogTool()
    window.resize(300, 300)
    window.show()
    sys.exit(app.exec_())