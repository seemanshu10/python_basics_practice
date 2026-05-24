# -*- coding: utf-8 -*-


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(346, 213)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.lineEdit_username = QLineEdit(self.groupBox)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.verticalLayout_4.addWidget(self.lineEdit_username)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit_password = QLineEdit(self.groupBox)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.lineEdit_password)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.comboBox_language = QComboBox(Form)
        self.comboBox_language.setObjectName(u"comboBox_language")
        list_of_languages = ["English", "French", "Spanish"]
        self.comboBox_language.addItems(list_of_languages)

        self.verticalLayout_3.addWidget(self.comboBox_language)

        self.button_login = QPushButton(Form)
        self.button_login.setObjectName(u"button_login")

        self.verticalLayout_3.addWidget(self.button_login)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Login Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Login Information", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username", None))
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("Form", u"Enter username", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Password", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Select Language", None))
        self.button_login.setText(QCoreApplication.translate("Form", u"Login", None))
    # retranslateUi

