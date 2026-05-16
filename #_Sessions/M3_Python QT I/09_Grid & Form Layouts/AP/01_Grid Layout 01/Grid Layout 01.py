from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class GridWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        buttons = [
            ["Cls", "Bck", "", "Close"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        for row, items in enumerate(buttons):
            for col, text in enumerate(items):
                if text:  # skip empty cell
                    layout.addWidget(QPushButton(text), row, col)

if __name__ == "__main__":
    app = QApplication([])

    window = GridWindow()
    window.show()

    app.exec_()