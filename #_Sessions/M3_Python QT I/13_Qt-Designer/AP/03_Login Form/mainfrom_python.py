"""Login form application entry point.

This module initializes a Qt application and displays the login form
created by Qt Designer. The login form UI is imported from
`login_form_with_language.Ui_Form`.
"""

import sys
from PySide2.QtWidgets import QApplication, QWidget
from login_form_with_language import Ui_Form  # This is the class generated from the .ui file

class MyApp(QWidget):
    """Main application window for the login form."""

    def __init__(self):
        """Initialize the login form window and UI components."""
        super().__init__()

        self.ui = Ui_Form()         # Create an instance of the UI class
        self.ui.setupUi(self)       # Set up the UI for this QMainWindow instance

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())