import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QFileDialog
)


class FilePickerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom QFileDialog Example")
        self.resize(500, 150)

        # Layout
        layout = QVBoxLayout()

        # Widgets
        self.path_edit = QLineEdit()
        self.browse_button = QPushButton("Browse")
        self.status_label = QLabel("Status: Waiting for input...")

        # Add widgets to layout
        layout.addWidget(self.path_edit)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        # Button connection
        self.browse_button.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        # Create custom QFileDialog
        dialog = QFileDialog(self)

        #  dialog
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Images (*.exr *.png *.jpg)")
        dialog.setDirectory("./assets")
        dialog.selectFile("sample.exr")
        dialog.setViewMode(QFileDialog.Detail)
        dialog.setOption(QFileDialog.ShowDirsOnly, False)

        # Apply stylesheet
        dialog.setStyleSheet("QFileDialog { font-size: 14px; }")

        # Signals
        dialog.fileSelected.connect(self.on_file_selected)
        dialog.currentChanged.connect(self.on_current_changed)
        dialog.directoryEntered.connect(self.on_directory_entered)
        dialog.filterSelected.connect(self.on_filter_selected)

        # Executes the dialog modally.
        dialog.exec_()

    # Signal callbacks
    def on_file_selected(self, file_path):
        print("File selected:", file_path)

        self.path_edit.setText(file_path)
        self.status_label.setText(f"File Selected: {file_path}")

    def on_current_changed(self, path):
        print("Current file:", path)

    def on_directory_entered(self, directory):
        print("Entered dir:", directory)

    def on_filter_selected(self, selected_filter):
        print("Filter:", selected_filter)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = FilePickerWindow()
    window.show()

    sys.exit(app.exec_())