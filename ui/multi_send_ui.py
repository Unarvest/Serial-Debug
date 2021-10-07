# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'multi_send.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import icoPack_rc

class Ui_multi_send(object):
    def setupUi(self, multi_send):
        if not multi_send.objectName():
            multi_send.setObjectName(u"multi_send")
        multi_send.resize(704, 51)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(multi_send.sizePolicy().hasHeightForWidth())
        multi_send.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        multi_send.setFont(font)
        self.horizontalLayout = QHBoxLayout(multi_send)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.pushButton = QPushButton(multi_send)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/flat/flatwhite/calendar_prevmonth.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(multi_send)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Cascadia Code"])
        font2.setPointSize(12)
        self.lineEdit.setFont(font2)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.retranslateUi(multi_send)
        self.lineEdit.returnPressed.connect(multi_send.sendMsg)
        self.pushButton.clicked.connect(multi_send.sendMsg)

        QMetaObject.connectSlotsByName(multi_send)
    # setupUi

    def retranslateUi(self, multi_send):
        multi_send.setWindowTitle(QCoreApplication.translate("multi_send", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("multi_send", u" \u53d1\u9001", None))
        self.lineEdit.setText("")
    # retranslateUi

