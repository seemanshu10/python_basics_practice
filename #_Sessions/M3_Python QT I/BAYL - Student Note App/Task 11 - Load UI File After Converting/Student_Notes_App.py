# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Student_Notes_App.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(859, 658)
        self.actionNew_File_Clear = QAction(MainWindow)
        self.actionNew_File_Clear.setObjectName(u"actionNew_File_Clear")
        self.actionSave_Note = QAction(MainWindow)
        self.actionSave_Note.setObjectName(u"actionSave_Note")
        self.actionExport_Note = QAction(MainWindow)
        self.actionExport_Note.setObjectName(u"actionExport_Note")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionChange_Title = QAction(MainWindow)
        self.actionChange_Title.setObjectName(u"actionChange_Title")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.subjectLabel = QLabel(self.centralwidget)
        self.subjectLabel.setObjectName(u"subjectLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.subjectLabel)

        self.subjectLineEdit = QLineEdit(self.centralwidget)
        self.subjectLineEdit.setObjectName(u"subjectLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.subjectLineEdit)

        self.categoryLabel = QLabel(self.centralwidget)
        self.categoryLabel.setObjectName(u"categoryLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.categoryLabel)

        self.categoryLineEdit = QLineEdit(self.centralwidget)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.categoryLineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout.setStretch(5, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 859, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew_File_Clear)
        self.menuFile.addAction(self.actionSave_Note)
        self.menuFile.addAction(self.actionExport_Note)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionChange_Title)
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNew_File_Clear)
        self.toolBar.addAction(self.actionSave_Note)
        self.toolBar.addAction(self.actionExport_Note)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionChange_Title)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Students Note App", None))
        self.actionNew_File_Clear.setText(QCoreApplication.translate("MainWindow", u"New File/Clear", None))
        self.actionSave_Note.setText(QCoreApplication.translate("MainWindow", u"Save Note", None))
        self.actionExport_Note.setText(QCoreApplication.translate("MainWindow", u"Export Note", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(statustip)
        self.actionCopy.setStatusTip(QCoreApplication.translate("MainWindow", u"Copied to clipboard", None))
#endif // QT_CONFIG(statustip)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(statustip)
        self.actionPaste.setStatusTip(QCoreApplication.translate("MainWindow", u"Paste", None))
#endif // QT_CONFIG(statustip)
        self.actionChange_Title.setText(QCoreApplication.translate("MainWindow", u"Change Title", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Students Notes Pro", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.subjectLabel.setText(QCoreApplication.translate("MainWindow", u"Subject:", None))
        self.categoryLabel.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Notes:", None))
        self.plainTextEdit.setPlaceholderText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Choose Clear", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Set Title", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Note", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Export Note", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Choose Font", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Status Application Ready", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Student Notes Pro v1.0", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

