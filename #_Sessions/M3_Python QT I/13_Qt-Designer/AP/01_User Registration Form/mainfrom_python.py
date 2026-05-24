import sys
from PySide2.QtWidgets import QApplication, QWidget
from user_registration_Form import Ui_Form  # This is the class generated from the .ui file

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()         # Create an instance of the UI class
        self.ui.setupUi(self)       # Set up the UI for this QMainWindow instance

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())