from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    # Initialize the layout
    self.layout = QGridLayout()
    self.setLayout(self.layout)

    # Create buttons
    self.create_widgets()

  def create_widgets(self):
    button1 = QPushButton("Button 1")
    button2 = QPushButton("Button 2")
    button3 = QPushButton("Spanning Button")
    button4 = QPushButton("Button 4")
    button5 = QPushButton("Button 5")

    # Add buttons to the grid layout
    self.layout.addWidget(button1, 0, 0) # Row 0, Column 0
    self.layout.addWidget(button2, 0, 1) # Row 0, Column 1
    self.layout.addWidget(button3, 1, 0, 1, 2) # Spans 1 row, 2 columns
    self.layout.addWidget(button4, 2, 0) # Row 2, Column 0
    self.layout.addWidget(button5, 2, 1) # Row 2, Column 1

if __name__ == "__main__":
  app = QApplication([])

  window = MyWindow()
  window.show()

  app.exec_()