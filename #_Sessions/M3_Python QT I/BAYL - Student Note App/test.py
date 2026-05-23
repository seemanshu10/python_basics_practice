import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QFrame,
    QSplitter,
    QMessageBox
)

from PySide2.QtCore import Qt


class VFXPublishTool(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VFX Asset Publish Manager")
        self.resize(1300, 700)

        self.projects_data = {
            "DragonFilm": [
                "dragon_A",
                "dragon_B",
                "cave_env"
            ],

            "SpaceWars": [
                "spaceship_X",
                "laser_gun",
                "robot_Z"
            ],

            "FantasyWorld": [
                "castle_A",
                "magic_tree",
                "wizard_char"
            ]
        }

        self.build_ui()
        self.load_projects()
        self.load_publish_history()

    def build_ui(self):

        # =========================
        # MAIN LAYOUT
        # =========================

        main_layout = QVBoxLayout(self)

        title = QLabel("VFX Asset Publish Tool")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            padding: 10px;
        """)

        main_layout.addWidget(title)

        splitter = QSplitter(Qt.Horizontal)

        # =========================
        # LEFT PANEL
        # =========================

        left_panel = QFrame()
        left_panel.setFrameShape(QFrame.StyledPanel)

        left_layout = QVBoxLayout(left_panel)

        project_label = QLabel("Projects")
        project_label.setStyleSheet("font-size:18px;")

        left_layout.addWidget(project_label)

        self.project_list = QListWidget()
        self.project_list.currentTextChanged.connect(
            self.update_assets
        )

        left_layout.addWidget(self.project_list)

        asset_label = QLabel("Assets")
        asset_label.setStyleSheet("font-size:18px;")

        left_layout.addWidget(asset_label)

        self.asset_list = QListWidget()
        self.asset_list.currentTextChanged.connect(
            self.select_asset
        )

        left_layout.addWidget(self.asset_list)

        # =========================
        # CENTER PANEL
        # =========================

        center_panel = QFrame()
        center_panel.setFrameShape(QFrame.StyledPanel)

        center_layout = QVBoxLayout(center_panel)

        info_label = QLabel("Publish Information")
        info_label.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        center_layout.addWidget(info_label)

        self.asset_name_input = QLineEdit()
        self.asset_name_input.setPlaceholderText(
            "Asset Name"
        )

        center_layout.addWidget(self.asset_name_input)

        self.task_dropdown = QComboBox()

        self.task_dropdown.addItems([
            "Model",
            "Rig",
            "Texture",
            "Animation",
            "FX",
            "Lighting",
            "Lookdev"
        ])

        center_layout.addWidget(self.task_dropdown)

        self.version_input = QLineEdit()
        self.version_input.setPlaceholderText(
            "Version (Example: v001)"
        )

        center_layout.addWidget(self.version_input)

        notes_label = QLabel("Publish Notes")
        notes_label.setStyleSheet("font-size:16px;")

        center_layout.addWidget(notes_label)

        self.notes_box = QTextEdit()
        self.notes_box.setPlaceholderText(
            "Write publish notes..."
        )

        center_layout.addWidget(self.notes_box)

        self.publish_button = QPushButton("Publish Asset")
        self.publish_button.setMinimumHeight(40)

        self.publish_button.clicked.connect(
            self.publish_asset
        )

        center_layout.addWidget(self.publish_button)

        self.status_label = QLabel("")
        center_layout.addWidget(self.status_label)

        # =========================
        # RIGHT PANEL
        # =========================

        right_panel = QFrame()
        right_panel.setFrameShape(QFrame.StyledPanel)

        right_layout = QVBoxLayout(right_panel)

        history_label = QLabel("Publish History")
        history_label.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        right_layout.addWidget(history_label)

        self.history_table = QTableWidget()

        self.history_table.setColumnCount(5)

        self.history_table.setHorizontalHeaderLabels([
            "Project",
            "Asset",
            "Task",
            "Version",
            "Artist"
        ])

        self.history_table.horizontalHeader().setStretchLastSection(True)

        right_layout.addWidget(self.history_table)

        # =========================
        # ADD PANELS
        # =========================

        splitter.addWidget(left_panel)
        splitter.addWidget(center_panel)
        splitter.addWidget(right_panel)

        splitter.setSizes([250, 400, 650])

        main_layout.addWidget(splitter)

        # =========================
        # STYLE
        # =========================

        self.setStyleSheet("""

            QWidget {
                background-color: #2b2b2b;
                color: #dddddd;
                font-size: 14px;
            }

            QListWidget,
            QTextEdit,
            QLineEdit,
            QComboBox,
            QTableWidget {
                background-color: #3a3a3a;
                border: 1px solid #555555;
                padding: 5px;
            }

            QPushButton {
                background-color: #4c89ff;
                border: none;
                border-radius: 4px;
                padding: 8px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #6ca0ff;
            }

            QHeaderView::section {
                background-color: #444444;
                padding: 5px;
                border: 1px solid #555555;
            }

        """)

    # =========================
    # LOAD PROJECTS
    # =========================

    def load_projects(self):

        self.project_list.clear()

        for project in self.projects_data:
            self.project_list.addItem(project)

    # =========================
    # UPDATE ASSET LIST
    # =========================

    def update_assets(self):

        self.asset_list.clear()

        project = self.project_list.currentItem()

        if not project:
            return

        project_name = project.text()

        assets = self.projects_data.get(project_name, [])

        self.asset_list.addItems(assets)

    # =========================
    # SELECT ASSET
    # =========================

    def select_asset(self):

        asset = self.asset_list.currentItem()

        if not asset:
            return

        self.asset_name_input.setText(asset.text())

    # =========================
    # LOAD HISTORY
    # =========================

    def load_publish_history(self):

        history_data = [

            ["DragonFilm", "dragon_A", "Model", "v001", "John"],

            ["DragonFilm", "dragon_A", "Texture", "v002", "Mike"],

            ["SpaceWars", "robot_Z", "Rig", "v003", "Anna"],

            ["FantasyWorld", "castle_A", "Lookdev", "v004", "David"]
        ]

        self.history_table.setRowCount(len(history_data))

        for row, data in enumerate(history_data):

            for column, value in enumerate(data):

                item = QTableWidgetItem(value)

                self.history_table.setItem(
                    row,
                    column,
                    item
                )

    # =========================
    # PUBLISH ASSET
    # =========================

    def publish_asset(self):

        project_item = self.project_list.currentItem()

        asset = self.asset_name_input.text().strip()
        task = self.task_dropdown.currentText()
        version = self.version_input.text().strip()
        notes = self.notes_box.toPlainText().strip()

        if not project_item:

            QMessageBox.warning(
                self,
                "Missing Project",
                "Please select a project."
            )

            return

        if not asset:

            QMessageBox.warning(
                self,
                "Missing Asset",
                "Please enter asset name."
            )

            return

        if not version:

            QMessageBox.warning(
                self,
                "Missing Version",
                "Please enter version."
            )

            return

        project = project_item.text()

        current_row = self.history_table.rowCount()

        self.history_table.insertRow(current_row)

        publish_data = [
            project,
            asset,
            task,
            version,
            "You"
        ]

        for column, value in enumerate(publish_data):

            self.history_table.setItem(
                current_row,
                column,
                QTableWidgetItem(value)
            )

        self.status_label.setText(
            f"{asset} published successfully."
        )

        self.status_label.setStyleSheet("""
            color: lightgreen;
            font-size: 14px;
            font-weight: bold;
            padding: 5px;
        """)

        print("\n========== PUBLISH INFO ==========")
        print(f"Project : {project}")
        print(f"Asset   : {asset}")
        print(f"Task    : {task}")
        print(f"Version : {version}")
        print(f"Notes   : {notes}")
        print("==================================")

        self.notes_box.clear()

    # =========================
    # END
    # =========================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = VFXPublishTool()
    window.show()

    sys.exit(app.exec_())