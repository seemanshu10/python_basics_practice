import sys
import os
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_path = os.path.join(script_dir, "01_sample_ui.ui")
            
        # Load the .ui file dynamically
        self.ui = QUiLoader().load(ui_file_path, self)  
        print(type(self.ui))  # Check the type of the loaded UI
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
