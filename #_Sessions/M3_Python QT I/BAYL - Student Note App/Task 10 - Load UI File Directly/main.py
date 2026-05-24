import sys, os 
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtUiTools import QUiLoader


class StudentApp(QMainWindow):

    def __init__(self):
        super().__init__()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_path = os.path.join(script_dir, "Student_Notes_App.ui")
        # print(ui_file_path)

        self.ui = QUiLoader().load(ui_file_path, self)
        # print(type(self.ui))
        self.ui.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentApp()
    # window.show()
    sys.exit(app.exec_())

