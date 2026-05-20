# Practice QMessageBox
import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QMessageBox
)

class MessageBoxWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessage Practice")
        self.resize(500, 150)

        # Layout
        layout = QVBoxLayout()

        # Widgets
        self.render_button = QPushButton("Delete Render Cache")

        # Add widgets to layout
        layout.addWidget(self.render_button)
    
        self.setLayout(layout)

        # Button connection
        self.render_button.clicked.connect(self.show_message_box)

    def show_message_box(self):
        # Create custom QFileDialog
        dialog = QMessageBox(self)

        #  dialog
        dialog.setText("Delete render cache?")
        dialog.setInformativeText("This action cannot be undone.")
        dialog.setIcon(QMessageBox.Warning)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.No)
        
        # stylesheet set
        dialog.setStyleSheet("QFileDialog { font-size: 14px; }")

        # connect a  signal

        dialog.buttonClicked.connect(lambda b: print("Button clicked:", b.text()))

        dialog.exec_()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MessageBoxWindow()
    window.show()

    sys.exit(app.exec_())