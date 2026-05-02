import sys
import time
from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
)


def load_asset_by_name(asset_name):
    """Simulates loading an asset by name. Replace with actual loader."""
    time.sleep(1)  # Simulate loading delay
    return bool(asset_name)


class AssetLoaderUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asset Loader")
        self.setFixedSize(300, 150)
        self._build_ui()

    def _build_ui(self):
        self.asset_input = QLineEdit()
        self.asset_input.setPlaceholderText("Enter asset name or ID")

        self.load_button = QPushButton("Load Asset")
        self.load_button.clicked.connect(self._on_load_clicked)

        self.status_label = QLabel("Status: Waiting for input")

        layout = QVBoxLayout()
        layout.addWidget(self.asset_input)
        layout.addWidget(self.load_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def _on_load_clicked(self):
        asset_name = self.asset_input.text().strip()

        if not asset_name:
            self.status_label.setText("Error: Asset name is required.")
            return

        self.status_label.setText(f"Loading asset '{asset_name}'...")
        self.load_button.setEnabled(False)

        success = load_asset_by_name(asset_name)

        if success:
            self.status_label.setText(f"Asset '{asset_name}' loaded successfully.")
            self.asset_input.clear()
        else:
            self.status_label.setText(f"Failed to load asset '{asset_name}'.")

        self.load_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AssetLoaderUI()
    window.show()
    sys.exit(app.exec_())