import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from Student_Notes_App_var_name import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.actionExit
        print(type(self.ui))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())