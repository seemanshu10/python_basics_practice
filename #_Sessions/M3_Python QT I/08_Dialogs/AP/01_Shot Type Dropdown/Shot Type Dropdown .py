# Choose a Shot Type from Dropdown
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Shot Type Dropdown")
        self.setGeometry(100, 100, 400, 150)

        self.button = QPushButton("Pick Shot Category", self)
        self.button.setGeometry(100, 50, 200, 40)

        self.status_label = QLabel("No Shot Type Selected", self)
        self.status_label.setGeometry(20, 100, 250, 50)

        self.button.clicked.connect(self.pick_shot_category)


    def pick_shot_category(self):
        shot_categories = ["Plate", "Comp", "Matte Painting", "Roto", "Cleanup"]
        tag, ok = QInputDialog.getItem(
            self,
            "Shot Category",
            "Select Shot category:",
            shot_categories,
            0, 
            False
            
        )
        # print(f"{tag},   {ok}")
        if ok:
            self.status_label.setText(f"Selected shot type: {tag}")
        else:
            self.status_label.setText("No Shot Type Selected")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
