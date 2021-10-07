# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'draw_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLineEdit, QListWidget, QListWidgetItem, QPlainTextEdit,
    QProgressBar, QPushButton, QRadioButton, QScrollBar,
    QSizePolicy, QVBoxLayout, QWidget)
import icoPack_rc

class Ui_Draw_Widget(object):
    def setupUi(self, Draw_Widget):
        if not Draw_Widget.objectName():
            Draw_Widget.setObjectName(u"Draw_Widget")
        Draw_Widget.resize(1182, 649)
        self.verticalLayout = QVBoxLayout(Draw_Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphFrame = QFrame(Draw_Widget)
        self.graphFrame.setObjectName(u"graphFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.graphFrame.sizePolicy().hasHeightForWidth())
        self.graphFrame.setSizePolicy(sizePolicy)
        self.graphFrame.setMinimumSize(QSize(0, 0))
        self.graphFrame.setCursor(QCursor(Qt.CrossCursor))
        self.graphFrame.setFrameShape(QFrame.Box)
        self.graphFrame.setFrameShadow(QFrame.Raised)
        self.graphFrame.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.graphFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.graphLayout = QVBoxLayout()
        self.graphLayout.setSpacing(6)
        self.graphLayout.setObjectName(u"graphLayout")
        self.graphLayout.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout_5.addLayout(self.graphLayout)


        self.verticalLayout.addWidget(self.graphFrame)

        self.graphSetFrame = QFrame(Draw_Widget)
        self.graphSetFrame.setObjectName(u"graphSetFrame")
        self.graphSetFrame.setFrameShape(QFrame.StyledPanel)
        self.graphSetFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.graphSetFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.progressBar_2 = QProgressBar(self.graphSetFrame)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)
        self.progressBar_2.setOrientation(Qt.Vertical)
        self.progressBar_2.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_9.addWidget(self.progressBar_2)

        self.graphSetFrame_2 = QFrame(self.graphSetFrame)
        self.graphSetFrame_2.setObjectName(u"graphSetFrame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.graphSetFrame_2.sizePolicy().hasHeightForWidth())
        self.graphSetFrame_2.setSizePolicy(sizePolicy1)
        self.graphSetFrame_2.setMinimumSize(QSize(0, 0))
        self.graphSetFrame_2.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.graphSetFrame_2)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.graphSetFrame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 4, 0)
        self.connectStateRadioButton_2 = QRadioButton(self.frame)
        self.connectStateRadioButton_2.setObjectName(u"connectStateRadioButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.connectStateRadioButton_2.sizePolicy().hasHeightForWidth())
        self.connectStateRadioButton_2.setSizePolicy(sizePolicy2)
        self.connectStateRadioButton_2.setMaximumSize(QSize(25, 16777215))
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.connectStateRadioButton_2.setFont(font)
        self.connectStateRadioButton_2.setStyleSheet(u"QRadioButton::indicator {width:25px;height:25px;border-radius:25px}\n"
"QRadioButton::indicator:checked {image: url(:/ico/ico/\u6253\u5f00.png);}\n"
"QRadioButton::indicator:unchecked {image: url(:/ico/ico/\u5173\u95ed.png);}\n"
"")
        self.connectStateRadioButton_2.setIconSize(QSize(0, 0))
#if QT_CONFIG(shortcut)
        self.connectStateRadioButton_2.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.connectStateRadioButton_2.setCheckable(False)
        self.connectStateRadioButton_2.setChecked(False)
        self.connectStateRadioButton_2.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.connectStateRadioButton_2)

        self.graphScrollBar = QScrollBar(self.frame)
        self.graphScrollBar.setObjectName(u"graphScrollBar")
        self.graphScrollBar.setMinimum(0)
        self.graphScrollBar.setMaximum(41)
        self.graphScrollBar.setPageStep(100)
        self.graphScrollBar.setValue(0)
        self.graphScrollBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.graphScrollBar)

        self.stopShowButton_2 = QPushButton(self.frame)
        self.stopShowButton_2.setObjectName(u"stopShowButton_2")
        sizePolicy2.setHeightForWidth(self.stopShowButton_2.sizePolicy().hasHeightForWidth())
        self.stopShowButton_2.setSizePolicy(sizePolicy2)
        self.stopShowButton_2.setMinimumSize(QSize(0, 27))
        self.stopShowButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.stopShowButton_2.setFont(font)
        self.stopShowButton_2.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/MainWin/ico/20200510-235146.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.stopShowButton_2.setIcon(icon)
        self.stopShowButton_2.setIconSize(QSize(22, 22))

        self.horizontalLayout_6.addWidget(self.stopShowButton_2)

        self.saveDataButton_2 = QPushButton(self.frame)
        self.saveDataButton_2.setObjectName(u"saveDataButton_2")
        sizePolicy2.setHeightForWidth(self.saveDataButton_2.sizePolicy().hasHeightForWidth())
        self.saveDataButton_2.setSizePolicy(sizePolicy2)
        self.saveDataButton_2.setMinimumSize(QSize(0, 27))
        self.saveDataButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.saveDataButton_2.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/MainWin/ico/20200510-223336.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.saveDataButton_2.setIcon(icon1)
        self.saveDataButton_2.setIconSize(QSize(22, 22))

        self.horizontalLayout_6.addWidget(self.saveDataButton_2)

        self.resetButton = QPushButton(self.frame)
        self.resetButton.setObjectName(u"resetButton")
        sizePolicy2.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy2)
        self.resetButton.setMinimumSize(QSize(0, 27))
        self.resetButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/setting/ico/\u8bbe\u7f6e/20200517-232159.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.resetButton.setIcon(icon2)
        self.resetButton.setIconSize(QSize(22, 22))

        self.horizontalLayout_6.addWidget(self.resetButton)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.graphSetFrame_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(2, 5, 0, 0)
        self.graphReceiveBox = QPlainTextEdit(self.frame_3)
        self.graphReceiveBox.setObjectName(u"graphReceiveBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(11)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.graphReceiveBox.sizePolicy().hasHeightForWidth())
        self.graphReceiveBox.setSizePolicy(sizePolicy4)
        self.graphReceiveBox.setMaximumSize(QSize(16777215, 16777215))
        self.graphReceiveBox.setFont(font)
        self.graphReceiveBox.setFrameShape(QFrame.Box)
        self.graphReceiveBox.setFrameShadow(QFrame.Raised)
        self.graphReceiveBox.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.graphReceiveBox)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(7)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy5)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget_2 = QListWidget(self.frame_4)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_2.addWidget(self.listWidget_2)


        self.horizontalLayout_21.addWidget(self.frame_4)


        self.horizontalLayout_22.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy6)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(7)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(5, 5, 0, 0)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.stopShowButton = QPushButton(self.frame_5)
        self.stopShowButton.setObjectName(u"stopShowButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.stopShowButton.sizePolicy().hasHeightForWidth())
        self.stopShowButton.setSizePolicy(sizePolicy7)
        self.stopShowButton.setMinimumSize(QSize(168, 27))
        self.stopShowButton.setMaximumSize(QSize(16777215, 16777215))
        self.stopShowButton.setFont(font)
        self.stopShowButton.setCursor(QCursor(Qt.ArrowCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Mainico/ico/20200511-103826.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.stopShowButton.setIcon(icon3)
        self.stopShowButton.setIconSize(QSize(22, 22))

        self.horizontalLayout_24.addWidget(self.stopShowButton)

        self.saveDataButton = QPushButton(self.frame_5)
        self.saveDataButton.setObjectName(u"saveDataButton")
        sizePolicy7.setHeightForWidth(self.saveDataButton.sizePolicy().hasHeightForWidth())
        self.saveDataButton.setSizePolicy(sizePolicy7)
        self.saveDataButton.setMinimumSize(QSize(168, 27))
        self.saveDataButton.setMaximumSize(QSize(16777215, 16777215))
        self.saveDataButton.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/setting/ico/\u8bbe\u7f6e/20200517-232213.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.saveDataButton.setIcon(icon4)
        self.saveDataButton.setIconSize(QSize(22, 22))

        self.horizontalLayout_24.addWidget(self.saveDataButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_24, 3, 0, 1, 2)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(3)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.addGraphColor = QPushButton(self.frame_5)
        self.addGraphColor.setObjectName(u"addGraphColor")
        sizePolicy7.setHeightForWidth(self.addGraphColor.sizePolicy().hasHeightForWidth())
        self.addGraphColor.setSizePolicy(sizePolicy7)
        self.addGraphColor.setMinimumSize(QSize(0, 27))
        self.addGraphColor.setMaximumSize(QSize(16777215, 16777215))
        self.addGraphColor.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/MainWin/ico/20200510-223440.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.addGraphColor.setIcon(icon5)
        self.addGraphColor.setIconSize(QSize(22, 22))

        self.horizontalLayout_23.addWidget(self.addGraphColor)

        self.clearDataButton = QPushButton(self.frame_5)
        self.clearDataButton.setObjectName(u"clearDataButton")
        sizePolicy7.setHeightForWidth(self.clearDataButton.sizePolicy().hasHeightForWidth())
        self.clearDataButton.setSizePolicy(sizePolicy7)
        self.clearDataButton.setMinimumSize(QSize(168, 27))
        self.clearDataButton.setMaximumSize(QSize(16777215, 16777215))
        self.clearDataButton.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/MainWin/ico/20200510-223403.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.clearDataButton.setIcon(icon6)
        self.clearDataButton.setIconSize(QSize(22, 22))

        self.horizontalLayout_23.addWidget(self.clearDataButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_23, 2, 0, 1, 2)

        self.frame_17 = QFrame(self.frame_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.addGraphColor_2 = QPushButton(self.frame_17)
        self.addGraphColor_2.setObjectName(u"addGraphColor_2")
        sizePolicy2.setHeightForWidth(self.addGraphColor_2.sizePolicy().hasHeightForWidth())
        self.addGraphColor_2.setSizePolicy(sizePolicy2)
        self.addGraphColor_2.setMinimumSize(QSize(0, 27))
        self.addGraphColor_2.setMaximumSize(QSize(16777215, 16777215))
        self.addGraphColor_2.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/Mainico/ico/20200510-221424.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.addGraphColor_2.setIcon(icon7)
        self.addGraphColor_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.addGraphColor_2)

        self.lineEdit_3 = QLineEdit(self.frame_17)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy8)

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.gridLayout_2.addWidget(self.frame_17, 1, 0, 1, 1)


        self.horizontalLayout_22.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.horizontalLayout_9.addWidget(self.graphSetFrame_2)


        self.verticalLayout.addWidget(self.graphSetFrame)


        self.retranslateUi(Draw_Widget)
        self.graphScrollBar.sliderMoved.connect(Draw_Widget.moveGraph)
        self.graphScrollBar.sliderPressed.connect(Draw_Widget.stopUpdate)
        self.graphScrollBar.sliderReleased.connect(Draw_Widget.continueUpdate)
        self.resetButton.clicked.connect(Draw_Widget.resetGraph)

        QMetaObject.connectSlotsByName(Draw_Widget)
    # setupUi

    def retranslateUi(self, Draw_Widget):
        Draw_Widget.setWindowTitle(QCoreApplication.translate("Draw_Widget", u"Form", None))
        self.progressBar_2.setFormat(QCoreApplication.translate("Draw_Widget", u"%p", None))
#if QT_CONFIG(tooltip)
        self.connectStateRadioButton_2.setToolTip(QCoreApplication.translate("Draw_Widget", u"\u5207\u6362\u4e32\u53e3\u72b6\u6001", None))
#endif // QT_CONFIG(tooltip)
        self.connectStateRadioButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.stopShowButton_2.setToolTip(QCoreApplication.translate("Draw_Widget", u"\u6682\u505c\u7ed8\u56fe\u529f\u80fd", None))
#endif // QT_CONFIG(tooltip)
        self.stopShowButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.saveDataButton_2.setToolTip(QCoreApplication.translate("Draw_Widget", u"\u5bfc\u51fa\u7ed8\u56fe\u533a\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.saveDataButton_2.setText("")
        self.resetButton.setText("")
#if QT_CONFIG(tooltip)
        self.stopShowButton.setToolTip(QCoreApplication.translate("Draw_Widget", u"\u6682\u505c\u7ed8\u56fe\u529f\u80fd", None))
#endif // QT_CONFIG(tooltip)
        self.stopShowButton.setText(QCoreApplication.translate("Draw_Widget", u" \u7f16\u8f91\u66f2\u7ebf", None))
#if QT_CONFIG(tooltip)
        self.saveDataButton.setToolTip(QCoreApplication.translate("Draw_Widget", u"\u5bfc\u51fa\u7ed8\u56fe\u533a\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.saveDataButton.setText(QCoreApplication.translate("Draw_Widget", u" \u5750\u6807\u8f74\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.addGraphColor.setToolTip(QCoreApplication.translate("Draw_Widget", u"\u66f2\u7ebf\u4e0e\u989c\u8272\u5bf9\u5e94", None))
#endif // QT_CONFIG(tooltip)
        self.addGraphColor.setText(QCoreApplication.translate("Draw_Widget", u" \u6dfb\u52a0\u66f2\u7ebf", None))
#if QT_CONFIG(tooltip)
        self.clearDataButton.setToolTip(QCoreApplication.translate("Draw_Widget", u"\u6e05\u7a7a\u6240\u6709\uff01\uff01", None))
#endif // QT_CONFIG(tooltip)
        self.clearDataButton.setText(QCoreApplication.translate("Draw_Widget", u" \u6e05\u7a7a\u66f2\u7ebf", None))
#if QT_CONFIG(tooltip)
        self.addGraphColor_2.setToolTip(QCoreApplication.translate("Draw_Widget", u"\u66f2\u7ebf\u4e0e\u989c\u8272\u5bf9\u5e94", None))
#endif // QT_CONFIG(tooltip)
        self.addGraphColor_2.setText("")
    # retranslateUi

