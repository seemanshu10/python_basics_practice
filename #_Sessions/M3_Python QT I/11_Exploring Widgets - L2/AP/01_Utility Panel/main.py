import sys
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QAction, QSplitter,
    QDockWidget, QWidget, QVBoxLayout, QFormLayout,
    QPushButton, QLabel, QFileDialog, QColorDialog,
    QFontDialog, QSpinBox, QDoubleSpinBox, QScrollArea,
    QTreeView, QListView, QTableView
)
from PySide2.QtGui import QPixmap, QColor, QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt, QStringListModel


class UtilityPanel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AP Utility Panel")
        self.setGeometry(100, 100, 1200, 700)

        # =========================
        # Menu Bar
        # =========================
        file_menu = self.menuBar().addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

        # =========================
        # Toolbar
        # =========================
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.addAction(exit_action)

        # =========================
        # Status Bar
        # =========================
        self.statusBar().showMessage("Ready")

        # =========================
        # Main Splitter
        # =========================
        splitter = QSplitter(Qt.Horizontal)
        self.setCentralWidget(splitter)

        # ======================================================
        # LEFT SIDE - Dock Widget with Tree/List/Table Views
        # ======================================================
        dock = QDockWidget("Assets", self)
        dock_widget = QWidget()
        dock_layout = QVBoxLayout()

        # -------------------------
        # Tree View
        # -------------------------
        self.tree_view = QTreeView()
        tree_model = QStandardItemModel()
        tree_model.setHorizontalHeaderLabels(["Asset Hierarchy"])

        parent1 = QStandardItem("Characters")
        parent1.appendRow(QStandardItem("Hero"))
        parent1.appendRow(QStandardItem("Villain"))

        parent2 = QStandardItem("Environment")
        parent2.appendRow(QStandardItem("Forest"))
        parent2.appendRow(QStandardItem("City"))

        tree_model.appendRow(parent1)
        tree_model.appendRow(parent2)

        self.tree_view.setModel(tree_model)

        # -------------------------
        # List View
        # -------------------------
        self.list_view = QListView()

        list_model = QStringListModel()
        list_model.setStringList([
            "Textures",
            "Models",
            "Animations",
            "Lighting",
            "FX"
        ])

        self.list_view.setModel(list_model)

        # -------------------------
        # Table View
        # -------------------------
        self.table_view = QTableView()

        table_model = QStandardItemModel(3, 3)
        table_model.setHorizontalHeaderLabels([
            "Name",
            "Version",
            "Status"
        ])

        mock_data = [
            ["Hero", "v001", "Approved"],
            ["City", "v003", "Pending"],
            ["ExplosionFX", "v002", "In Progress"]
        ]

        for row, data in enumerate(mock_data):
            for col, value in enumerate(data):
                item = QStandardItem(value)
                table_model.setItem(row, col, item)

        self.table_view.setModel(table_model)

        # Add widgets to dock layout
        dock_layout.addWidget(self.tree_view)
        dock_layout.addWidget(self.list_view)
        dock_layout.addWidget(self.table_view)

        dock_widget.setLayout(dock_layout)
        dock.setWidget(dock_widget)

        # Add dock widget to splitter
        splitter.addWidget(dock)

        # ======================================================
        # RIGHT SIDE - Scroll Area with Controls
        # ======================================================
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        right_widget = QWidget()
        form_layout = QFormLayout()

        # -------------------------
        # SpinBox
        # -------------------------
        self.frame_spin = QSpinBox()
        self.frame_spin.setRange(1, 10000)
        self.frame_spin.setValue(100)

        # -------------------------
        # Double SpinBox
        # -------------------------
        self.opacity_spin = QDoubleSpinBox()
        self.opacity_spin.setRange(0.0, 1.0)
        self.opacity_spin.setSingleStep(0.05)
        self.opacity_spin.setValue(1.0)

        # -------------------------
        # Image Preview Label
        # -------------------------
        self.image_label = QLabel("No Image Loaded")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(400, 300)
        self.image_label.setStyleSheet("""
            border: 2px solid gray;
            background-color: #222;
            color: white;
        """)

        # -------------------------
        # Load Image Button
        # -------------------------
        load_btn = QPushButton("Load Image")
        load_btn.clicked.connect(self.load_image)

        # -------------------------
        # Color Dialog Button
        # -------------------------
        color_btn = QPushButton("Select Border Color")
        color_btn.clicked.connect(self.select_color)

        # -------------------------
        # Font Dialog Button
        # -------------------------
        font_btn = QPushButton("Select Font")
        font_btn.clicked.connect(self.select_font)

        # Add widgets to form layout
        form_layout.addRow("Frame:", self.frame_spin)
        form_layout.addRow("Opacity:", self.opacity_spin)
        form_layout.addRow(load_btn)
        form_layout.addRow(self.image_label)
        form_layout.addRow(color_btn)
        form_layout.addRow(font_btn)

        right_widget.setLayout(form_layout)

        scroll_area.setWidget(right_widget)

        # Add scroll area to splitter
        splitter.addWidget(scroll_area)

        # Initial splitter sizes
        splitter.setSizes([300, 850])

    # ======================================================
    # Load Image Function
    # ======================================================
    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if file_name:
            pixmap = QPixmap(file_name)

            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    self.image_label.width(),
                    self.image_label.height(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )

                self.image_label.setPixmap(scaled_pixmap)

                print(f"Loaded file: {file_name}")
                self.statusBar().showMessage(f"Loaded: {file_name}")

    # ======================================================
    # Select Border Color
    # ======================================================
    def select_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.image_label.setStyleSheet(f"""
                border: 4px solid {color.name()};
                background-color: #222;
                color: white;
            """)

            print(f"Selected color: {color.name()}")
            self.statusBar().showMessage(f"Border Color: {color.name()}")

    # ======================================================
    # Select Font
    # ======================================================
    def select_font(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.image_label.setFont(font)

            print(f"Selected font: {font.toString()}")
            self.statusBar().showMessage("Font Applied")


# ==========================================================
# Main Application
# ==========================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = UtilityPanel()
    window.show()

    sys.exit(app.exec_())
