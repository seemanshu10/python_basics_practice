import sys
from PySide2.QtWidgets import QApplication, QWidget
from user_registration_Form import Ui_Form 

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()       
        self.ui.setupUi(self)       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())