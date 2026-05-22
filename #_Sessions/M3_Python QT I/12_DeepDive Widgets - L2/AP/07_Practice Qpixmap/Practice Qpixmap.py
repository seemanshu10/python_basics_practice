# Practice QPixmap
# Practice QInputDialog

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    
)

from PySide2.QtGui import QPixmap
from PySide2.QtCore import Slot
class PixmapDialogWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QpixMap Dialog Example")
        self.resize(300, 400)
        self.main_layout = QVBoxLayout()
        # buittons
        self.image_label = QLabel()
        self.image_label.setStyleSheet("QLabel { background-color: black; border: 1px solid #ccc; }")
        self.load_button = QPushButton("Load Image")
        self.save_button = QPushButton("Save Cropped Image ")
        
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addWidget(self.load_button)
        self.main_layout.addWidget(self.save_button)
        
        # Input Dialog 
        self.load_button.clicked.connect(self.load_image_file)
        self.save_button.clicked.connect(self.cropped_image_file)

        self.setLayout(self.main_layout)

    @Slot()
    def load_image_file(self):
        # getText
        file_path, ok = QFileDialog.getOpenFileName(
            self,
            "Select an Image File?",
            "",
            "Images (*.png *.jpg *.exr)"
        )

        if ok:
            if file_path:

                self.pixmap = QPixmap(file_path)
                self.pixmap.load(file_path)                             # load
            if not self.pixmap.isNull():                                # isNull
                scaled = self.pixmap.scaled(500, 500)                   # scaled
                print(self.pixmap.width(), self.pixmap.height())        # width, height
                self.image_label.setPixmap(scaled)
                # cropped = self.pixmap.copy(50, 50, 100, 100)          # copy
                # cropped.save("cropped.jpg")        
                
        else:
            print("File Input Canceled ")

    @Slot()
    def cropped_image_file(self):
        cropped_image = self.pixmap.copy(100, 100, 200, 300)
        self.image_label.setPixmap(cropped_image)
        cropped_image.save("cropped_output.jpg")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PixmapDialogWindow()
    window.show()

    sys.exit(app.exec_())