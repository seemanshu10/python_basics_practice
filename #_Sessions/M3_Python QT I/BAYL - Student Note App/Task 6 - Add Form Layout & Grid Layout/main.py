import sys 

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox, QColorDialog, QFontDialog, QInputDialog, QFileDialog, QFormLayout, QGridLayout)

from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QTextCharFormat

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):    
        # Window creating
        self.setWindowTitle("Student Notes App")
        self.label = QLabel("Student Notes App")

        # Student Layout 
        self.student_layout = QHBoxLayout()
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

        # notes layout 
        self.notes_label = QLabel("Notes:")
        self.notes_textbox = QTextEdit()
        self.notes_textbox.setPlaceholderText("Write notes here....")

        # Buttons layout 
        self.button_layout = QGridLayout()
        self.save_button = QPushButton("Save Note")
        self.save_button.setEnabled(False)
        self.clear_button = QPushButton("Clear")

        self.color_button = QPushButton("Choose Color")
        self.font_button = QPushButton("Choose Font")
        self.title_button = QPushButton("Set Title")
        self.export_button = QPushButton("Export Note")

        self.button_layout.addWidget(self.save_button, 0, 0)
        self.button_layout.addWidget(self.clear_button, 0, 1)

        self.button_layout.addWidget(self.color_button, 1, 0)
        self.button_layout.addWidget(self.font_button, 1, 1)
        self.button_layout.addWidget(self.title_button, 2, 0)
        self.button_layout.addWidget(self.export_button, 2, 1)

        # Status layout 
        self.status_label = QLabel("Status: Waiting For Input")

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.label, alignment= Qt.AlignCenter)
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.notes_label)
        self.main_layout.addWidget(self.notes_textbox)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.status_label)

        # applying StyleSheet
        self.style_sheet()
        self.setLayout(self.main_layout)

        # signals connection
        self.all_signals_connector()

    # all connections 
    def all_signals_connector(self):
        # connection 
        self.student_name_line.textChanged.connect(self.names_inputs)
        self.subject_name_line.textChanged.connect(self.subject_inputs)
        self.category_name_line.textChanged.connect(self.category_inputs)
        self.notes_textbox.textChanged.connect(self.notes_inputs)
        self.save_button.clicked.connect(self.confirm_save)
        self.clear_button.clicked.connect(self.confirm_clear_ui)

        self.color_button.clicked.connect(self.choose_color_ui)
        self.font_button.clicked.connect(self.choose_font_ui)
        self.title_button.clicked.connect(self.choose_title_ui)
        self.export_button.clicked.connect(self.choose_export_ui)

    # style sheet function
    def style_sheet(self):
        self.label.setStyleSheet("""
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

        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: green;
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

        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: red;
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

        self.status_label.setStyleSheet("""
        QLabel{
            color: blue;
            font-style: italic;
        }
        """)

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

    # title change function
    def choose_title_ui(self):
        
        self.name, ok = QInputDialog.getText(self, "Change notes Title?", "Write New Title?")
        if ok:
            self.label.setText(f"{self.name}")
            print(self.name)

    # font selection function
    def choose_font_ui(self):
        ok, self.font_color = QFontDialog.getFont()
        
        if ok:
            fmt = QTextCharFormat()
            fmt.setFont(self.font_color)

            cursor = self.notes_textbox.textCursor()
            cursor.mergeCharFormat(fmt)

            self.notes_textbox.mergeCurrentCharFormat(fmt)

            self.status_label.setText(
                f"Selected color: {self.font_color.family()}"
            )
    
    # color choose notes function
    def choose_color_ui(self):
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

    def choose_export_ui(self):
        self.save_file_path, _ = QFileDialog.getSaveFileName(self, "Select File", "", "Text (*.html *.txt)")
        if self.save_file_path:
            self.status_label.setText(f"Exported Notes To:\n{self.save_file_path}")
            self.export_notes()

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

    def confirm_clear_ui(self):
        response = QMessageBox.question(
            None,
            "Clear All Fields. ",
            "Are you sure you want to Clear all the Fields?"
        )

        if response == QMessageBox.Yes:
            print("User confirmed to Clear Feilds.")
            self.clear_ui()
        else:
            print("User canceled to clear thew fields.")

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
    def save_note(self):
        self.status_label.setText("Status: Note Saved Successfully.")

    @Slot()
    def names_inputs(self):
        name = self.student_name_line.text().strip()
        if name:
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)
        
        if name:
            self.status_label.setText(f"Status: Typing name - {name}")
        else:
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def subject_inputs(self):
        name = self.subject_name_line.text().strip()
        if name:
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)
        
        if name:
            self.status_label.setText(f"Status: Typing subject - {name}")
        else:
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def category_inputs(self):
        name = self.category_name_line.text().strip()
        if name:
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)
        
        if name:
            self.status_label.setText(f"Status: Typing Category - {name}")
        else:
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def notes_inputs(self):

        note = self.notes_textbox.toPlainText()
        if note:
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)
        
        if note:
            self.status_label.setText(f"Status: Note Updated")
        else:
            self.status_label.setText("Status: Waiting for input")
        
    @Slot()
    def clear_ui(self):
        self.student_name_line.setText("")
        self.subject_name_line.setText("")
        self.category_name_line.setText("")
        self.notes_textbox.setText("")
        self.status_label.setText("Status: All Fields Cleared")
        self.save_button.setEnabled(False)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(500, 500)
    
    window.show()
    sys.exit(app.exec_())