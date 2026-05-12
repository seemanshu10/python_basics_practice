import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide2.QtGui import QPalette, QColor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qpallette demo") 
        self.setGeometry(100, 180, 400, 200)
        self.init_ui()

    def init_ui(self):
       
        main_layout = QVBoxLayout()

        label = QLabel("This text ")
        btn = QPushButton("Stylized Button(Button Text)", self)
        main_layout.addWidget(label)
        main_layout.addWidget(btn)
        
        self.setLayout(main_layout)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    palette = QPalette()

    palette.setColor(QPalette.Window, QColor("#435f99"))
    palette.setColor(QPalette.WindowText, QColor("#ffffff"))
    palette.setColor(QPalette.Button, QColor("#61afef"))
    palette.setColor(QPalette.ButtonText, QColor("#282c34"))
    
    app.setPalette(palette)

    window = MainWindow()
    # window.resize(300, 200)
    window.show()

    sys.exit(app.exec_())