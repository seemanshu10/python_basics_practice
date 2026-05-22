# Practice QListView

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QListView,
    QSlider,
    
)
from PySide2.QtCore import Slot, Qt, QStringListModel

class QlistWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListView Practice")
        self.resize(200, 200)

        main_layout = QVBoxLayout()

        self.qlist_widget = QListView()
        
        model = QStringListModel(["Beauty", "Specular", "Diffuse", "ZDepth", "Shadow"])
        self.qlist_widget.setModel(model)
        # self.qlist_widget(model)
        self.qlist_widget.setViewMode(QListView.ListMode)
        self.qlist_widget.setStyleSheet("""
        QListView {
            background-color: #2b2b2b;
            color: #ffffff;
            font-size: 14px;
            border: 1px solid #555;
        }
        QListView::item:selected {
            background-color: #007acc;
        }
        """)

        self.label = QLabel("Selected:")
        main_layout.addWidget(self.qlist_widget)
        main_layout.addWidget(self.label)
        self.setLayout(main_layout)

        # Connections
        self.qlist_widget.clicked.connect(self.on_item_clicked)

    @Slot()
    def on_item_clicked(self, index):
        print(f"item Clicked: {index.data()}")
        self.label.setText(f"Selected: {index.data()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QlistWindow()
    window.show()

    sys.exit(app.exec_())