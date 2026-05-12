from PySide2.QtWidgets import QApplication, QFontDialog, QPushButton, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font Style for Review Labels")
        self.setGeometry(100, 100, 400, 150)

        # self.main_layout = QVBoxLayout()

        self.button = QPushButton("Choose Font", self)
        self.button.setGeometry(100, 50, 200, 40)
        self.status_label = QLabel("Review Label Here", self)
        self.status_label.setGeometry(20, 100, 250, 50)

        self.button.clicked.connect(self.pick_font)

    def pick_font(self):
        ok, font= QFontDialog.getFont()
        print(font)
        
        if ok:
            font_family = font.family()
            font_size = font.pointSize()
            # strike = font.effects()
            # font_size = font.AnyStyle()
            # print(f"{font},   {ok}")
            print(f"Selected font: {font_family} at size {font_size}")
            self.status_label.setText(f"{font_family} , {font_size}pt ")

            self.status_label.setFont(font)
            # self.status_label.setStyleSheet(f"""
            # QLabel{{
            #     font-family: {font_family};
            #     font-size: {font_size}pt;
            
            # }}
            # """)

        else:
            print("Font selection canceled.")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
