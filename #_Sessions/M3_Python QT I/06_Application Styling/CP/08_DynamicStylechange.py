import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App Styling Demo") 
        self.setGeometry(100, 180, 400, 200)
        self.init_ui()

    def init_ui(self):
       
        main_layout = QVBoxLayout()

        window_btn = QPushButton("Switch to Windows Style", self) 
        fusion_btn = QPushButton("Switch to Fusion Style", self)
        # button3 = QPushButton("Click Me 3")

        main_layout.addWidget(window_btn)
        main_layout.addWidget(fusion_btn)
        # main_layout.addWidget(button3)
        
        window_btn.clicked.connect(lambda: app.setStyle("Windows"))
        fusion_btn.clicked.connect(lambda: app.setStyle("Fusion"))
        self.setLayout(main_layout)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    window = MainWindow()
    # window.resize(300, 200)
    window.show()

    sys.exit(app.exec_())