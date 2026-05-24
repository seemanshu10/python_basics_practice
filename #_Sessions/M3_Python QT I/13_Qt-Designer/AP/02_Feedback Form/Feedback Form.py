import sys
import os
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_path = os.path.join(script_dir, "feedback_form.ui")
            
        self.ui = QUiLoader().load(ui_file_path, self)  
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())