import sys
from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit,
    QLabel, QPushButton, QHBoxLayout
)

DEFAULT_SHOT = "shot010"
DEFAULT_VERSION = "v001"
DEFAULT_EXT = ".mov"


def build_playblast_filename(override_name):
    if override_name.strip():
        return f"{override_name.strip()}{DEFAULT_EXT}"
    return f"{DEFAULT_SHOT}_{DEFAULT_VERSION}{DEFAULT_EXT}"


class PlayblastNamingHelper(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Playblast Naming Helper")
        self.setFixedSize(400, 150)
        self._init_ui()

    def _init_ui(self):
        self.override_input = QLineEdit()
        self.override_input.setPlaceholderText("Optional override filename")

        self.result_label = QLabel("Generated Filename: (click 'Generate')")

        self.generate_btn = QPushButton("Generate")
        self.generate_btn.clicked.connect(self._on_generate_clicked)

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.clicked.connect(self._on_reset_clicked)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Generate Playblast Filename"))
        layout.addWidget(self.override_input)
        layout.addWidget(self.result_label)

        button_row = QHBoxLayout()
        button_row.addWidget(self.generate_btn)
        button_row.addWidget(self.reset_btn)

        layout.addLayout(button_row)
        self.setLayout(layout)

    def _on_generate_clicked(self):
        override = self.override_input.text()
        filename = build_playblast_filename(override)
        self.result_label.setText(f"Generated Filename: {filename}")

    def _on_reset_clicked(self):
        self.override_input.clear()
        self.result_label.setText("Generated Filename: (click 'Generate')")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayblastNamingHelper()
    window.show()
    sys.exit(app.exec_())