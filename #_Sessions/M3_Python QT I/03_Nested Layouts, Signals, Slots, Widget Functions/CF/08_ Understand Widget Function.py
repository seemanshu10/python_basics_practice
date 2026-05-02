from PySide2.QtWidgets import QLabel, QApplication

app = QApplication([])
label = QLabel("Hello")

print(label)
# <PySide2.QtWidgets.QLabel(0x1de20a6f790) at 0x000001DE1E18EE40>


# Getting Widget Functions with dir()
print(dir(label))