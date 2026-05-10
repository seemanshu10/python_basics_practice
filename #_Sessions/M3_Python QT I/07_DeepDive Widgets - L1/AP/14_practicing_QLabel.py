import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

from PySide2.QtCore import Qt

class CompleteQLabelExample(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("Complete QLabel Example")
        self.resize(350, 300)

        # Main layout
        main_layout = QVBoxLayout()

        self.text_label = QLabel("Hello, VFX World!")

        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setWordWrap(True)

        self.text_label.setToolTip("Greeting message")

        self.text_label.setStyleSheet("""
            QLabel {
                background-color: #2d2d2d;
                color: white;
                padding: 10px;
                border: 2px solid #555;
                border-radius: 5px;
                font-size: 14px;
            }
        """)

        main_layout.addWidget(self.text_label)

        html_label = QLabel("<b>Current Frame:</b> <i>1001</i>")

        html_label.setTextFormat(Qt.RichText)
        html_label.setAlignment(Qt.AlignLeft)

        main_layout.addWidget(html_label)

        link_label = QLabel('<a href="https://vfx.io">Visit VFX Site</a>')

        link_label.setOpenExternalLinks(True)

        main_layout.addWidget(link_label)
        # Button
        update_button = QPushButton("Update Text")
        update_button.clicked.connect(self.update_label)
        main_layout.addWidget(update_button)

        # Set layout
        self.setLayout(main_layout)

    def update_label(self):
        self.text_label.setText("Rendering frame 1002...")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CompleteQLabelExample()
    window.show()

    sys.exit(app.exec_())