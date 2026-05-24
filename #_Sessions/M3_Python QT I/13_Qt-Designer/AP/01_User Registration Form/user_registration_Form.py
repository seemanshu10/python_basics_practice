from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(256, 304)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.personal_info_grp = QGroupBox(Form)
        self.personal_info_grp.setObjectName(u"personal_info_grp")
        self.verticalLayout_4 = QVBoxLayout(self.personal_info_grp)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.personal_info_grp)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.lineEdit_name = QLineEdit(self.personal_info_grp)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout_4.addWidget(self.lineEdit_name)

        self.label_2 = QLabel(self.personal_info_grp)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit_email = QLineEdit(self.personal_info_grp)
        self.lineEdit_email.setObjectName(u"lineEdit_email")

        self.verticalLayout_4.addWidget(self.lineEdit_email)

        self.label_3 = QLabel(self.personal_info_grp)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit_password = QLineEdit(self.personal_info_grp)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.lineEdit_password)


        self.verticalLayout_2.addWidget(self.personal_info_grp)

        self.user_pref_grp = QGroupBox(Form)
        self.user_pref_grp.setObjectName(u"user_pref_grp")
        self.verticalLayout_6 = QVBoxLayout(self.user_pref_grp)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_newsletter = QCheckBox(self.user_pref_grp)
        self.checkBox_newsletter.setObjectName(u"checkBox_newsletter")
        self.checkBox_newsletter.setEnabled(True)
        font = QFont()
        font.setPointSize(10)
        self.checkBox_newsletter.setFont(font)
        self.checkBox_newsletter.setTabletTracking(False)
        self.checkBox_newsletter.setIconSize(QSize(50, 50))
        self.checkBox_newsletter.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBox_newsletter)

        self.checkBox_notifications = QCheckBox(self.user_pref_grp)
        self.checkBox_notifications.setObjectName(u"checkBox_notifications")
        self.checkBox_notifications.setFont(font)
        self.checkBox_notifications.setChecked(False)

        self.verticalLayout_5.addWidget(self.checkBox_notifications)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addWidget(self.user_pref_grp)

        self.button_submit = QPushButton(Form)
        self.button_submit.setObjectName(u"button_submit")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.button_submit.setFont(font1)
        self.button_submit.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.button_submit)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"User Registration Form", None))
        self.personal_info_grp.setTitle(QCoreApplication.translate("Form", u"Personal Information", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.lineEdit_password.setInputMask("")
        self.user_pref_grp.setTitle(QCoreApplication.translate("Form", u"User Preferences", None))
        self.checkBox_newsletter.setText(QCoreApplication.translate("Form", u"Subscribe to Newsletter", None))
        self.checkBox_notifications.setText(QCoreApplication.translate("Form", u"Enable Notifications", None))
        self.button_submit.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

