from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

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

