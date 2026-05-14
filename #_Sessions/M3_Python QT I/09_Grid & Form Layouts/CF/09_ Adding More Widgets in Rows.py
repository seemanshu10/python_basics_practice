from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel
class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    
    form_layout = QFormLayout()
    
    self.username_label = QLabel("Username:")
    self.username_input = QLineEdit()
    self.email_label = QLabel("Email:")
    self.email_input = QLineEdit()
    
    
    self.user_label = QLabel("User:")
    self.user_input = QLineEdit()
    
    
    form_layout.addRow(self.username_label, self.username_input)
    form_layout.addRow(self.email_label, self.email_input)
    form_layout.addRow(self.user_label, self.user_input ) 
    
    self.setLayout(form_layout)

if __name__ == "__main__":
  app = QApplication([])
  window = MyWindow()
  window.show()
  app.exec_()