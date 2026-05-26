from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QToolBar, QAction, QWidget,
    QStatusBar, QVBoxLayout, QPushButton, QGridLayout, QLineEdit, QFormLayout, QTextEdit,
    QMessageBox, QColorDialog, QFontDialog, QInputDialog, QFileDialog, QSizePolicy
)
from PySide2.QtGui import QTextCharFormat, QIcon
from PySide2.QtCore import Qt, Slot
import sys, os, qtawesome

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
ICON_FOLDER_PATH = os.path.join(FILE_PATH, "icons")

class MainWindow(QMainWindow):
    """Main application window for Student Notes Pro.

    This window builds the menu bar, toolbar, note form, status bar, and all
    signal connections needed to use the notes app.
    """

    def __init__(self):
        """Create the main window and initialize the user interface."""
        super().__init__()
        self.initUI()

    def initUI(self):
        """Build the user interface and connect widgets for the notes app."""
        self.setWindowTitle("Student Notes Pro")
        self.setGeometry(200, 200, 800, 600)
        self.setFixedSize(800, 600)

        # menu bar 
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.new_file_btn = self.file_menu.addAction("New File/Clear")
        self.save_file_btn = self.file_menu.addAction("Save Note")
        self.export_btn = self.file_menu.addAction("Export Note")
        self.file_menu.addSeparator()
        self.exit_btn = self.file_menu.addAction("Exit")
        
        # shortcuts
        self.new_file_btn.setShortcut("Ctrl+N")
        self.save_file_btn.setShortcut("Ctrl+S")
        self.export_btn.setShortcut("Ctrl+Shift+S")
        self.exit_btn.setShortcut("Ctrl+Q")
        self.save_file_btn.setEnabled(False)
        self.export_btn.setEnabled(False)

        self.new_file_btn.setIcon(qtawesome.icon('ei.file-new', color='#2980b9'))
        self.save_file_btn.setIcon(qtawesome.icon('fa5s.save', color='#2980b9'))
        self.export_btn.setIcon(qtawesome.icon('ph.export-bold', color='#2980b9'))
        self.exit_btn.setIcon(qtawesome.icon('mdi.exit-to-app', color="#a71a2d"))
        
        # edit menu 
        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.copy_btn = self.edit_menu.addAction("Copy")
        self.paste_btn = self.edit_menu.addAction("Paste")
        self.edit_menu.addSeparator()
        self.titlechange_btn = self.edit_menu.addAction("Change Title")

        # shortcuts
        self.copy_btn.setShortcut("Ctrl+C")
        self.paste_btn.setShortcut("Ctrl+V")
        self.titlechange_btn.setShortcut("Ctrl+T")

        self.copy_btn.setIcon(qtawesome.icon('fa5.copy', color='#2980b9'))
        self.paste_btn.setIcon(qtawesome.icon('fa6.paste', color='#2980b9'))
        self.titlechange_btn.setIcon(qtawesome.icon('mdi.format-title', color='#2980b9'))

        # Help Menu 
        self.help_menu = self.menu_bar.addMenu("Help")
        self.about_btn = self.help_menu.addAction("About")

        # shortcuts
        self.about_btn.setShortcut("F1")

        # Tool bar 
        self.toolbar = QToolBar() 
        # self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

        self.clear_tool = QAction(QIcon(os.path.join(ICON_FOLDER_PATH, "folder.png")), "Open", self)
        self.toolbar.addAction(self.clear_tool)

        self.save_tool = QAction(QIcon(os.path.join(ICON_FOLDER_PATH, "save.png")), "Save", self)
        self.toolbar.addAction(self.save_tool)

        self.export_tool = QAction(QIcon(os.path.join(ICON_FOLDER_PATH, "export.png")), "export", self)
        self.toolbar.addAction(self.export_tool)
        self.toolbar.addSeparator()

        self.copy_tool = QAction(QIcon(os.path.join(ICON_FOLDER_PATH, "copy.png")), "copy", self)
        self.toolbar.addAction(self.copy_tool)

        self.paste_tool = QAction(QIcon(os.path.join(ICON_FOLDER_PATH, "paste.png")), "paste", self)
        self.toolbar.addAction(self.paste_tool)
        self.toolbar.addSeparator()

        self.save_tool.setEnabled(False)
        self.export_tool.setEnabled(False)

        # central widget 
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # nested layout 
        self.widget_layout = QVBoxLayout()
        self.title_label = QLabel("Student Notes Pro")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFixedSize(800, 50)
        self.widget_layout.addWidget(self.title_label, alignment= Qt.AlignCenter)
        # self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.form_layout = QFormLayout()

        self.student_label = QLabel("Name:")
        self.student_name_line = QLineEdit()
        self.student_name_line.setPlaceholderText("Enter Name")

        self.subject_label = QLabel("Subject:")
        self.subject_name_line = QLineEdit()
        self.subject_name_line.setPlaceholderText("Enter Subject")

        self.category_label = QLabel("Category:")
        self.category_name_line = QLineEdit()
        self.category_name_line.setPlaceholderText("Enter Category")

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

        # Buttons layout 
        self.button_layout = QGridLayout()
        self.save_button = QPushButton("Save Note")
        self.save_button.setEnabled(False)
        self.clear_button = QPushButton("Clear")

        self.color_button = QPushButton("Choose Color")
        self.font_button = QPushButton("Choose Font")
        self.title_button = QPushButton("Set Title")
        self.export_button = QPushButton("Export Note")
        self.export_button.setEnabled(False)

        self.button_layout.addWidget(self.save_button, 0, 0)
        self.button_layout.addWidget(self.clear_button, 0, 1)

        self.button_layout.addWidget(self.color_button, 1, 0)
        self.button_layout.addWidget(self.font_button, 1, 1)
        self.button_layout.addWidget(self.title_button, 2, 0)
        self.button_layout.addWidget(self.export_button, 2, 1)

        self.widget_layout.addLayout(self.button_layout)

        # Status layout 
        self.status_label = QLabel("Status: Application Ready")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.widget_layout.addWidget(self.status_label)

        # Footer
        self.footer = QLabel("Student Notes Pro v1.0")
        self.footer.setAlignment(Qt.AlignCenter)
        self.widget_layout.addWidget(self.footer)
    
        self.central_widget.setLayout(self.widget_layout)

        # status bar  widget 
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Ready")

        # applying StyleSheet
        self.apply_stylesheet()

        # signals connection
        self.all_signals_connector()

        self.setStatusBar(self.status_bar)

        # Exit button 
        self.exit_btn.triggered.connect(self.close)

    # all connections 
    def all_signals_connector(self):
        """Connect user actions and menu commands to handler methods."""
        # Tool and menu bar connections
        self.new_file_btn.triggered.connect(self.open_file)
        self.save_file_btn.triggered.connect(self.confirm_save)
        self.export_btn.triggered.connect(self.choose_export_tool)
        
        # Copy Paste Action
        self.copy_btn.triggered.connect(self.copy_action)
        self.paste_btn.triggered.connect(self.paste_action)
        self.copy_tool.triggered.connect(self.copy_action)
        self.paste_tool.triggered.connect(self.paste_action)
        self.titlechange_btn.triggered.connect(self.choose_title_dialog)
        
        self.clear_tool.triggered.connect(self.open_file)
        self.save_tool.triggered.connect(self.confirm_save)

        self.export_tool.triggered.connect(self.choose_export_tool)

        self.about_btn.triggered.connect(self.about_tool_action)

        # connection 
        self.student_name_line.textChanged.connect(self.names_inputs)
        self.subject_name_line.textChanged.connect(self.subject_inputs)
        self.category_name_line.textChanged.connect(self.category_inputs)
        self.notes_textbox.textChanged.connect(self.notes_inputs)
        self.save_button.clicked.connect(self.confirm_save)
        self.clear_button.clicked.connect(self.confirm_clear_dialog)

        self.color_button.clicked.connect(self.choose_color_dialog)
        self.font_button.clicked.connect(self.choose_font_dialog)
        self.title_button.clicked.connect(self.choose_title_dialog)
        self.export_button.clicked.connect(self.choose_export_tool)
    
    @Slot()
    def about_tool_action(self):
        """Show the About dialog describing the application."""
        self.about_message = QMessageBox.about(
            None,
            "About Students Notes Pro",
            "Student Notes Pro v1.0\nA Simple Notes App to take notes?"
            )

    @Slot()
    def choose_export_tool(self):
        """Open a save dialog and export the current note when a path is chosen."""
        self.save_file_path, _ = QFileDialog.getSaveFileName(self, "Select File", "", "Text (*.txt)")
        if self.save_file_path:
            
            self.export_notes()

    def export_notes(self):
        """Write the current note contents and metadata to the selected file."""
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
    
    @Slot()
    def choose_title_dialog(self):
        """Ask the user for a new title and update the header label."""
        self.name, ok = QInputDialog.getText(self, "Change notes Title?", "Write New Title?")
        if ok:
            self.title_label.setText(f"{self.name}")
            print(self.name)

        self.status_bar.showMessage("Title Changed Successfully.")
        self.status_label.setText(f"Title Changed Successfully to: {self.title_label.text()}")

    @Slot()
    def choose_font_dialog(self):
        """Let the user pick a font and apply it to the notes text."""
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
    def choose_color_dialog(self):
        """Open a color picker and apply the chosen text color to the notes."""
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
    def confirm_new_file_dialog(self):
        """Ask the user to confirm creating a new note and clear fields if approved."""
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

    @Slot()
    def confirm_clear_dialog(self):
        """Confirm with the user before clearing all form fields."""
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
    def confirm_save(self):
        """Ask the user to confirm saving the note and then save it."""
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
    def names_inputs(self):
        """Update the status message when the student name field changes."""
        name = self.student_name_line.text().strip()
        if name:
            self.status_label.setText(f"Status: Typing name - {name}")
        else:
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def subject_inputs(self):
        """Update the status message when the subject field changes."""
        name = self.subject_name_line.text().strip()
        if name:
            self.status_label.setText(f"Status: Typing subject - {name}")
        else:
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def category_inputs(self):
        """Update the status message when the category field changes."""
        name = self.category_name_line.text().strip()
        if name:
            self.status_label.setText(f"Status: Typing Category - {name}")
        else:
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def notes_inputs(self):
        """Enable or disable save/export controls based on whether notes exist."""

        note = self.notes_textbox.toPlainText()
        
        if note:
            self.save_button.setEnabled(True)
            self.export_button.setEnabled(True)
            self.save_file_btn.setEnabled(True)
            self.export_btn.setEnabled(True)
            self.save_tool.setEnabled(True)
            self.export_tool.setEnabled(True)
            self.status_label.setText(f"Status: Note Updated")
            
        else:
            self.save_button.setEnabled(False)
            self.export_button.setEnabled(False)
            self.save_file_btn.setEnabled(False)
            self.export_btn.setEnabled(False)
            self.save_tool.setEnabled(False)
            self.export_tool.setEnabled(False)
            self.status_label.setText("Status: Waiting for input")

    def save_note(self):
        """Mark the current note as saved and update the status messages."""
        self.status_label.setText(f"Status: Note Saved for {self.student_name_line.text()}.")
        self.status_bar.showMessage("Note Saved Successfully.")

    @Slot()
    def clear_line_tool(self):
        """Clear all input fields and set the toolbar status to cleared."""
        self.student_name_line.clear()
        self.subject_name_line.clear()
        self.category_name_line.clear()
        self.notes_textbox.clear()

        self.status_label.setText("Status: All Fields Cleared")
        self.status_bar.showMessage("All Fields Cleared")
        # self.save_button.setEnabled(False)
 
    @Slot()
    def open_file(self):
        """Start a new note by confirming with the user and then clearing fields."""
        self.confirm_new_file_dialog()
        print("New File is opening")
        self.status_bar.showMessage("New Note Created")

    @Slot()
    def copy_action(self):
        """Handle copy actions and update the status bar."""
        print("Copied to clipboard.")
        self.status_bar.showMessage("Copied to Clipboard")

    @Slot()
    def paste_action(self):
        """Handle paste actions and update the status bar."""
        print("Text Pasted.")
        self.status_bar.showMessage("Text Pasted")

    def apply_stylesheet(self):
        """Load and apply the application stylesheet and widget styles."""

        stylesheet_path = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(stylesheet_path, "style.css")

        with open(stylesheet_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

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
  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())