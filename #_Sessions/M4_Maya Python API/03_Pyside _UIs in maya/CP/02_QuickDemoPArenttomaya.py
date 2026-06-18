from PySide2.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout
import shiboken2
from maya import OpenMayaUI as omui


def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(main_window_ptr), QWidget)

class SimpleWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SimpleWindow, self).__init__(parent)
        self.setWindowTitle("QMainWindow Integrated")

        # Create a basic central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Add a button to the central widget
        button = QPushButton("Click Me", central_widget)

        button.clicked.connect(self.on_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(button)
        central_widget.setLayout(layout)

    def on_button_clicked(self):
        print("Button Clicked! This window is part of maya's UI")

def show_window():
    global my_window
    # checks if window is already open it closes them 
    # method resolution order is 
    # 
    """
    [
    SimpleWindow,
    PySide2.QtWidgets.QMainWindow,
    PySide2.QtWidgets.QWidget,
    PySide2.QtCore.QObject,
    object
    ]
    """
    try:
        my_window.close()
        my_window.deleteLater()
    except:
        pass
    # print(SimpleWindow.mro())
    maya_main_window = get_maya_main_window()
    my_window = SimpleWindow(parent=maya_main_window)
    my_window.show()

show_window()