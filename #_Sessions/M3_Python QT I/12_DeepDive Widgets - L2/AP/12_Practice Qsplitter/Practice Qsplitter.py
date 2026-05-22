# Practice QSplitter

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QSplitter,
    QListView,
    QTextEdit
)
from PySide2.QtCore import Slot, Qt

class QsplitterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Splitter Practice")
        self.resize(400, 500)

        main_layout = QVBoxLayout()

        # Qsplitter Widgets
        self.splitter_widget = QSplitter()
        self.splitter_widget.setOrientation(Qt.Horizontal)
        self.splitter_widget.setSizes([200, 400])

        self.left_widget = QListView()
        self.right_widget = QTextEdit()
        self.splitter_widget.addWidget(self.left_widget)
        self.splitter_widget.addWidget(self.right_widget)
        self.splitter_widget.setStretchFactor(0, 1)
        
        self.splitter_widget.setStyleSheet("""
        QSplitter::handle {
            background-color: #444;
            width: 6px;
        }
        """)
        
        main_layout.addWidget(self.splitter_widget)
        self.setLayout(main_layout)

        self.splitter_widget.splitterMoved.connect(self.changed_splitter)
        # self.splitter_widget.editingFinished.connect(lambda: print("Editing Done"))

    @Slot()
    def changed_splitter(self, pos, index):
        count_widget = self.splitter_widget.count()     
        print(f"Splitter moved Count: {count_widget}")

        widget_type = self.splitter_widget.widget(1)
        print(f"Splitter moved. Position: {pos} Index: {index}")
        # self.spinlabel.setText(f"Scroll position: {current}")

        widget_sizes = self.splitter_widget.sizes()
        print("Sizes:", widget_sizes)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QsplitterWindow()
    window.show()

    sys.exit(app.exec_())