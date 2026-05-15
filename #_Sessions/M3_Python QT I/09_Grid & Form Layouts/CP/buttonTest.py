import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QSizePolicy,
)
from PySide2.QtCore import Qt


class DashboardUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide2 Button Layout")
        self.resize(900, 600)

        # Main layout
        layout = QGridLayout()
        # layout.setSpacing(15)
        # layout.setContentsMargins(20, 20, 20, 20)

        # Create buttons
        btn1 = self.create_button("Button 1")
        btn2 = self.create_button("Button 2")
        btn3 = self.create_button("Button 3")

        btn4 = self.create_button("Button 4")
        btn5 = self.create_button("Wide Button")

        btn6 = self.create_button("Button 6")
        btn7 = self.create_button("Large Panel")

        btn8 = self.create_button("Button 8")

        # Top row
        layout.addWidget(btn1, 0, 0)
        layout.addWidget(btn2, 0, 1)
        layout.addWidget(btn3, 0, 2)

        # Middle row
        layout.addWidget(btn4, 1, 0)
        layout.addWidget(btn5, 1, 1, 1, 2)

        # Bottom section
        layout.addWidget(btn6, 2, 0)
        layout.addWidget(btn7, 2, 1, 2, 2)

        layout.addWidget(btn8, 3, 0)

        # Row stretch for better proportions
        # layout.setRowStretch(0, 1)
        # layout.setRowStretch(1, 1)
        # layout.setRowStretch(2, 2)
        # layout.setRowStretch(3, 1)

        # Column stretch
        # layout.setColumnStretch(0, 1)
        # layout.setColumnStretch(1, 1)
        # layout.setColumnStretch(2, 1)

        self.setLayout(layout)

        # Style
        self.setStyleSheet("""
            QWidget {
                background-color: #f2f2f2;
            }

            QPushButton {
                border: 2px solid #333;
                border-radius: 20px;
                background-color: white;
                font-size: 16px;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: #dfefff;
            }

            QPushButton:pressed {
                background-color: #c5ddff;
            }
        """)

    def create_button(self, text):
        btn = QPushButton(text)
        # set size policy sets the button as neded 
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        return btn


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DashboardUI()
    window.show()

    sys.exit(app.exec_())