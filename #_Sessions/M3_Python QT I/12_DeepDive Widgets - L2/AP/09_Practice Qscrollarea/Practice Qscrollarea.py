# Practice QInputDialog

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QScrollArea
)
from PySide2.QtCore import Slot, Qt

class InputDialogWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QScrollArea Practice")
        self.resize(400, 500)

        main_layout = QVBoxLayout()
        self.scroll_button = QPushButton("Scroll to Bottom")
        main_layout.addWidget(self.scroll_button)

        # Scroll Area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Scrollbar beahaviour
        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarAsNeeded
        )
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        # Content widget inside scroll area
        content_widget = QWidget()
        content_layout = QVBoxLayout()

        # Add label
        for i in range(1, 31):
            label = QLabel(f"Item {i}")
            content_layout.addWidget(label)

        content_widget.setLayout(content_layout)
        self.scroll_area.setWidget(content_widget)

        # Style scroll area
        self.scroll_area.setStyleSheet("""
        QScrollArea {
            background-color: #2c2c2c;
        }
        QScrollBar:vertical {
            background: #444;
            width: 10px;
        }
        """)

        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

        # connections Slots
        self.scroll_button.clicked.connect(self.scroll_to_bottom)

        # Track scrollbar moving
        self.scroll_area.verticalScrollBar().valueChanged.connect(
            self.print_scroll_value
        )

    @Slot()
    def scroll_to_bottom(self):
        self.scroll_area.ensureVisible(0, 10000)

    def print_scroll_value(self, value):
        print(f"Scroll position: {value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = InputDialogWindow()
    window.show()

    sys.exit(app.exec_())