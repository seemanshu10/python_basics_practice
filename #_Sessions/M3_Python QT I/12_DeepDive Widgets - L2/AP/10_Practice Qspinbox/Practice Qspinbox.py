# Practice QSpinBox

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QSpinBox
)
from PySide2.QtCore import Slot, Qt

class QspinboxWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinbox Practice")
        self.resize(400, 500)

        main_layout = QVBoxLayout()

        # QSpinbox Widsgets
        self.spin_widget = QSpinBox()
        self.spin_widget.setRange(0, 100)
        self.spin_widget.setValue(10)
        self.spin_widget.setSingleStep(5)
        self.spin_widget.setPrefix("Frame ")
        self.spin_widget.setSuffix(" px")
        self.spin_widget.setSpecialValueText("Auto")
        self.spin_widget.setStyleSheet("""
        QSpinBox {
            font-size: 14px;
            color: #ffffff;
            background-color: #2b2b2b;
            border: 1px solid #666;
        }
        """)

        self.spinlabel = QLabel("Selected:")

        main_layout.addWidget(self.spin_widget)
        main_layout.addWidget(self.spinlabel)
        self.setLayout(main_layout)

        self.spin_widget.valueChanged.connect(self.changed_spin_label)
        self.spin_widget.editingFinished.connect(lambda: print("Editing Done"))

    @Slot()
    def changed_spin_label(self):
        current = self.spin_widget.value()     
        print(f"Scroll position: {current}")
        self.spinlabel.setText(f"Scroll position: {current}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QspinboxWindow()
    window.show()

    sys.exit(app.exec_())