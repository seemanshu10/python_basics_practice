from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QDockWidget, QToolBar, QAction, QWidget,
    QStatusBar, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QLineEdit, QFormLayout, QTextEdit,
    QListWidget
)

from PySide2.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Student Notes App - QMainWindow Version")
        self.setGeometry(200, 200, 800, 600)

        # menu bar 
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.new_btn = self.file_menu.addAction("New File")
        self.save_btn = self.file_menu.addAction("Export Note")
        self.file_menu.addSeparator()
        self.file_menu.addAction("Exit")

        # shortcuts
        self.new_btn.setShortcut("Ctrl+N")
        
        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.copy_btn = self.edit_menu.addAction("Copy")
        self.paste_btn = self.edit_menu.addAction("Paste")
        self.edit_menu.addSeparator()
        self.teitlechange_btn = self.edit_menu.addAction("Change Title")

        # shortcuts
        self.copy_btn.setShortcut("Ctrl+C")
        self.paste_btn.setShortcut("Ctrl+V")

        # Tool bar 
        self.toolbar = QToolBar() 
        # self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

        self.clear_tool = QAction("Clear", self)
        self.toolbar.addAction(self.clear_tool)

        self.save_tool = QAction("Save", self)
        self.toolbar.addAction(self.save_tool)

        self.export_tool = QAction("export", self)
        self.toolbar.addAction(self.export_tool)
        self.toolbar.addSeparator()

        self.copy_tool = QAction("copy", self)
        self.toolbar.addAction(self.copy_tool)

        self.paste_tool = QAction("paste", self)
        self.toolbar.addAction(self.paste_tool)
        self.toolbar.addSeparator()

        # central widget 
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # nested layout 
        self.widget_layout = QVBoxLayout()
        self.title_label = QLabel("Student Notes App")

        self.widget_layout.addWidget(self.title_label, alignment= Qt.AlignCenter)
        self.form_layout = QFormLayout()

        self.student_label = QLabel("Student Name:")
        self.student_name_line = QLineEdit()
        self.student_name_line.setPlaceholderText("Enter the Student name")

        self.subject_label = QLabel("Subject:")
        self.subject_name_line = QLineEdit()
        self.subject_name_line.setPlaceholderText("Enter the Subject name")

        self.category_label = QLabel("Category:")
        self.category_name_line = QLineEdit()
        self.category_name_line.setPlaceholderText("Enter the Category name")

        self.form_layout.addRow(self.student_label, self.student_name_line)
        self.form_layout.addRow(self.subject_label, self.subject_name_line)
        self.form_layout.addRow(self.category_label, self.category_name_line)
        
        self.widget_layout.addLayout(self.form_layout)

        # notes layout 
        self.notes_label = QLabel("Notes:")
        self.notes_textbox = QTextEdit()
        self.notes_textbox.setPlaceholderText("Write notes here....")


        self.widget_layout.addWidget(self.notes_label)
        self.widget_layout.addWidget(self.notes_textbox)

        # button submit
        self.submit_btn = QPushButton("Submit")  
        self.widget_layout.addWidget(self.submit_btn)

        self.central_widget.setLayout(self.widget_layout)

        # connection 
        self.new_btn.triggered.connect(self.open_file)
        self.save_btn.triggered.connect(self.save_file)
        self.copy_btn.triggered.connect(self.copy_action)

        self.clear_tool.triggered.connect(self.clear_tool_ui)
        self.save_tool.triggered.connect(self.save_tool_ui)
        self.export_tool.triggered.connect(self.export_tool_ui)

        self.submit_btn.clicked.connect(self.submit_asset_ui)
        # self.toggle_dock.triggered.connect(self.toggle_dock_ui)
        
        # dock toolbar
        self.dock = QDockWidget("Asset List", self)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.BottomDockWidgetArea | Qt.TopDockWidgetArea)
        # self.dock.setWidget(QLabel("This is a Dock Widget"))

        self.dock_list = QListWidget()
        self.dock_list.addItems(["Tree", "Character", "Vehicle"])
        self.dock.setWidget(self.dock_list)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)

        # status bar  widget 
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Ready")

        # applying StyleSheet
        self.style_sheet()
        self.setStatusBar(self.status_bar)

    # style sheet function
    def style_sheet(self):
        self.title_label.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                padding: 10px;
                font-style: bold;
            }
        """)
        
        all_label = ["student_label", "subject_label", "category_label"]
        all_line = ["student_name_line", "subject_name_line", "category_name_line"]

        for i in range(len(all_label)):
            label = getattr(self, all_label[i])
            line = getattr(self, all_line[i])

            label.setStyleSheet("""
                QLabel {
                    font-size: 15px;
                    padding: 2px;
                }
            """)

            line.setStyleSheet("""
                QLineEdit {
                    color: black;
                    border: 1px solid #00a8ff;
                    padding: 6px;
                    border-radius: 8px;
                }
                QLineEdit:focus {
                    border: 2px solid purple;
                }
            """)

        self.notes_label.setStyleSheet("""
            QLabel {
                font-size: 15px;
                padding: 2px;
            }
        """)

        self.notes_textbox.setStyleSheet("""
            QTextEdit {
                color: black;
                font-size: 15px;
                border: 1px solid #485460;
                padding: 6px;
                border-radius: 10px;
            }
            QTextEdit:focus {
                border: 2px solid purple;
            }
        """)

        # self.save_button.setStyleSheet("""
        #     QPushButton {
        #         background-color: green;
        #         color: white;
        #         border-radius: 10px;
        #         padding: 8px 16px;
        #     }
        #     QPushButton:hover {
        #         background-color: #2980b9;
        #     }
        #     QPushButton:pressed {
        #         background-color: #1c5980;
        #     }
        # """)

        # self.clear_button.setStyleSheet("""
        #     QPushButton {
        #         background-color: red;
        #         color: white;
        #         border-radius: 10px;
        #         padding: 8px 16px;
        #     }
        #     QPushButton:hover {
        #         background-color: #2980b9;
        #     }
        #     QPushButton:pressed {
        #         background-color: #1c5980;
        #     }
        # """)

        # self.status_label.setStyleSheet("""
        # QLabel{
        #     color: blue;
        #     font-style: italic;
        # }
        # """)

        self.setStyleSheet("""
        QPushButton {
                background-color: #007FFF;
                color: white;
                border-radius: 10px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c5980;
            }               

        """)

    def submit_asset(self):
        print("Asset Submitted")
    
    def open_file(self):
        print("File is opening")
        self.status_bar.showMessage("File is opening")

    def save_file(self):
        print("File is saved.")
        self.status_bar.showMessage("File is saving..")

    def copy_action(self):
        print("Copied to clipboard.")
        self.status_bar.showMessage("Copied to Clipboard")
    
    def clear_tool_ui(self):
        print("Asset Added.")
        self.status_bar.showMessage("Asset is created.")

    def save_tool_ui(self):
        print("Asset Deleted .")
        self.status_bar.showMessage("Asset is deleted.")

    def export_tool_ui(self):
        print("Asset Updated.")
        self.status_bar.showMessage("Asset is Updated.")

    def submit_asset_ui(self):

        asset = self.asset_line.text()
        type = self.type_line.text()
        print("Asset Submited")
        self.status_bar.showMessage(f"Asset {asset} of type {type} is submitted.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())