from PySide2.QtWidgets import QApplication, QWidget, QLabel

app = QApplication()
label = QLabel("Hello")

# print(label)
# <PySide2.QtWidgets.QLabel(0x1bd499f3e40) at 0x000001BD4734F500>
print(dir(label))