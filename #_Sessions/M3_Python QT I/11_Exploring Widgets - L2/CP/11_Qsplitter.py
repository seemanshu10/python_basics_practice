import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QSplitter, QTextEdit
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSplitter Example")
        
        self.splitter = QSplitter(Qt.Horizontal)
        
        self.editor1 = QTextEdit()
        self.editor2 = QTextEdit()
        
        self.splitter.addWidget(self.editor1)
        self.splitter.addWidget(self.editor2)
        
        self.setCentralWidget(self.splitter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
