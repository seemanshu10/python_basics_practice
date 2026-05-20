# Practice QPixmap
# Practice QInputDialog

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QInputDialog,
)


class PixmapDialogWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QpixMap Dialog Example")
        self.resize(300, 400)
        self.main_layout = QVBoxLayout()
        # buittons
        self.load_button = QPushButton("Load Image")
        self.save_button = QPushButton("Save Cropped Image ")
        
        self.main_layout.addWidget(self.load_button)
        self.main_layout.addWidget(self.save_button)
        
        # Input Dialog 
        self.load_button.clicked.connect(self.ask_for_image)
        self.save_button.clicked.connect(self.ask_for_frame)

        self.setLayout(self.main_layout)
        
    def ask_for_image(self):
        # getText
        text, ok = QInputDialog.getText(self, "Input", "Enter your name:")
        
        if ok:
            print(f"Name : {text}")
            self.name_line.setText(f"{text}")
        else:
            print("File Input Canceled ")

    def ask_for_frame(self):
        frame, ok = QInputDialog.getInt(self, "Input", "Enter Frame Number:")
    
        if ok:
            print(f"Frame Number : {frame}")
            self.frame_line.setText(f"{frame}")
        else:
            print("Frame Input Canceled ")

    def ask_for_opacity(self):
        opacity, ok = QInputDialog.getDouble(self,  "Input", "Enter opacity value:")
    
        if ok:
            print(f"Opacity : {opacity}")
            self.opacity_line.setText(f"{opacity}")
        else:
            print("Opacity Input Canceled ")

    def ask_for_render_engine(self):
        item, ok = QInputDialog.getItem(self, "Select Engine", "Choose Render Engine:", ["Arnold", "Redshift", "VRay"])
    
        if ok:
            print(f"Render Engine : {item}")
            self.render_line.setText(f"{item}")
        else:
            print("Render Engine Input Canceled ")

    def ask_for_shot(self):
        dialog = QInputDialog(self)
        dialog.setLabelText("Enter shot number:")
        dialog.textValueChanged.connect(lambda text: print("Changed:", text))  # textValueChanged
        dialog.textValueSelected.connect(lambda text: print("Selected:", text))  # textValueSelected
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PixmapDialogWindow()
    window.show()

    sys.exit(app.exec_())