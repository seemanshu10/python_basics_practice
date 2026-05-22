# Practice QDoubleSpinBox


import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QDoubleSpinBox,
    QSlider
)
from PySide2.QtCore import Slot, Qt

class QspinboxWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDoubleSpinbox Practice")
        self.resize(200, 200)

        main_layout = QVBoxLayout()

        # QSpinbox Widsgets
        self.double_spin_widget = QDoubleSpinBox()
        self.double_spin_widget.setRange(0.0, 100.0)
        self.double_spin_widget.setValue(1.25)
        self.double_spin_widget.setSingleStep(0.1)
        self.double_spin_widget.setDecimals(2)
        self.double_spin_widget.setPrefix("Opacity: ")
        self.double_spin_widget.setSuffix("  %")
        self.double_spin_widget.setSpecialValueText("Auto")
        self.double_spin_widget.setStyleSheet("""
        QDoubleSpinBox {
            font-size: 14px;
            color: #ffffff;
            background-color: #2e2e2e;
            border: 1px solid #555;
        }
        """)

        self.spinlabel = QLabel("Selected:")
        self.spinslider = QSlider(Qt.Horizontal)
        self.spinslider.setRange(0, 100)

        main_layout.addWidget(self.spinlabel)
        main_layout.addWidget(self.spinslider)
        main_layout.addWidget(self.double_spin_widget)
        self.setLayout(main_layout)

        # Connections
        self.double_spin_widget.editingFinished.connect(lambda: print("Editing Done"))
        self.double_spin_widget.valueChanged.connect(self.changed_spin_label)
        self.spinslider.valueChanged.connect(self.slider_changed)

    @Slot()
    def changed_spin_label(self):
        current = self.double_spin_widget.value()     
        print(f"Scroll position: {current}")
        self.spinlabel.setText(f"Scroll position: {current}")

    def slider_changed(self):
        current = self.spinslider.value()     
        float_value = float(current)
        print("slider_changed", float_value)
        self.double_spin_widget.setValue(float_value)

    def spinbox_changed(self, value):
        print("spinbox_changed", value)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QspinboxWindow()
    window.show()

    sys.exit(app.exec_())