import sys
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QScrollArea, QWidget,
    QVBoxLayout, QLabel, QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QScrollArea Example")

        # Create a widget with a vertical layout (this will go inside the scroll area)
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        # Add many widgets to simulate large content
        for i in range(30):
            layout.addWidget(QLabel(f"Label {i+1}"))
            layout.addWidget(QPushButton(f"Button {i+1}"))

        # Scroll Area setup
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # Let content resize with scroll area
        scroll_area.setWidget(content_widget)

        self.setCentralWidget(scroll_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(300, 400)
    window.show()
    app.exec_()