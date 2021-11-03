# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_axis.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_setAxisWidget(object):
    def setupUi(self, setAxisWidget):
        if not setAxisWidget.objectName():
            setAxisWidget.setObjectName(u"setAxisWidget")
        setAxisWidget.resize(398, 260)
        font = QFont()
        font.setPointSize(12)
        setAxisWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(setAxisWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(setAxisWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.frame_2 = QFrame(setAxisWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.isMax = QCheckBox(self.frame_2)
        self.isMax.setObjectName(u"isMax")

        self.horizontalLayout_2.addWidget(self.isMax)

        self.YLimitMax = QDoubleSpinBox(self.frame_2)
        self.YLimitMax.setObjectName(u"YLimitMax")
        self.YLimitMax.setReadOnly(True)
        self.YLimitMax.setMinimum(-9999999.000000000000000)
        self.YLimitMax.setMaximum(99999999.000000000000000)

        self.horizontalLayout_2.addWidget(self.YLimitMax)

        self.isMin = QCheckBox(self.frame_2)
        self.isMin.setObjectName(u"isMin")

        self.horizontalLayout_2.addWidget(self.isMin)

        self.YLimitMin = QDoubleSpinBox(self.frame_2)
        self.YLimitMin.setObjectName(u"YLimitMin")
        self.YLimitMin.setReadOnly(True)
        self.YLimitMin.setMinimum(-9999999.000000000000000)
        self.YLimitMin.setMaximum(99999999.000000000000000)

        self.horizontalLayout_2.addWidget(self.YLimitMin)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(setAxisWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.YValueMax = QDoubleSpinBox(self.frame)
        self.YValueMax.setObjectName(u"YValueMax")
        self.YValueMax.setReadOnly(True)
        self.YValueMax.setMinimum(-9999999.000000000000000)
        self.YValueMax.setMaximum(99999999.000000000000000)

        self.horizontalLayout.addWidget(self.YValueMax)

        self.YValueMin = QDoubleSpinBox(self.frame)
        self.YValueMin.setObjectName(u"YValueMin")
        self.YValueMin.setReadOnly(True)
        self.YValueMin.setMinimum(-9999999.000000000000000)
        self.YValueMin.setMaximum(99999999.000000000000000)

        self.horizontalLayout.addWidget(self.YValueMin)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(setAxisWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.XValueMax = QDoubleSpinBox(self.frame_3)
        self.XValueMax.setObjectName(u"XValueMax")
        self.XValueMax.setReadOnly(True)
        self.XValueMax.setMaximum(99999999.000000000000000)
        self.XValueMax.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_3.addWidget(self.XValueMax)

        self.XValueMin = QDoubleSpinBox(self.frame_3)
        self.XValueMin.setObjectName(u"XValueMin")
        self.XValueMin.setReadOnly(True)
        self.XValueMin.setMaximum(99999999.000000000000000)

        self.horizontalLayout_3.addWidget(self.XValueMin)


        self.verticalLayout.addWidget(self.frame_3)

        self.autoSetBox = QCheckBox(setAxisWidget)
        self.autoSetBox.setObjectName(u"autoSetBox")
        self.autoSetBox.setChecked(True)

        self.verticalLayout.addWidget(self.autoSetBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(setAxisWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(65, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(setAxisWidget)
        self.pushButton.clicked.connect(setAxisWidget.returnOk)
        self.isMax.clicked.connect(setAxisWidget.editMax)
        self.isMin.clicked.connect(setAxisWidget.editMin)
        self.autoSetBox.clicked.connect(setAxisWidget.setAuto)
        self.pushButton_2.clicked.connect(setAxisWidget.Close)

        QMetaObject.connectSlotsByName(setAxisWidget)
    # setupUi

    def retranslateUi(self, setAxisWidget):
        setAxisWidget.setWindowTitle(QCoreApplication.translate("setAxisWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("setAxisWidget", u"Y\u8f74\u9650\u5236", None))
        self.isMax.setText(QCoreApplication.translate("setAxisWidget", u"\u6700\u5927", None))
        self.isMin.setText(QCoreApplication.translate("setAxisWidget", u"\u6700\u5c0f", None))
        self.label_2.setText(QCoreApplication.translate("setAxisWidget", u"Y\u8f74\u5f53\u524d\u503c", None))
        self.label_3.setText(QCoreApplication.translate("setAxisWidget", u"X\u8f74\u5f53\u524d\u503c", None))
        self.autoSetBox.setText(QCoreApplication.translate("setAxisWidget", u"\u81ea\u52a8\u4f38\u7f29", None))
        self.pushButton.setText(QCoreApplication.translate("setAxisWidget", u"\u786e\u5b9a", None))
        self.pushButton_2.setText(QCoreApplication.translate("setAxisWidget", u"\u53d6\u6d88", None))
    # retranslateUi

