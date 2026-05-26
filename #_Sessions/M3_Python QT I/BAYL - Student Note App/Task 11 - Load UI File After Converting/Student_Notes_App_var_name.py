
from PySide2.QtCore import Qt, Slot, QMetaObject, QRect, QCoreApplication
from PySide2.QtGui import QTextCharFormat, QIcon
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QToolBar, QAction, QWidget,
    QStatusBar, QVBoxLayout, QPushButton, QGridLayout, QLineEdit, QFormLayout, QTextEdit,
    QMessageBox, QColorDialog, QFontDialog, QInputDialog, QFileDialog, QSizePolicy, QPlainTextEdit, QMenuBar, QMenu, QToolBar
)
import qtawesome, os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
ICON_FOLDER_PATH = os.path.join(FILE_PATH, "icons")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # self.MainWindow = MainWindow
        MainWindow.resize(859, 658)
        self.clear_tool = QAction(MainWindow)
        self.clear_tool.setObjectName(u"clear_tool")
        self.save_tool = QAction(MainWindow)
        self.save_tool.setObjectName(u"save_tool")
        self.export_tool = QAction(MainWindow)
        self.export_tool.setObjectName(u"export_tool")
        self.exit_btn = QAction(MainWindow)
        self.exit_btn.setObjectName(u"exit_btn")
        self.about_btn = QAction(MainWindow)
        self.about_btn.setObjectName(u"about_btn")
        self.copy_tool = QAction(MainWindow)
        self.copy_tool.setObjectName(u"copy_tool")
        self.paste_tool = QAction(MainWindow)
        self.paste_tool.setObjectName(u"paste_tool")
        self.titlechange_tool = QAction(MainWindow)
        self.titlechange_tool.setObjectName(u"titlechange_tool")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout_2 = QVBoxLayout(self.central_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_layout = QVBoxLayout()
        self.widget_layout.setObjectName(u"widget_layout")
        self.title_label = QLabel(self.central_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.widget_layout.addWidget(self.title_label)

        self.form_layout = QFormLayout()
        self.form_layout.setObjectName(u"form_layout")
        self.student_label = QLabel(self.central_widget)
        self.student_label.setObjectName(u"student_label")

        self.form_layout.setWidget(0, QFormLayout.LabelRole, self.student_label)

        self.student_name_line = QLineEdit(self.central_widget)
        self.student_name_line.setObjectName(u"student_name_line")

        self.form_layout.setWidget(0, QFormLayout.FieldRole, self.student_name_line)

        self.subject_label = QLabel(self.central_widget)
        self.subject_label.setObjectName(u"subject_label")

        self.form_layout.setWidget(1, QFormLayout.LabelRole, self.subject_label)

        self.subject_name_line = QLineEdit(self.central_widget)
        self.subject_name_line.setObjectName(u"subject_name_line")

        self.form_layout.setWidget(1, QFormLayout.FieldRole, self.subject_name_line)

        self.category_label = QLabel(self.central_widget)
        self.category_label.setObjectName(u"category_label")

        self.form_layout.setWidget(2, QFormLayout.LabelRole, self.category_label)

        self.category_name_line = QLineEdit(self.central_widget)
        self.category_name_line.setObjectName(u"category_name_line")

        self.form_layout.setWidget(2, QFormLayout.FieldRole, self.category_name_line)


        self.widget_layout.addLayout(self.form_layout)

        self.notes_label = QLabel(self.central_widget)
        self.notes_label.setObjectName(u"notes_label")

        self.widget_layout.addWidget(self.notes_label)

        self.notes_textbox = QPlainTextEdit(self.central_widget)
        self.notes_textbox.setObjectName(u"notes_textbox")

        self.widget_layout.addWidget(self.notes_textbox)

        self.button_layout = QGridLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.color_button = QPushButton(self.central_widget)
        self.color_button.setObjectName(u"color_button")

        self.button_layout.addWidget(self.color_button, 1, 0, 1, 1)

        self.title_button = QPushButton(self.central_widget)
        self.title_button.setObjectName(u"title_button")

        self.button_layout.addWidget(self.title_button, 2, 0, 1, 1)

        self.save_button = QPushButton(self.central_widget)
        self.save_button.setObjectName(u"save_button")

        self.button_layout.addWidget(self.save_button, 0, 0, 1, 1)

        self.export_button = QPushButton(self.central_widget)
        self.export_button.setObjectName(u"export_button")

        self.button_layout.addWidget(self.export_button, 2, 1, 1, 1)

        self.font_button = QPushButton(self.central_widget)
        self.font_button.setObjectName(u"font_button")

        self.button_layout.addWidget(self.font_button, 1, 1, 1, 1)

        self.clear_button = QPushButton(self.central_widget)
        self.clear_button.setObjectName(u"clear_button")

        self.button_layout.addWidget(self.clear_button, 0, 1, 1, 1)


        self.widget_layout.addLayout(self.button_layout)

        self.status_label = QLabel(self.central_widget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setAlignment(Qt.AlignCenter)

        self.widget_layout.addWidget(self.status_label)

        self.footer = QLabel(self.central_widget)
        self.footer.setObjectName(u"footer")
        self.footer.setAlignment(Qt.AlignCenter)

        self.widget_layout.addWidget(self.footer)

        self.widget_layout.setStretch(0, 1)
        self.widget_layout.setStretch(1, 2)
        self.widget_layout.setStretch(2, 1)
        self.widget_layout.setStretch(3, 3)
        self.widget_layout.setStretch(5, 1)

        self.verticalLayout_2.addLayout(self.widget_layout)

        MainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 859, 21))
        self.file_menu = QMenu(self.menu_bar)
        self.file_menu.setObjectName(u"file_menu")
        self.edit_menu = QMenu(self.menu_bar)
        self.edit_menu.setObjectName(u"edit_menu")
        self.help_menu = QMenu(self.menu_bar)
        self.help_menu.setObjectName(u"help_menu")
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.toolbar = QToolBar(MainWindow)
        self.toolbar.setObjectName(u"toolbar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolbar)

        self.menu_bar.addAction(self.file_menu.menuAction())
        self.menu_bar.addAction(self.edit_menu.menuAction())
        self.menu_bar.addAction(self.help_menu.menuAction())
        self.file_menu.addAction(self.clear_tool)
        self.file_menu.addAction(self.save_tool)
        self.file_menu.addAction(self.export_tool)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_btn)
        self.edit_menu.addAction(self.copy_tool)
        self.edit_menu.addAction(self.paste_tool)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.titlechange_tool)
        self.help_menu.addAction(self.about_btn)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.clear_tool)
        self.toolbar.addAction(self.save_tool)
        self.toolbar.addAction(self.export_tool)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.copy_tool)
        self.toolbar.addAction(self.paste_tool)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.titlechange_tool)


        # shortcuts
        self.clear_tool.setShortcut("Ctrl+N")
        self.save_tool.setShortcut("Ctrl+S")
        self.export_tool.setShortcut("Ctrl+Shift+S")
        self.exit_btn.setShortcut("Ctrl+Q")
        self.save_tool.setEnabled(False)
        self.export_tool.setEnabled(False)
        
        self.copy_tool.setShortcut("Ctrl+C")
        self.paste_tool.setShortcut("Ctrl+V")
        self.titlechange_tool.setShortcut("Ctrl+T")

        self.about_btn.setShortcut("F1")

        # icons
        
        self.clear_tool.setIcon(qtawesome.icon('ei.file-new', color='#2980b9'))
        self.save_tool.setIcon(qtawesome.icon('fa5s.save', color='#2980b9'))
        self.export_tool.setIcon(qtawesome.icon('ph.export-bold', color='#2980b9'))
        self.exit_btn.setIcon(qtawesome.icon('mdi.exit-to-app', color="#a71a2d"))

        self.copy_tool.setIcon(qtawesome.icon('fa5.copy', color='#2980b9'))
        self.paste_tool.setIcon(qtawesome.icon('fa6.paste', color='#2980b9'))
        self.titlechange_tool.setIcon(qtawesome.icon('mdi.format-title', color='#2980b9'))

        self.status_bar.showMessage("Ready")
        
        self.retranslateUi(MainWindow)
        # applying StyleSheet
        self.apply_stylesheet(MainWindow)
        self.all_signals_connector(MainWindow)

        # Exit button 
        self.exit_btn.triggered.connect(MainWindow.close)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def apply_stylesheet(self, MainWindow):

        stylesheet_path = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(stylesheet_path, "style.css")

        with open(stylesheet_path, "r") as f:
                style = f.read()
                MainWindow.setStyleSheet(style)

        self.title_label.setStyleSheet("""
        QLabel {
                font-size: 22px;
                font-weight: bold;
                background-color: #dbeafe;
                border-radius: 12px;
                padding: 15px;
        }
        """)

        all_label = ["student_label", "subject_label", "category_label"]
        all_line = ["student_name_line", "subject_name_line", "category_name_line"]

        for i in range(len(all_label)):
                label = getattr(self, all_label[i])
                line = getattr(self, all_line[i])

                label.setStyleSheet("""
                        QLabel {
                        font-size: 12px;
                        padding: 2px;
                        font-style: normal;
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
                font-size: 12px;
                padding: 2px;
                font-weight: bold;         
        }
        """)

        self.status_label.setStyleSheet("""
        QLabel{
                background: white;
                border: 1px solid grey;
                color: #64748b;
                font-size: 10px;
                font-style: italic;
                border-radius: 8px;
        }
        """)

        self.footer.setStyleSheet("""
        QLabel{
                font-size: 11px;
                color: #64748b;
        }
        """)

    def export_notes(self):
        name_student = self.student_label.text()
        name_student_name = self.student_name_line.text()
        subject_student = self.subject_label.text()
        subject_student_name = self.subject_name_line.text()
        category_student = self.category_label.text()
        category_student_name = self.category_name_line.text()

        notes_data = self.notes_textbox.toPlainText()
        # print(name_student, name_student_name, notes_data)

        export_data = (
        f"{name_student} {name_student_name}\n"
        f"{subject_student} {subject_student_name}\n"
        f"{category_student} {category_student_name}\n\n"
        f"Notes:\n{notes_data}\n"
        )

        with open(self.save_file_path, "w") as export_note:
            export_note.write(export_data)

        self.status_bar.showMessage("Note Saved Successfully.")
        self.status_label.setText(f"Exported Notes To:\n{self.save_file_path}")

    def save_note(self):
        self.status_label.setText(f"Status: Note Saved for {self.student_name_line.text()}.")
        self.status_bar.showMessage("Note Saved Successfully.")

    def confirm_new_file_dialog(self):
        response = QMessageBox.question(
            None,
            "Opening New Note ",
            "Are you sure you want to create a new file? " \
            "All unsaved progress will be lost"
        )

        if response == QMessageBox.Yes:
            print("User confirmed to create new fields.")
            self.clear_line_tool()
        else:
            print("User canceled to create new fields.")

    def clear_line_tool(self):
        self.student_name_line.clear()
        self.subject_name_line.clear()
        self.category_name_line.clear()
        self.notes_textbox.clear()

        self.status_label.setText("Status: All Fields Cleared")
        self.status_bar.showMessage("All Fields Cleared")

    # all connections 
    def all_signals_connector(self, MainWindow):
        # Tool and menu bar connections
        self.clear_tool.triggered.connect(self.open_file)
        self.save_tool.triggered.connect(self.confirm_save)
        self.export_tool.triggered.connect(self.choose_export_tool)
        
        # Copy Paste Action
        self.copy_tool.triggered.connect(self.copy_action)
        self.paste_tool.triggered.connect(self.paste_action)
        self.titlechange_tool.triggered.connect(self.choose_title_dialog)
        # self.export_tool.triggered.connect(self.choose_export_tool)

        self.about_btn.triggered.connect(self.about_tool_action)

        # connection 
        self.student_name_line.textChanged.connect(self.names_inputs)
        self.subject_name_line.textChanged.connect(self.subject_inputs)
        self.category_name_line.textChanged.connect(self.category_inputs)
        self.notes_textbox.textChanged.connect(self.notes_inputs)
        self.clear_button.clicked.connect(self.confirm_clear_dialog)

        self.color_button.clicked.connect(self.choose_color_dialog)
        self.font_button.clicked.connect(self.choose_font_dialog)
        self.title_button.clicked.connect(self.choose_title_dialog)
        self.save_button.clicked.connect(self.confirm_save)
        self.export_button.clicked.connect(self.choose_export_tool)

    # Clear Dialog function 
    @Slot()
    def confirm_clear_dialog(self):
        response = QMessageBox.question(
            None,
            "Clear All Fields. ",
            "Are you sure you want to Clear all the Fields?"
        )

        if response == QMessageBox.Yes:
            print("User confirmed to Clear Feilds.")
            self.clear_line_tool()
        else:
            print("User canceled to clear thew fields.")

    @Slot()
    def notes_inputs(self):

        note = self.notes_textbox.toPlainText()
        
        if note:
            self.save_button.setEnabled(True)
            self.export_button.setEnabled(True)
            self.save_tool.setEnabled(True)
            self.export_tool.setEnabled(True)
            self.status_label.setText(f"Status: Note Updated")
            
        else:
            self.save_button.setEnabled(False)
            self.export_button.setEnabled(False)
            self.save_tool.setEnabled(False)
            self.export_tool.setEnabled(False)
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def about_tool_action(self):
        self.about_message = QMessageBox.about(
            None,
            "About Students Notes Pro",
            "Student Notes Pro v1.0\nA Simple Notes App to take notes?"
            )

    @Slot()
    # title change function
    def choose_title_dialog(self):
        
        self.name, ok = QInputDialog.getText(self, "Change notes Title?", "Write New Title?")
        if ok:
            self.title_label.setText(f"{self.name}")
            print(self.name)

        self.status_bar.showMessage("Title Changed Successfully.")
        self.status_label.setText(f"Title Changed Successfully to: {self.title_label.text()}")

    @Slot()
    def paste_action(self):
        print("Text Pasted.")
        self.notes_textbox.paste()
        self.status_bar.showMessage("Text Pasted")

    @Slot()
    def copy_action(self):
        print("Copied to clipboard.")
        self.notes_textbox.copy()
        self.status_bar.showMessage("Copied to Clipboard")

    @Slot()
    def open_file(self):
        self.confirm_new_file_dialog()
        print("New File is opening")
        self.status_bar.showMessage("New Note Created")

    @Slot()
    def confirm_save(self):
        response = QMessageBox.question(
            None,
            "Save Note File",
            "Are you sure you want to save the note?"
        )

        if response == QMessageBox.Yes:
            print("User confirmed to save Note.")
            self.save_note()
            # self.save_button.clicked.connect(self.save_note)
        else:
            print("User canceled to save the note.")

    @Slot()
    # font selection function
    def choose_font_dialog(self):
        ok, self.font_color = QFontDialog.getFont()
        
        if ok:
            fmt = QTextCharFormat()
            fmt.setFont(self.font_color)

            cursor = self.notes_textbox.textCursor()
            cursor.mergeCharFormat(fmt)

            self.notes_textbox.mergeCurrentCharFormat(fmt)

            self.status_label.setText(
                f"Selected Font: {self.font_color.family()}"
            )
        
        self.status_bar.showMessage("Font Changed.")

    @Slot()
    # color choose notes function
    def choose_color_dialog(self):
        self.font_color = QColorDialog.getColor()
        if self.font_color.isValid():
            
            fmt = QTextCharFormat()
            fmt.setForeground(self.font_color)

            cursor = self.notes_textbox.textCursor()
            cursor.mergeCharFormat(fmt)

            self.notes_textbox.mergeCurrentCharFormat(fmt)

            self.status_label.setText(
                f"Selected color: {self.font_color.name()}"
            )

        self.status_bar.showMessage("Color Changed Successfully.")

    @Slot()
    def names_inputs(self):
        name = self.student_name_line.text().strip()
        if name:
            self.status_label.setText(f"Status: Typing name - {name}")
        else:
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def subject_inputs(self):
        name = self.subject_name_line.text().strip()
        if name:
            self.status_label.setText(f"Status: Typing subject - {name}")
        else:
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def category_inputs(self):
        name = self.category_name_line.text().strip()
        if name:
            self.status_label.setText(f"Status: Typing Category - {name}")
        else:
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def choose_export_tool(self):
        self.save_file_path, _ = QFileDialog.getSaveFileName(self, "Select File", "", "Text (*.txt)")
        if self.save_file_path:
            
            self.export_notes()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Students Note App", None))
        self.clear_tool.setText(QCoreApplication.translate("MainWindow", u"New File/Clear", None))
        self.save_tool.setText(QCoreApplication.translate("MainWindow", u"Save Note", None))
        self.export_tool.setText(QCoreApplication.translate("MainWindow", u"Export Note", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.copy_tool.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(statustip)
        self.copy_tool.setStatusTip(QCoreApplication.translate("MainWindow", u"Copied to clipboard", None))
#endif // QT_CONFIG(statustip)
        self.paste_tool.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(statustip)
        self.paste_tool.setStatusTip(QCoreApplication.translate("MainWindow", u"Paste", None))
#endif // QT_CONFIG(statustip)
        self.titlechange_tool.setText(QCoreApplication.translate("MainWindow", u"Change Title", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Students Notes Pro", None))
        self.student_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.subject_label.setText(QCoreApplication.translate("MainWindow", u"Subject:", None))
        self.category_label.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.notes_label.setText(QCoreApplication.translate("MainWindow", u"Notes:", None))
        self.notes_textbox.setPlaceholderText("")
        self.color_button.setText(QCoreApplication.translate("MainWindow", u"Choose Clear", None))
        self.title_button.setText(QCoreApplication.translate("MainWindow", u"Set Title", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save Note", None))
        self.export_button.setText(QCoreApplication.translate("MainWindow", u"Export Note", None))
        self.font_button.setText(QCoreApplication.translate("MainWindow", u"Choose Font", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status Application Ready", None))
        self.footer.setText(QCoreApplication.translate("MainWindow", u"Student Notes Pro v1.0", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.edit_menu.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.help_menu.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


