# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Serial_MainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFontComboBox, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTextBrowser, QToolBox, QToolButton, QVBoxLayout,
    QWidget)
import icoPack_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1059, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(790, 550))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Mainico/ico/Main.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QPalette{background:#FFFFFF;}*{outline:0px;color:#57595B;}\n"
"\n"
"QWidget[form=\"true\"],QLabel[frameShape=\"1\"]{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"]{\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"] .QFrame{\n"
"border:1px solid #57595B;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"] QLabel,QWidget[form=\"title\"] QLabel{\n"
"border-radius:0px;\n"
"color:#57595B;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QWidget[form=\"title\"],QWidget[nav=\"left\"],QWidget[nav=\"top\"] QAbstractButton{\n"
"border-style:none;\n"
"border-radius:0px;\n"
"padding:5px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QWidget[nav=\"top\"] QAbstractButton:hover,QWidget[nav=\"top\"] QAbstractButton:pressed,QWidget[nav=\"top\"] QAbstractButton:checked{\n"
"border-style:solid;\n"
"border-width:0px 0px 2px 0px;\n"
"padding:4px 4px 2px 4px;\n"
"border-color:#00BB9E;\n"
"backg"
                        "round:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton{\n"
"border-radius:0px;\n"
"color:#57595B;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton:hover{\n"
"color:#FFFFFF;\n"
"background-color:#00BB9E;\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton:checked,QWidget[nav=\"left\"] QAbstractButton:pressed{\n"
"color:#57595B;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 2px;\n"
"padding:4px 4px 4px 2px;\n"
"border-color:#00BB9E;\n"
"background-color:#FFFFFF;\n"
"}\n"
"\n"
"QWidget[video=\"true\"] QLabel{\n"
"color:#57595B;\n"
"border:1px solid #B6B6B6;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QWidget[video=\"true\"] QLabel:focus{\n"
"border:1px solid #00BB9E;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPlainTextEdit,QSpi"
                        "nBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#00BB9E;\n"
"selection-color:#FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{\n"
"border:1px solid #B6B6B6;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"]{\n"
"lineedit-password-character:9679;\n"
"}\n"
"\n"
"/* .QFrame{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:3px;\n"
"} */\n"
"\n"
".QGroupBox{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:5px;\n"
"margin-top:3ex;\n"
"}\n"
"\n"
".QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"position:relative;\n"
"left:10px;\n"
"}\n"
"\n"
".QPushButton,.QToolButton{\n"
"border-style:none;\n"
"border"
                        ":1px solid #B6B6B6;\n"
"color:#57595B;\n"
"padding:5px;\n"
"min-height:15px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
".QPushButton:hover,.QToolButton:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
".QPushButton:pressed,.QToolButton:pressed{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
".QToolButton::menu-indicator{\n"
"image:None;\n"
"}\n"
"\n"
"QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{\n"
"border-radius:3px;\n"
"color:#57595B;\n"
"padding:3px;\n"
"margin:0px;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{\n"
"color:#FFFFFF;\n"
"margin:1px 1px 2px 1px;\n"
"background-color:rgba(51,127,209,230);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
""
                        "color:#FFFFFF;\n"
"margin:1px 1px 2px 1px;\n"
"background-color:rgba(238,0,0,128);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"width:15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"image:url(:/flat/flatwhite/radiobutton_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked:disabled{\n"
"image:url(:/flat/flatwhite/radiobutton_unchecked_disable.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image:url(:/flat/flatwhite/radiobutton_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked:disabled{\n"
"image:url(:/flat/flatwhite/radiobutton_checked_disable.png);\n"
"}\n"
"\n"
"QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{\n"
"padding:0px -3px 0px 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{\n"
"image"
                        ":url(:/flat/flatwhite/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{\n"
"image:url(:/flat/flatwhite/checkbox_unchecked_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{\n"
"image:url(:/flat/flatwhite/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{\n"
"image:url(:/flat/flatwhite/checkbox_checked_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{\n"
"image:url(:/flat/flatwhite/checkbox_parcial.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTr"
                        "eeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{\n"
"image:url(:/flat/flatwhite/checkbox_parcial_disable.png);\n"
"}\n"
"\n"
"QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{\n"
"image:url(:/flat/flatwhite/add_top.png);\n"
"width:10px;\n"
"height:10px;\n"
"padding:2px 5px 0px 0px;\n"
"}\n"
"\n"
"QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{\n"
"image:url(:/flat/flatwhite/add_bottom.png);\n"
"width:10px;\n"
"height:10px;\n"
"padding:0px 5px 2px 0px;\n"
"}\n"
"\n"
"QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{\n"
"top:-2px;\n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pre"
                        "ssed{\n"
"bottom:-2px;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit[calendarPopup=\"true\"]::down-arrow,QTimeEdit[calendarPopup=\"true\"]::down-arrow,QDateTimeEdit[calendarPopup=\"true\"]::down-arrow{\n"
"image:url(:/flat/flatwhite/add_bottom.png);\n"
"width:10px;\n"
"height:10px;\n"
"right:2px;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{\n"
"subcontrol-origin:padding;\n"
"subcontrol-position:top right;\n"
"width:15px;\n"
"border-left-width:0px;\n"
"border-left-style:solid;\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius:3px;\n"
"border-left-color:#B6B6B6;\n"
"}\n"
"\n"
"QComboBox::drop-down:on{\n"
"top:1px;\n"
"}\n"
"\n"
"QMenuBar::item{\n"
"color:#57595B;\n"
"background-color:#E4E4E4;\n"
"margin:0px;\n"
"padding:3px 10px;\n"
"}\n"
"\n"
"QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{\n"
"color:#57595B;\n"
"background-color:#E4E4E4;\n"
"border:1px solid #B6B6B6;\n"
"margin:0px;\n"
"}\n"
"\n"
"QMenu::item{\n"
"padding:3px 20px;\n"
""
                        "}\n"
"\n"
"QMenu::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QMenu::item:selected,QMenuBar::item:selected{\n"
"color:#57595B;\n"
"border:0px solid #B6B6B6;\n"
"background:#F6F6F6;\n"
"}\n"
"\n"
"QMenu::separator{\n"
"height:1px;\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QProgressBar{\n"
"min-height:10px;\n"
"background:#E4E4E4;\n"
"border-radius:5px;\n"
"text-align:center;\n"
"border:1px solid #E4E4E4;\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"border-radius:5px;\n"
"background-color:#B6B6B6;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"background:#E4E4E4;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background:#E4E4E4;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"background:#B6B6B6;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:13px;\n"
"margin-top:-3px;\n"
"margin-bottom:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx"
                        ":0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);\n"
"}\n"
"\n"
"QSlider::groove:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"height:14px;\n"
"margin-left:-3px;\n"
"margin-right:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"background:#E4E4E4;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-height:12px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"background:#B6B6B6;\n"
"min-width:50px;\n"
"border-radius:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::add-"
                        "page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"background:#E4E4E4;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background:#B6B6B6;\n"
"min-height:50px;\n"
"border-radius:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QTabWidget::pane{\n"
"border:1px solid #"
                        "B6B6B6;\n"
"selection-background-color:#F6F6F6;\n"
"background-color: rgb(255, 255, 255);\n"
"selection-color:#57595B;\n"
"alternate-background-color:#F6F6F6;\n"
"gridline-color:#B6B6B6;\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children{\n"
"margin:4px;\n"
"border-image:url(:/flat/flatwhite/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children{\n"
"margin:4px;\n"
"border-image:url(:/flat/flatwhite/branch_close.png);\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QTableView::item:hover,QListView::item:hover,QTreeView::item:hover,QHeaderView{\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTableView::item,QListView::item,QTreeView::item{\n"
""
                        "padding:1px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QHeaderView::section,QTableCornerButton:section{\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#57595B;\n"
"border:1px solid #B6B6B6;\n"
"border-left-width:0px;\n"
"border-right-width:1px;\n"
"border-top-width:0px;\n"
"border-bottom-width:1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"border:1px solid #B6B6B6;\n"
"color:#57595B;\n"
"margin:0px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTabBar::tab:selected,QTabBar::tab:hover{\n"
"border-style:solid;\n"
"border-color:#00BB9E;\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"QTabBar::tab:top,QTabBar::tab:bottom{\n"
"padding:3px 8px 3px 8px;\n"
"}\n"
"\n"
"QTabBar::tab:left,QTabBar::tab:right{\n"
"padding:8px 3px 8px 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected,QTabBar::tab:top:hover{\n"
"border-width:2px 0px 0px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected,QTabBar::tab:right:ho"
                        "ver{\n"
"border-width:0px 0px 0px 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{\n"
"border-width:0px 0px 2px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected,QTabBar::tab:left:hover{\n"
"border-width:0px 2px 0px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{\n"
"border-left-width:1px;\n"
"border-left-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{\n"
"border-top-width:1px;\n"
"border-top-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{\n"
"border-right-width:1px;\n"
"border-right-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{\n"
"border-bottom-width:1px;\n"
"borde"
                        "r-bottom-color:#B6B6B6;\n"
"}\n"
"\n"
"QStatusBar::item{\n"
"border:0px solid #E4E4E4;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{\n"
"padding:3px;\n"
"border-radius:5px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QToolTip{\n"
"border:0px solid #57595B;\n"
"padding:1px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QToolBox::tab:selected{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QPrintPreviewDialog QToolButton{\n"
"border:0px solid #57595B;\n"
"border-radius:0px;\n"
"margin:0px;\n"
"padding:3px;\n"
"background:none;\n"
"}\n"
"\n"
"QColorDialog QPushButton,QFileDialog QPushButton{\n"
"min-width:80px;\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth{\n"
"icon-size:0px;\n"
"min"
                        "-width:20px;\n"
"image:url(:/flat/flatwhite/calendar_prevmonth.png);\n"
"}\n"
"\n"
"QToolButton#qt_calendar_nextmonth{\n"
"icon-size:0px;\n"
"min-width:20px;\n"
"image:url(:/flat/flatwhite/calendar_nextmonth.png);\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{\n"
"border:0px solid #57595B;\n"
"border-radius:3px;\n"
"margin:3px 3px 3px 3px;\n"
"padding:3px;\n"
"background:none;\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{\n"
"border:1px solid #B6B6B6;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox#qt_calendar_yearedit{\n"
"margin:2px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::menu-indicator{\n"
"image:None;\n"
""
                        "}\n"
"\n"
"QCalendarWidget QTableView{\n"
"border-width:0px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"border:1px solid #B6B6B6;\n"
"border-width:1px 1px 0px 1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"min-height:20px;\n"
"min-width:10px;\n"
"}\n"
"\n"
"QTableView[model=\"true\"]::item{\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit"
                        ",QTimeEdit,QDateTimeEdit{\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"QTabWidget::pane:top{top:-1px;}\n"
"QTabWidget::pane:bottom{bottom:-1px;}\n"
"QTabWidget::pane:left{right:-1px;}\n"
"QTabWidget::pane:right{left:-1px;}\n"
"\n"
"*:disabled{\n"
"background:#FFFFFF;\n"
"border-color:#E4E4E4;\n"
"color:#B6B6B6;\n"
"}\n"
"\n"
"/*TextColor:#57595B*/\n"
"/*PanelColor:#FFFFFF*/\n"
"/*BorderColor:#B6B6B6*/\n"
"/*NormalColorStart:#E4E4E4*/\n"
"/*NormalColorEnd:#E4E4E4*/\n"
"/*DarkColorStart:#F6F6F6*/\n"
"/*DarkColorEnd:#F6F6F6*/\n"
"/*HighColor:#00BB9E*/")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_17 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.tabWidget.setFont(font1)
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(28, 28))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.Main = QWidget()
        self.Main.setObjectName(u"Main")
        self.horizontalLayout_2 = QHBoxLayout(self.Main)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(11, 8, 11, 8)
        self.mainLeftWidget = QTabWidget(self.Main)
        self.mainLeftWidget.setObjectName(u"mainLeftWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainLeftWidget.sizePolicy().hasHeightForWidth())
        self.mainLeftWidget.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.mainLeftWidget.setFont(font2)
        self.mainLeftWidget.setTabPosition(QTabWidget.South)
        self.mainLeftWidget.setTabShape(QTabWidget.Rounded)
        self.mainLeftWidget.setIconSize(QSize(18, 18))
        self.mainLeftWidget.setElideMode(Qt.ElideNone)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_19 = QVBoxLayout(self.tab_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setFont(font2)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 291, 573))
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy4)
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setFont(font2)
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(8, 8, 8, 9)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(-1, -1, -1, 5)
        self.byteSizeLabel = QLabel(self.scrollAreaWidgetContents)
        self.byteSizeLabel.setObjectName(u"byteSizeLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.byteSizeLabel.sizePolicy().hasHeightForWidth())
        self.byteSizeLabel.setSizePolicy(sizePolicy5)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.byteSizeLabel.setFont(font3)

        self.gridLayout.addWidget(self.byteSizeLabel, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(11, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 1, 4, 1)

        self.stopBitsLabel = QLabel(self.scrollAreaWidgetContents)
        self.stopBitsLabel.setObjectName(u"stopBitsLabel")
        sizePolicy5.setHeightForWidth(self.stopBitsLabel.sizePolicy().hasHeightForWidth())
        self.stopBitsLabel.setSizePolicy(sizePolicy5)
        self.stopBitsLabel.setFont(font3)

        self.gridLayout.addWidget(self.stopBitsLabel, 5, 0, 1, 1)

        self.parityComboBox = QComboBox(self.scrollAreaWidgetContents)
        icon1 = QIcon()
        icon1.addFile(u":/MainWin/ico/20200510-223427.ico", QSize(), QIcon.Normal, QIcon.On)
        self.parityComboBox.addItem(icon1, "")
        self.parityComboBox.addItem(icon1, "")
        self.parityComboBox.addItem(icon1, "")
        self.parityComboBox.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/MainWin/ico/20200510-223427.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.parityComboBox.addItem(icon2, "")
        self.parityComboBox.addItem(icon2, "")
        self.parityComboBox.setObjectName(u"parityComboBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.parityComboBox.sizePolicy().hasHeightForWidth())
        self.parityComboBox.setSizePolicy(sizePolicy6)
        self.parityComboBox.setFont(font2)
        self.parityComboBox.setIconSize(QSize(18, 18))

        self.gridLayout.addWidget(self.parityComboBox, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 3, 4, 1)

        self.bpscomboBox = QComboBox(self.scrollAreaWidgetContents)
        icon3 = QIcon()
        icon3.addFile(u":/MainWin/ico/20200510-223358.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem(icon3, "")
        self.bpscomboBox.addItem("")
        self.bpscomboBox.setObjectName(u"bpscomboBox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(5)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.bpscomboBox.sizePolicy().hasHeightForWidth())
        self.bpscomboBox.setSizePolicy(sizePolicy7)
        self.bpscomboBox.setFont(font2)
        self.bpscomboBox.setIconSize(QSize(18, 18))

        self.gridLayout.addWidget(self.bpscomboBox, 2, 2, 1, 1)

        self.bpsLabel = QLabel(self.scrollAreaWidgetContents)
        self.bpsLabel.setObjectName(u"bpsLabel")
        sizePolicy5.setHeightForWidth(self.bpsLabel.sizePolicy().hasHeightForWidth())
        self.bpsLabel.setSizePolicy(sizePolicy5)
        self.bpsLabel.setFont(font3)

        self.gridLayout.addWidget(self.bpsLabel, 2, 0, 1, 1)

        self.parityLabel = QLabel(self.scrollAreaWidgetContents)
        self.parityLabel.setObjectName(u"parityLabel")
        sizePolicy5.setHeightForWidth(self.parityLabel.sizePolicy().hasHeightForWidth())
        self.parityLabel.setSizePolicy(sizePolicy5)
        self.parityLabel.setFont(font3)

        self.gridLayout.addWidget(self.parityLabel, 4, 0, 1, 1)

        self.byteSizeComboBox = QComboBox(self.scrollAreaWidgetContents)
        icon4 = QIcon()
        icon4.addFile(u":/MainWin/ico/20200510-223408.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.byteSizeComboBox.addItem(icon4, "")
        self.byteSizeComboBox.addItem(icon4, "")
        self.byteSizeComboBox.addItem(icon4, "")
        self.byteSizeComboBox.addItem(icon4, "")
        self.byteSizeComboBox.setObjectName(u"byteSizeComboBox")
        sizePolicy6.setHeightForWidth(self.byteSizeComboBox.sizePolicy().hasHeightForWidth())
        self.byteSizeComboBox.setSizePolicy(sizePolicy6)
        self.byteSizeComboBox.setFont(font2)
        self.byteSizeComboBox.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.byteSizeComboBox, 3, 2, 1, 1)

        self.stopBitsComboBox = QComboBox(self.scrollAreaWidgetContents)
        icon5 = QIcon()
        icon5.addFile(u":/MainWin/ico/20200510-223417.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.stopBitsComboBox.addItem(icon5, "")
        self.stopBitsComboBox.addItem(icon5, "")
        self.stopBitsComboBox.addItem(icon5, "")
        self.stopBitsComboBox.setObjectName(u"stopBitsComboBox")
        sizePolicy6.setHeightForWidth(self.stopBitsComboBox.sizePolicy().hasHeightForWidth())
        self.stopBitsComboBox.setSizePolicy(sizePolicy6)
        self.stopBitsComboBox.setFont(font2)
        self.stopBitsComboBox.setIconSize(QSize(18, 18))

        self.gridLayout.addWidget(self.stopBitsComboBox, 5, 2, 1, 1)

        self.openSerialButton = QToolButton(self.scrollAreaWidgetContents)
        self.openSerialButton.setObjectName(u"openSerialButton")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(10)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.openSerialButton.sizePolicy().hasHeightForWidth())
        self.openSerialButton.setSizePolicy(sizePolicy8)
        self.openSerialButton.setMinimumSize(QSize(0, 27))
        self.openSerialButton.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/Mainico/ico/\u8fde\u63a5.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.openSerialButton.setIcon(icon6)
        self.openSerialButton.setIconSize(QSize(30, 30))
        self.openSerialButton.setCheckable(False)

        self.gridLayout.addWidget(self.openSerialButton, 2, 4, 4, 1)


        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_7)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        sizePolicy5.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy5)
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.line.setFont(font4)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy9)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_15 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(2, 2, 0, 3)
        self.sendHexCheckBox = QCheckBox(self.frame_8)
        self.sendHexCheckBox.setObjectName(u"sendHexCheckBox")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.sendHexCheckBox.sizePolicy().hasHeightForWidth())
        self.sendHexCheckBox.setSizePolicy(sizePolicy10)
        self.sendHexCheckBox.setMinimumSize(QSize(0, 0))
        self.sendHexCheckBox.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/Mainico/ico/20200510-234010.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.sendHexCheckBox.setIcon(icon7)
        self.sendHexCheckBox.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.sendHexCheckBox)

        self.enterSendCheckBox = QCheckBox(self.frame_8)
        self.enterSendCheckBox.setObjectName(u"enterSendCheckBox")
        sizePolicy10.setHeightForWidth(self.enterSendCheckBox.sizePolicy().hasHeightForWidth())
        self.enterSendCheckBox.setSizePolicy(sizePolicy10)
        self.enterSendCheckBox.setMinimumSize(QSize(0, 0))
        self.enterSendCheckBox.setFont(font2)
        icon8 = QIcon()
        icon8.addFile(u":/Mainico/ico/20200510-234445.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.enterSendCheckBox.setIcon(icon8)
        self.enterSendCheckBox.setIconSize(QSize(20, 20))
        self.enterSendCheckBox.setChecked(True)

        self.horizontalLayout_15.addWidget(self.enterSendCheckBox)


        self.verticalLayout_15.addWidget(self.frame_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 2, 0, 3)
        self.showHexCheckBox = QCheckBox(self.scrollAreaWidgetContents)
        self.showHexCheckBox.setObjectName(u"showHexCheckBox")
        sizePolicy10.setHeightForWidth(self.showHexCheckBox.sizePolicy().hasHeightForWidth())
        self.showHexCheckBox.setSizePolicy(sizePolicy10)
        self.showHexCheckBox.setFont(font2)
        icon9 = QIcon()
        icon9.addFile(u":/Mainico/ico/hex-30 \u5207\u6362\u7cfb\u7edf.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.showHexCheckBox.setIcon(icon9)
        self.showHexCheckBox.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.showHexCheckBox)

        self.showSendMsgBox = QCheckBox(self.scrollAreaWidgetContents)
        self.showSendMsgBox.setObjectName(u"showSendMsgBox")
        sizePolicy10.setHeightForWidth(self.showSendMsgBox.sizePolicy().hasHeightForWidth())
        self.showSendMsgBox.setSizePolicy(sizePolicy10)
        self.showSendMsgBox.setMinimumSize(QSize(0, 0))
        self.showSendMsgBox.setFont(font2)
        icon10 = QIcon()
        icon10.addFile(u":/Mainico/ico/\u4e0a\u4e00\u5c42.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.showSendMsgBox.setIcon(icon10)
        self.showSendMsgBox.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.showSendMsgBox)


        self.verticalLayout_15.addLayout(self.horizontalLayout_12)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        sizePolicy5.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy5)
        self.line_2.setFont(font4)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_15.addWidget(self.line_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(2, -1, -1, -1)
        self.sendTimeRadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.sendTimeRadioButton.setObjectName(u"sendTimeRadioButton")
        sizePolicy10.setHeightForWidth(self.sendTimeRadioButton.sizePolicy().hasHeightForWidth())
        self.sendTimeRadioButton.setSizePolicy(sizePolicy10)
        self.sendTimeRadioButton.setFont(font2)
        icon11 = QIcon()
        icon11.addFile(u":/MainWin/ico/20200510-230202.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.sendTimeRadioButton.setIcon(icon11)
        self.sendTimeRadioButton.setIconSize(QSize(20, 20))
        self.sendTimeRadioButton.setAutoExclusive(False)

        self.horizontalLayout_11.addWidget(self.sendTimeRadioButton)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.sendTimeSpinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.sendTimeSpinBox.setObjectName(u"sendTimeSpinBox")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(2)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.sendTimeSpinBox.sizePolicy().hasHeightForWidth())
        self.sendTimeSpinBox.setSizePolicy(sizePolicy11)
        self.sendTimeSpinBox.setMinimumSize(QSize(0, 0))
        self.sendTimeSpinBox.setFont(font2)
        self.sendTimeSpinBox.setMinimum(1)
        self.sendTimeSpinBox.setMaximum(20000)

        self.horizontalLayout_7.addWidget(self.sendTimeSpinBox)

        self.sendTimeLabel = QLabel(self.scrollAreaWidgetContents)
        self.sendTimeLabel.setObjectName(u"sendTimeLabel")
        sizePolicy10.setHeightForWidth(self.sendTimeLabel.sizePolicy().hasHeightForWidth())
        self.sendTimeLabel.setSizePolicy(sizePolicy10)
        self.sendTimeLabel.setFont(font2)

        self.horizontalLayout_7.addWidget(self.sendTimeLabel)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, -1, -1, -1)
        self.sendLineBreak = QCheckBox(self.scrollAreaWidgetContents)
        self.sendLineBreak.setObjectName(u"sendLineBreak")
        self.sendLineBreak.setFont(font)
        icon12 = QIcon()
        icon12.addFile(u":/MainWin/ico/20200510-223345.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.sendLineBreak.setIcon(icon12)
        self.sendLineBreak.setIconSize(QSize(20, 18))
        self.sendLineBreak.setChecked(True)

        self.horizontalLayout_8.addWidget(self.sendLineBreak)

        self.lineBreakComboBox = QComboBox(self.scrollAreaWidgetContents)
        self.lineBreakComboBox.addItem("")
        self.lineBreakComboBox.addItem("")
        self.lineBreakComboBox.addItem("")
        self.lineBreakComboBox.setObjectName(u"lineBreakComboBox")
        sizePolicy9.setHeightForWidth(self.lineBreakComboBox.sizePolicy().hasHeightForWidth())
        self.lineBreakComboBox.setSizePolicy(sizePolicy9)
        self.lineBreakComboBox.setFont(font2)

        self.horizontalLayout_8.addWidget(self.lineBreakComboBox)


        self.verticalLayout_15.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, -1, -1, -1)
        self.autoConnectCheckBox = QCheckBox(self.scrollAreaWidgetContents)
        self.autoConnectCheckBox.setObjectName(u"autoConnectCheckBox")
        sizePolicy10.setHeightForWidth(self.autoConnectCheckBox.sizePolicy().hasHeightForWidth())
        self.autoConnectCheckBox.setSizePolicy(sizePolicy10)
        self.autoConnectCheckBox.setFont(font2)
        icon13 = QIcon()
        icon13.addFile(u":/MainWin/ico/20200510-230228.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.autoConnectCheckBox.setIcon(icon13)
        self.autoConnectCheckBox.setIconSize(QSize(20, 20))
        self.autoConnectCheckBox.setChecked(True)

        self.horizontalLayout_16.addWidget(self.autoConnectCheckBox)

        self.autoConnectLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.autoConnectLineEdit.setObjectName(u"autoConnectLineEdit")
        sizePolicy6.setHeightForWidth(self.autoConnectLineEdit.sizePolicy().hasHeightForWidth())
        self.autoConnectLineEdit.setSizePolicy(sizePolicy6)
        self.autoConnectLineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.autoConnectLineEdit.setSizeIncrement(QSize(150, 0))
        self.autoConnectLineEdit.setFont(font2)
        self.autoConnectLineEdit.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_16.addWidget(self.autoConnectLineEdit)


        self.verticalLayout_15.addLayout(self.horizontalLayout_16)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_4)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 0, 5, 0)
        self.cutFrameCheckBox = QCheckBox(self.scrollAreaWidgetContents)
        self.cutFrameCheckBox.setObjectName(u"cutFrameCheckBox")
        sizePolicy10.setHeightForWidth(self.cutFrameCheckBox.sizePolicy().hasHeightForWidth())
        self.cutFrameCheckBox.setSizePolicy(sizePolicy10)
        self.cutFrameCheckBox.setFont(font2)
        self.cutFrameCheckBox.setIcon(icon12)
        self.cutFrameCheckBox.setIconSize(QSize(18, 18))
        self.cutFrameCheckBox.setChecked(True)

        self.horizontalLayout_14.addWidget(self.cutFrameCheckBox)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy9.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy9)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(8, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_14)

        self.showLabel1_3 = QLabel(self.frame_14)
        self.showLabel1_3.setObjectName(u"showLabel1_3")
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.showLabel1_3.sizePolicy().hasHeightForWidth())
        self.showLabel1_3.setSizePolicy(sizePolicy12)
        self.showLabel1_3.setMaximumSize(QSize(16777215, 16777215))
        self.showLabel1_3.setFont(font4)

        self.horizontalLayout_35.addWidget(self.showLabel1_3)

        self.frameLCD = QLCDNumber(self.frame_14)
        self.frameLCD.setObjectName(u"frameLCD")
        sizePolicy12.setHeightForWidth(self.frameLCD.sizePolicy().hasHeightForWidth())
        self.frameLCD.setSizePolicy(sizePolicy12)
        self.frameLCD.setFrameShape(QFrame.NoFrame)
        self.frameLCD.setSmallDecimalPoint(False)
        self.frameLCD.setDigitCount(7)
        self.frameLCD.setMode(QLCDNumber.Dec)
        self.frameLCD.setSegmentStyle(QLCDNumber.Flat)
        self.frameLCD.setProperty("value", 0.000000000000000)
        self.frameLCD.setProperty("intValue", 0)

        self.horizontalLayout_35.addWidget(self.frameLCD)


        self.horizontalLayout_14.addWidget(self.frame_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 5, 0)
        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        icon14 = QIcon()
        icon14.addFile(u":/Mainico/ico/20200511-171524.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon14)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(8, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.RTS_RadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.RTS_RadioButton.setObjectName(u"RTS_RadioButton")
        sizePolicy9.setHeightForWidth(self.RTS_RadioButton.sizePolicy().hasHeightForWidth())
        self.RTS_RadioButton.setSizePolicy(sizePolicy9)
        self.RTS_RadioButton.setFont(font2)
        self.RTS_RadioButton.setCursor(QCursor(Qt.ArrowCursor))
        self.RTS_RadioButton.setCheckable(True)
        self.RTS_RadioButton.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.RTS_RadioButton)

        self.DTR_RadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.DTR_RadioButton.setObjectName(u"DTR_RadioButton")
        sizePolicy9.setHeightForWidth(self.DTR_RadioButton.sizePolicy().hasHeightForWidth())
        self.DTR_RadioButton.setSizePolicy(sizePolicy9)
        self.DTR_RadioButton.setFont(font2)
        self.DTR_RadioButton.setCursor(QCursor(Qt.ArrowCursor))
        self.DTR_RadioButton.setCheckable(True)
        self.DTR_RadioButton.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.DTR_RadioButton)

        self.horizontalSpacer_17 = QSpacerItem(8, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_17)


        self.verticalLayout_15.addLayout(self.horizontalLayout_4)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_3)

        self.searchSerialButton = QPushButton(self.scrollAreaWidgetContents)
        self.searchSerialButton.setObjectName(u"searchSerialButton")
        sizePolicy5.setHeightForWidth(self.searchSerialButton.sizePolicy().hasHeightForWidth())
        self.searchSerialButton.setSizePolicy(sizePolicy5)
        self.searchSerialButton.setMinimumSize(QSize(0, 27))
        self.searchSerialButton.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        self.searchSerialButton.setFont(font5)
        icon15 = QIcon()
        icon15.addFile(u":/MainWin/ico/20200511-173453.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.searchSerialButton.setIcon(icon15)
        self.searchSerialButton.setIconSize(QSize(22, 22))

        self.verticalLayout_15.addWidget(self.searchSerialButton)

        self.serialListWidget = QListWidget(self.scrollAreaWidgetContents)
        self.serialListWidget.setObjectName(u"serialListWidget")
        sizePolicy13 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.serialListWidget.sizePolicy().hasHeightForWidth())
        self.serialListWidget.setSizePolicy(sizePolicy13)
        self.serialListWidget.setMinimumSize(QSize(0, 110))
        self.serialListWidget.setMaximumSize(QSize(16777215, 16777215))
        self.serialListWidget.setFont(font2)
        self.serialListWidget.setFrameShape(QFrame.Box)
        self.serialListWidget.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.serialListWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_19.addWidget(self.scrollArea)

        icon16 = QIcon()
        icon16.addFile(u":/Mainico/ico/\u4e32\u53e3.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.mainLeftWidget.addTab(self.tab_2, icon16, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.network_layout = QVBoxLayout(self.tab_3)
        self.network_layout.setObjectName(u"network_layout")
        self.network_layout.setContentsMargins(0, 0, 0, 0)
        icon17 = QIcon()
        icon17.addFile(u":/Mainico/ico/\u7f51\u7edc.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.mainLeftWidget.addTab(self.tab_3, icon17, "")

        self.horizontalLayout_2.addWidget(self.mainLeftWidget)

        self.mainRightFrame = QFrame(self.Main)
        self.mainRightFrame.setObjectName(u"mainRightFrame")
        sizePolicy14 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(9)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.mainRightFrame.sizePolicy().hasHeightForWidth())
        self.mainRightFrame.setSizePolicy(sizePolicy14)
        self.mainRightFrame.setFont(font4)
        self.mainRightFrame.setFrameShape(QFrame.StyledPanel)
        self.mainRightFrame.setFrameShadow(QFrame.Raised)
        self.mainRightFrame.setLineWidth(1)
        self.mainRightFrame.setMidLineWidth(0)
        self.verticalLayout_16 = QVBoxLayout(self.mainRightFrame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.sendFrame = QFrame(self.mainRightFrame)
        self.sendFrame.setObjectName(u"sendFrame")
        self.verticalLayout = QVBoxLayout(self.sendFrame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.cleanMsgButton = QPushButton(self.sendFrame)
        self.cleanMsgButton.setObjectName(u"cleanMsgButton")
        sizePolicy12.setHeightForWidth(self.cleanMsgButton.sizePolicy().hasHeightForWidth())
        self.cleanMsgButton.setSizePolicy(sizePolicy12)
        self.cleanMsgButton.setFont(font4)
        icon18 = QIcon()
        icon18.addFile(u":/MainWin/ico/20200510-223403.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.cleanMsgButton.setIcon(icon18)
        self.cleanMsgButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.cleanMsgButton)

        self.saveMsgButton = QPushButton(self.sendFrame)
        self.saveMsgButton.setObjectName(u"saveMsgButton")
        sizePolicy12.setHeightForWidth(self.saveMsgButton.sizePolicy().hasHeightForWidth())
        self.saveMsgButton.setSizePolicy(sizePolicy12)
        self.saveMsgButton.setMinimumSize(QSize(0, 27))
        self.saveMsgButton.setFont(font4)
        self.saveMsgButton.setStyleSheet(u"")
        icon19 = QIcon()
        icon19.addFile(u":/Mainico/ico/20200510-221417.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.saveMsgButton.setIcon(icon19)
        self.saveMsgButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.saveMsgButton)

        self.showMsgButton = QPushButton(self.sendFrame)
        self.showMsgButton.setObjectName(u"showMsgButton")
        sizePolicy12.setHeightForWidth(self.showMsgButton.sizePolicy().hasHeightForWidth())
        self.showMsgButton.setSizePolicy(sizePolicy12)
        self.showMsgButton.setMaximumSize(QSize(16777215, 16777215))
        self.showMsgButton.setFont(font4)
        icon20 = QIcon()
        icon20.addFile(u":/Mainico/ico/20200512-164645.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon20.addFile(u":/MainWin/ico/20200510-235146.ico", QSize(), QIcon.Normal, QIcon.On)
        self.showMsgButton.setIcon(icon20)
        self.showMsgButton.setIconSize(QSize(20, 20))
        self.showMsgButton.setCheckable(True)
        self.showMsgButton.setChecked(True)

        self.horizontalLayout_5.addWidget(self.showMsgButton)

        self.horizontalSpacer_15 = QSpacerItem(0, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)

        self.frame_12 = QFrame(self.sendFrame)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy15 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy15)
        self.frame_12.setMinimumSize(QSize(300, 0))
        self.frame_12.setFont(font)
        self.frame_12.setFrameShape(QFrame.Box)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.showMsgButton_2 = QPushButton(self.frame_12)
        self.showMsgButton_2.setObjectName(u"showMsgButton_2")
        sizePolicy12.setHeightForWidth(self.showMsgButton_2.sizePolicy().hasHeightForWidth())
        self.showMsgButton_2.setSizePolicy(sizePolicy12)
        self.showMsgButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.showMsgButton_2.setFont(font4)
        self.showMsgButton_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:0px solid #FFFFFF;\n"
"padding:3px;")
        icon21 = QIcon()
        icon21.addFile(u":/Mainico/ico/20200510-221413.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.showMsgButton_2.setIcon(icon21)
        self.showMsgButton_2.setIconSize(QSize(20, 20))
        self.showMsgButton_2.setCheckable(True)
        self.showMsgButton_2.setChecked(False)

        self.horizontalLayout_30.addWidget(self.showMsgButton_2)

        self.sendCountLCD = QLCDNumber(self.frame_12)
        self.sendCountLCD.setObjectName(u"sendCountLCD")
        sizePolicy16 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.sendCountLCD.sizePolicy().hasHeightForWidth())
        self.sendCountLCD.setSizePolicy(sizePolicy16)
        self.sendCountLCD.setMinimumSize(QSize(120, 0))
        self.sendCountLCD.setFrameShape(QFrame.NoFrame)
        self.sendCountLCD.setSmallDecimalPoint(False)
        self.sendCountLCD.setDigitCount(10)
        self.sendCountLCD.setMode(QLCDNumber.Dec)
        self.sendCountLCD.setSegmentStyle(QLCDNumber.Flat)
        self.sendCountLCD.setProperty("value", 0.000000000000000)
        self.sendCountLCD.setProperty("intValue", 0)

        self.horizontalLayout_30.addWidget(self.sendCountLCD)

        self.showMsgButton_3 = QPushButton(self.frame_12)
        self.showMsgButton_3.setObjectName(u"showMsgButton_3")
        sizePolicy12.setHeightForWidth(self.showMsgButton_3.sizePolicy().hasHeightForWidth())
        self.showMsgButton_3.setSizePolicy(sizePolicy12)
        self.showMsgButton_3.setMinimumSize(QSize(0, 17))
        self.showMsgButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.showMsgButton_3.setFont(font4)
        self.showMsgButton_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:0px solid #FFFFFF;\n"
"padding:1px;")
        icon22 = QIcon()
        icon22.addFile(u":/Mainico/ico/\u4e0a \u4f20.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.showMsgButton_3.setIcon(icon22)
        self.showMsgButton_3.setIconSize(QSize(25, 27))
        self.showMsgButton_3.setCheckable(True)
        self.showMsgButton_3.setChecked(False)

        self.horizontalLayout_30.addWidget(self.showMsgButton_3)

        self.receiveCountLCD = QLCDNumber(self.frame_12)
        self.receiveCountLCD.setObjectName(u"receiveCountLCD")
        sizePolicy16.setHeightForWidth(self.receiveCountLCD.sizePolicy().hasHeightForWidth())
        self.receiveCountLCD.setSizePolicy(sizePolicy16)
        self.receiveCountLCD.setMinimumSize(QSize(120, 0))
        self.receiveCountLCD.setFrameShape(QFrame.NoFrame)
        self.receiveCountLCD.setSmallDecimalPoint(False)
        self.receiveCountLCD.setDigitCount(10)
        self.receiveCountLCD.setMode(QLCDNumber.Dec)
        self.receiveCountLCD.setSegmentStyle(QLCDNumber.Flat)
        self.receiveCountLCD.setProperty("value", 0.000000000000000)
        self.receiveCountLCD.setProperty("intValue", 0)

        self.horizontalLayout_30.addWidget(self.receiveCountLCD)

        self.showMsgButton_4 = QPushButton(self.frame_12)
        self.showMsgButton_4.setObjectName(u"showMsgButton_4")
        sizePolicy12.setHeightForWidth(self.showMsgButton_4.sizePolicy().hasHeightForWidth())
        self.showMsgButton_4.setSizePolicy(sizePolicy12)
        self.showMsgButton_4.setMinimumSize(QSize(0, 17))
        self.showMsgButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.showMsgButton_4.setFont(font4)
        self.showMsgButton_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:0px solid #FFFFFF;\n"
"padding:1px;")
        icon23 = QIcon()
        icon23.addFile(u":/Mainico/ico/\u4e0b\u8f7d.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.showMsgButton_4.setIcon(icon23)
        self.showMsgButton_4.setIconSize(QSize(27, 25))
        self.showMsgButton_4.setCheckable(True)
        self.showMsgButton_4.setChecked(False)

        self.horizontalLayout_30.addWidget(self.showMsgButton_4)


        self.horizontalLayout_5.addWidget(self.frame_12)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.receiveBox = QPlainTextEdit(self.sendFrame)
        self.receiveBox.setObjectName(u"receiveBox")
        sizePolicy17 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(7)
        sizePolicy17.setHeightForWidth(self.receiveBox.sizePolicy().hasHeightForWidth())
        self.receiveBox.setSizePolicy(sizePolicy17)
        self.receiveBox.setMinimumSize(QSize(350, 0))
        font6 = QFont()
        font6.setFamilies([u"Consolas"])
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        self.receiveBox.setFont(font6)
        self.receiveBox.setFocusPolicy(Qt.NoFocus)
        self.receiveBox.setFrameShape(QFrame.StyledPanel)
        self.receiveBox.setFrameShadow(QFrame.Plain)
        self.receiveBox.setReadOnly(True)
        self.receiveBox.setBackgroundVisible(False)
        self.receiveBox.setCenterOnScroll(False)

        self.verticalLayout.addWidget(self.receiveBox)


        self.verticalLayout_16.addWidget(self.sendFrame)

        self.toolBox = QToolBox(self.mainRightFrame)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy9.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy9)
        self.toolBox.setMinimumSize(QSize(0, 0))
        self.toolBox.setMaximumSize(QSize(16777215, 16777215))
        self.toolBox.setFont(font4)
        self.toolBox.setCursor(QCursor(Qt.ArrowCursor))
        self.toolBox.setFocusPolicy(Qt.TabFocus)
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setStyleSheet(u"")
        self.toolBox.setFrameShape(QFrame.StyledPanel)
        self.toolBox.setFrameShadow(QFrame.Raised)
        self.toolBox.setLineWidth(1)
        self.toolBox.setMidLineWidth(0)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 733, 133))
        sizePolicy4.setHeightForWidth(self.page_3.sizePolicy().hasHeightForWidth())
        self.page_3.setSizePolicy(sizePolicy4)
        self.page_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.page_3)
        self.frame.setObjectName(u"frame")
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setMinimumSize(QSize(0, 123))
        self.sendLayout = QHBoxLayout(self.frame)
        self.sendLayout.setSpacing(5)
        self.sendLayout.setObjectName(u"sendLayout")
        self.sendLayout.setContentsMargins(0, 0, 0, 0)
        self.sendBox = QPlainTextEdit(self.frame)
        self.sendBox.setObjectName(u"sendBox")
        sizePolicy18 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy18.setHorizontalStretch(10)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.sendBox.sizePolicy().hasHeightForWidth())
        self.sendBox.setSizePolicy(sizePolicy18)
        self.sendBox.setMinimumSize(QSize(100, 0))
        self.sendBox.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Consolas"])
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        self.sendBox.setFont(font7)
        self.sendBox.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.sendBox.setStyleSheet(u"")
        self.sendBox.setFrameShape(QFrame.Box)
        self.sendBox.setFrameShadow(QFrame.Raised)
        self.sendBox.setBackgroundVisible(False)

        self.sendLayout.addWidget(self.sendBox)

        self.sendButton = QPushButton(self.frame)
        self.sendButton.setObjectName(u"sendButton")
        sizePolicy19 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy19.setHorizontalStretch(1)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy19)
        self.sendButton.setMinimumSize(QSize(100, 27))
        self.sendButton.setFont(font4)
        icon24 = QIcon()
        icon24.addFile(u":/Mainico/ico/20200510-221424.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.sendButton.setIcon(icon24)
        self.sendButton.setIconSize(QSize(45, 45))
        self.sendButton.setAutoRepeat(True)

        self.sendLayout.addWidget(self.sendButton)


        self.verticalLayout_6.addWidget(self.frame)

        icon25 = QIcon()
        icon25.addFile(u":/MainWin/ico/20200510-230224.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_3, icon25, u"\u5355\u6761\u53d1\u9001")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 733, 202))
        self.horizontalLayout_17 = QHBoxLayout(self.page_4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.page_4)
        self.widget.setObjectName(u"widget")
        sizePolicy20 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy20.setHorizontalStretch(0)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy20)
        self.widget.setMinimumSize(QSize(0, 192))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_multi_send = QScrollArea(self.widget)
        self.scrollArea_multi_send.setObjectName(u"scrollArea_multi_send")
        sizePolicy21 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy21.setHorizontalStretch(0)
        sizePolicy21.setVerticalStretch(0)
        sizePolicy21.setHeightForWidth(self.scrollArea_multi_send.sizePolicy().hasHeightForWidth())
        self.scrollArea_multi_send.setSizePolicy(sizePolicy21)
        self.scrollArea_multi_send.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_multi_send.setSizeIncrement(QSize(0, 190))
        self.scrollArea_multi_send.setBaseSize(QSize(0, 192))
        self.scrollArea_multi_send.setFont(font4)
        self.scrollArea_multi_send.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_multi_send.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_multi_send.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 723, 192))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 7, 5, 5)
        self.multi_send_form = QFrame(self.scrollAreaWidgetContents_2)
        self.multi_send_form.setObjectName(u"multi_send_form")
        sizePolicy22 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy22.setHorizontalStretch(0)
        sizePolicy22.setVerticalStretch(0)
        sizePolicy22.setHeightForWidth(self.multi_send_form.sizePolicy().hasHeightForWidth())
        self.multi_send_form.setSizePolicy(sizePolicy22)
        self.verticalLayout_23 = QVBoxLayout(self.multi_send_form)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.multi_send_layout = QVBoxLayout()
        self.multi_send_layout.setObjectName(u"multi_send_layout")

        self.verticalLayout_23.addLayout(self.multi_send_layout)


        self.verticalLayout_8.addWidget(self.multi_send_form)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 35))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_19)

        self.pushButton_5 = QPushButton(self.frame_16)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font8 = QFont()
        font8.setPointSize(13)
        self.pushButton_5.setFont(font8)

        self.horizontalLayout_41.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_16)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font8)

        self.horizontalLayout_41.addWidget(self.pushButton_6)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.scrollArea_multi_send.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_multi_send)


        self.horizontalLayout_17.addWidget(self.widget)

        icon26 = QIcon()
        icon26.addFile(u":/MainWin/ico/20200510-230208.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_4, icon26, u"\u591a\u6761\u53d1\u9001")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 733, 77))
        sizePolicy9.setHeightForWidth(self.page_7.sizePolicy().hasHeightForWidth())
        self.page_7.setSizePolicy(sizePolicy9)
        self.page_7.setMinimumSize(QSize(0, 0))
        self.page_7.setMaximumSize(QSize(16777215, 16777215))
        self.page_7.setSizeIncrement(QSize(0, 0))
        self.page_7.setBaseSize(QSize(0, 0))
        self.verticalLayout_18 = QVBoxLayout(self.page_7)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.frame_7 = QFrame(self.page_7)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy9.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy9)
        self.frame_7.setFont(font4)
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(3, 0, 0, 0)
        self.selectLabel_2 = QLabel(self.frame_7)
        self.selectLabel_2.setObjectName(u"selectLabel_2")
        sizePolicy12.setHeightForWidth(self.selectLabel_2.sizePolicy().hasHeightForWidth())
        self.selectLabel_2.setSizePolicy(sizePolicy12)
        font9 = QFont()
        font9.setPointSize(14)
        font9.setBold(False)
        font9.setItalic(False)
        font9.setUnderline(False)
        font9.setStrikeOut(False)
        self.selectLabel_2.setFont(font9)
        self.selectLabel_2.setLineWidth(1)

        self.horizontalLayout_27.addWidget(self.selectLabel_2)

        self.cmdSendLabel = QLabel(self.frame_7)
        self.cmdSendLabel.setObjectName(u"cmdSendLabel")
        sizePolicy10.setHeightForWidth(self.cmdSendLabel.sizePolicy().hasHeightForWidth())
        self.cmdSendLabel.setSizePolicy(sizePolicy10)
        self.cmdSendLabel.setFont(font4)
        self.cmdSendLabel.setLineWidth(1)

        self.horizontalLayout_27.addWidget(self.cmdSendLabel)


        self.verticalLayout_18.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.page_7)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy9.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy9)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_26.setSpacing(3)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.cmdToolButton = QToolButton(self.frame_6)
        self.cmdToolButton.setObjectName(u"cmdToolButton")
        self.cmdToolButton.setMinimumSize(QSize(0, 27))
        self.cmdToolButton.setFont(font4)
        icon27 = QIcon()
        icon27.addFile(u":/Mainico/ico/\u4e0b\u4e00.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.cmdToolButton.setIcon(icon27)
        self.cmdToolButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_26.addWidget(self.cmdToolButton)

        self.cmdSendLine = QLineEdit(self.frame_6)
        self.cmdSendLine.setObjectName(u"cmdSendLine")
        sizePolicy23 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy23.setHorizontalStretch(0)
        sizePolicy23.setVerticalStretch(0)
        sizePolicy23.setHeightForWidth(self.cmdSendLine.sizePolicy().hasHeightForWidth())
        self.cmdSendLine.setSizePolicy(sizePolicy23)
        font10 = QFont()
        font10.setFamilies([u"Consolas"])
        font10.setPointSize(13)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setUnderline(False)
        font10.setStrikeOut(False)
        self.cmdSendLine.setFont(font10)

        self.horizontalLayout_26.addWidget(self.cmdSendLine)


        self.verticalLayout_18.addWidget(self.frame_6)

        icon28 = QIcon()
        icon28.addFile(u":/Mainico/ico/\u547d\u4ee4.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_7, icon28, u"\u6a21\u62df\u7ec8\u7aef")

        self.verticalLayout_16.addWidget(self.toolBox)


        self.horizontalLayout_2.addWidget(self.mainRightFrame)

        icon29 = QIcon()
        icon29.addFile(u":/MainWin/ico/20200511-103837.ico", QSize(), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Main, icon29, "")
        self.Draw = QWidget()
        self.Draw.setObjectName(u"Draw")
        self.draw_layout = QVBoxLayout(self.Draw)
        self.draw_layout.setObjectName(u"draw_layout")
        self.draw_layout.setContentsMargins(8, 8, 8, 8)
        icon30 = QIcon()
        icon30.addFile(u":/Mainico/ico/20200511-103831.ico", QSize(), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Draw, icon30, "")
        self.Setting = QWidget()
        self.Setting.setObjectName(u"Setting")
        self.verticalLayout_14 = QVBoxLayout(self.Setting)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame1 = QFrame(self.Setting)
        self.frame1.setObjectName(u"frame1")
        sizePolicy9.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy9)
        self.frame1.setFrameShape(QFrame.Box)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_7 = QLabel(self.frame1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.gridLayout_9.addWidget(self.label_7, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame1)
        self.label_6.setObjectName(u"label_6")
        sizePolicy15.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy15)
        self.label_6.setFont(font4)

        self.horizontalLayout.addWidget(self.label_6)

        self.fontComboBox = QFontComboBox(self.frame1)
        self.fontComboBox.setObjectName(u"fontComboBox")
        sizePolicy12.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy12)
        self.fontComboBox.setFont(font2)

        self.horizontalLayout.addWidget(self.fontComboBox)

        self.label_11 = QLabel(self.frame1)
        self.label_11.setObjectName(u"label_11")
        sizePolicy15.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy15)
        self.label_11.setFont(font4)

        self.horizontalLayout.addWidget(self.label_11)

        self.formSpinBox = QSpinBox(self.frame1)
        self.formSpinBox.setObjectName(u"formSpinBox")
        self.formSpinBox.setMinimumSize(QSize(80, 0))
        self.formSpinBox.setFont(font4)
        self.formSpinBox.setMinimum(6)
        self.formSpinBox.setMaximum(72)

        self.horizontalLayout.addWidget(self.formSpinBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)

        self.decodeLabel = QLabel(self.frame1)
        self.decodeLabel.setObjectName(u"decodeLabel")
        sizePolicy15.setHeightForWidth(self.decodeLabel.sizePolicy().hasHeightForWidth())
        self.decodeLabel.setSizePolicy(sizePolicy15)
        self.decodeLabel.setFont(font4)

        self.horizontalLayout.addWidget(self.decodeLabel)

        self.decodeComboBox = QComboBox(self.frame1)
        self.decodeComboBox.addItem("")
        self.decodeComboBox.addItem("")
        self.decodeComboBox.addItem("")
        self.decodeComboBox.addItem("")
        self.decodeComboBox.addItem("")
        self.decodeComboBox.setObjectName(u"decodeComboBox")
        self.decodeComboBox.setFont(font2)

        self.horizontalLayout.addWidget(self.decodeComboBox)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.gridLayout_9.addLayout(self.horizontalLayout, 2, 0, 1, 5)

        self.PathButton = QToolButton(self.frame1)
        self.PathButton.setObjectName(u"PathButton")
        self.PathButton.setFont(font4)

        self.gridLayout_9.addWidget(self.PathButton, 4, 4, 1, 1)

        self.pathLabel = QLabel(self.frame1)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setFont(font4)
        self.pathLabel.setFrameShape(QFrame.Box)
        self.pathLabel.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.pathLabel, 4, 0, 1, 4)

        self.openPathButton = QPushButton(self.frame1)
        self.openPathButton.setObjectName(u"openPathButton")
        sizePolicy24 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy24.setHorizontalStretch(4)
        sizePolicy24.setVerticalStretch(0)
        sizePolicy24.setHeightForWidth(self.openPathButton.sizePolicy().hasHeightForWidth())
        self.openPathButton.setSizePolicy(sizePolicy24)
        self.openPathButton.setMinimumSize(QSize(0, 27))
        self.openPathButton.setFont(font5)
        icon31 = QIcon()
        icon31.addFile(u":/setting/ico/\u8bbe\u7f6e/20200517-232143.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.openPathButton.setIcon(icon31)
        self.openPathButton.setIconSize(QSize(28, 28))

        self.gridLayout_9.addWidget(self.openPathButton, 5, 0, 1, 5)

        self.label_10 = QLabel(self.frame1)
        self.label_10.setObjectName(u"label_10")
        font11 = QFont()
        font11.setPointSize(18)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setUnderline(False)
        font11.setStrikeOut(False)
        self.label_10.setFont(font11)

        self.gridLayout_9.addWidget(self.label_10, 0, 0, 1, 3)

        self.horizontalSpacer_9 = QSpacerItem(612, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_9, 3, 2, 1, 3)


        self.verticalLayout_14.addWidget(self.frame1)

        self.frame2 = QFrame(self.Setting)
        self.frame2.setObjectName(u"frame2")
        sizePolicy9.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy9)
        self.frame2.setFrameShape(QFrame.Box)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.showLegend = QCheckBox(self.frame2)
        self.showLegend.setObjectName(u"showLegend")
        sizePolicy25 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy25.setHorizontalStretch(0)
        sizePolicy25.setVerticalStretch(0)
        sizePolicy25.setHeightForWidth(self.showLegend.sizePolicy().hasHeightForWidth())
        self.showLegend.setSizePolicy(sizePolicy25)
        self.showLegend.setFont(font4)
        icon32 = QIcon()
        icon32.addFile(u":/setting/ico/\u8bbe\u7f6e/20200518-125030.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.showLegend.setIcon(icon32)
        self.showLegend.setIconSize(QSize(22, 22))
        self.showLegend.setChecked(True)

        self.gridLayout_12.addWidget(self.showLegend, 1, 4, 1, 1)

        self.mousePosBox = QCheckBox(self.frame2)
        self.mousePosBox.setObjectName(u"mousePosBox")
        sizePolicy25.setHeightForWidth(self.mousePosBox.sizePolicy().hasHeightForWidth())
        self.mousePosBox.setSizePolicy(sizePolicy25)
        self.mousePosBox.setFont(font4)
        icon33 = QIcon()
        icon33.addFile(u":/setting/ico/\u8bbe\u7f6e/20200517-232202.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.mousePosBox.setIcon(icon33)
        self.mousePosBox.setIconSize(QSize(22, 22))
        self.mousePosBox.setChecked(True)

        self.gridLayout_12.addWidget(self.mousePosBox, 2, 4, 1, 1)

        self.pointShowBox = QCheckBox(self.frame2)
        self.pointShowBox.setObjectName(u"pointShowBox")
        sizePolicy25.setHeightForWidth(self.pointShowBox.sizePolicy().hasHeightForWidth())
        self.pointShowBox.setSizePolicy(sizePolicy25)
        self.pointShowBox.setFont(font4)
        icon34 = QIcon()
        icon34.addFile(u":/setting/ico/\u8bbe\u7f6e/20200517-232154.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pointShowBox.setIcon(icon34)
        self.pointShowBox.setIconSize(QSize(22, 22))
        self.pointShowBox.setChecked(True)

        self.gridLayout_12.addWidget(self.pointShowBox, 2, 0, 1, 1)

        self.label_9 = QLabel(self.frame2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font11)

        self.gridLayout_12.addWidget(self.label_9, 0, 0, 1, 1)

        self.gridBox = QCheckBox(self.frame2)
        self.gridBox.setObjectName(u"gridBox")
        sizePolicy25.setHeightForWidth(self.gridBox.sizePolicy().hasHeightForWidth())
        self.gridBox.setSizePolicy(sizePolicy25)
        self.gridBox.setFont(font4)
        icon35 = QIcon()
        icon35.addFile(u":/setting/ico/\u8bbe\u7f6e/20200517-232210.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.gridBox.setIcon(icon35)
        self.gridBox.setIconSize(QSize(22, 22))
        self.gridBox.setChecked(True)

        self.gridLayout_12.addWidget(self.gridBox, 1, 3, 1, 1)

        self.antialiasCheckBox = QCheckBox(self.frame2)
        self.antialiasCheckBox.setObjectName(u"antialiasCheckBox")
        sizePolicy25.setHeightForWidth(self.antialiasCheckBox.sizePolicy().hasHeightForWidth())
        self.antialiasCheckBox.setSizePolicy(sizePolicy25)
        self.antialiasCheckBox.setFont(font4)
        icon36 = QIcon()
        icon36.addFile(u":/setting/ico/\u8bbe\u7f6e/20200517-232207.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.antialiasCheckBox.setIcon(icon36)
        self.antialiasCheckBox.setIconSize(QSize(22, 22))
        self.antialiasCheckBox.setChecked(True)

        self.gridLayout_12.addWidget(self.antialiasCheckBox, 2, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(418, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_7, 0, 1, 1, 6)

        self.showXYBox = QCheckBox(self.frame2)
        self.showXYBox.setObjectName(u"showXYBox")
        sizePolicy25.setHeightForWidth(self.showXYBox.sizePolicy().hasHeightForWidth())
        self.showXYBox.setSizePolicy(sizePolicy25)
        self.showXYBox.setFont(font4)
        icon37 = QIcon()
        icon37.addFile(u":/setting/ico/\u8bbe\u7f6e/20200517-232213.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.showXYBox.setIcon(icon37)
        self.showXYBox.setIconSize(QSize(22, 22))
        self.showXYBox.setChecked(True)

        self.gridLayout_12.addWidget(self.showXYBox, 1, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.frame2)

        self.frame_2 = QFrame(self.Setting)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy9.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy9)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.versionLabel = QLabel(self.frame_2)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setFont(font9)
        self.versionLabel.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_11.addWidget(self.versionLabel, 2, 5, 1, 1)

        self.updateLabel = QLabel(self.frame_2)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setFont(font11)

        self.gridLayout_11.addWidget(self.updateLabel, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(927, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_5, 0, 1, 1, 5)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(1)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.updateButton = QPushButton(self.frame_5)
        self.updateButton.setObjectName(u"updateButton")
        sizePolicy26 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy26.setHorizontalStretch(1)
        sizePolicy26.setVerticalStretch(0)
        sizePolicy26.setHeightForWidth(self.updateButton.sizePolicy().hasHeightForWidth())
        self.updateButton.setSizePolicy(sizePolicy26)
        self.updateButton.setMinimumSize(QSize(0, 27))
        self.updateButton.setFont(font2)
        icon38 = QIcon()
        icon38.addFile(u":/MainWin/ico/20200510-230212.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.updateButton.setIcon(icon38)
        self.updateButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_25.addWidget(self.updateButton)

        self.fastUpdateButton = QPushButton(self.frame_5)
        self.fastUpdateButton.setObjectName(u"fastUpdateButton")
        sizePolicy27 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy27.setHorizontalStretch(5)
        sizePolicy27.setVerticalStretch(0)
        sizePolicy27.setHeightForWidth(self.fastUpdateButton.sizePolicy().hasHeightForWidth())
        self.fastUpdateButton.setSizePolicy(sizePolicy27)
        self.fastUpdateButton.setMinimumSize(QSize(0, 27))
        self.fastUpdateButton.setFont(font2)
        self.fastUpdateButton.setIcon(icon38)
        self.fastUpdateButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_25.addWidget(self.fastUpdateButton)

        self.updateCheckBox = QCheckBox(self.frame_5)
        self.updateCheckBox.setObjectName(u"updateCheckBox")
        sizePolicy25.setHeightForWidth(self.updateCheckBox.sizePolicy().hasHeightForWidth())
        self.updateCheckBox.setSizePolicy(sizePolicy25)
        self.updateCheckBox.setFont(font2)
        icon39 = QIcon()
        icon39.addFile(u":/setting/ico/\u8bbe\u7f6e/20200517-232159.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.updateCheckBox.setIcon(icon39)
        self.updateCheckBox.setIconSize(QSize(25, 25))
        self.updateCheckBox.setChecked(True)

        self.horizontalLayout_25.addWidget(self.updateCheckBox)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy28 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy28.setHorizontalStretch(0)
        sizePolicy28.setVerticalStretch(0)
        sizePolicy28.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy28)
        self.label_8.setFont(font2)
        self.label_8.setFrameShape(QFrame.NoFrame)
        self.label_8.setFrameShadow(QFrame.Plain)
        self.label_8.setOpenExternalLinks(True)

        self.horizontalLayout_25.addWidget(self.label_8)


        self.gridLayout_11.addWidget(self.frame_5, 2, 0, 1, 2)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(100)

        self.gridLayout_11.addWidget(self.progressBar, 1, 0, 1, 6)


        self.verticalLayout_14.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)

        icon40 = QIcon()
        icon40.addFile(u":/Mainico/ico/20200511-103826.ico", QSize(), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Setting, icon40, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.toolBox_2 = QToolBox(self.tab)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.toolBox_2.setFont(font4)
        self.toolBox_2.setStyleSheet(u"")
        self.toolBox_2.setFrameShape(QFrame.Box)
        self.toolBox_2.setFrameShadow(QFrame.Raised)
        self.toolBox_2.setLineWidth(1)
        self.toolBox_2.setMidLineWidth(0)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 120, 120))
        self.verticalLayout_11 = QVBoxLayout(self.page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.textBrowser = QTextBrowser(self.page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"")
        self.textBrowser.setFrameShadow(QFrame.Raised)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setTabChangesFocus(False)
        self.textBrowser.setUndoRedoEnabled(False)

        self.verticalLayout_11.addWidget(self.textBrowser)

        icon41 = QIcon()
        icon41.addFile(u":/Mainico/ico/20200511-105434.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_2.addItem(self.page, icon41, u"\u4e3b\u9875")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 120, 120))
        self.verticalLayout_12 = QVBoxLayout(self.page_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.textBrowser_2 = QTextBrowser(self.page_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.textBrowser_2)

        icon42 = QIcon()
        icon42.addFile(u":/Mainico/ico/20200511-105434.ico", QSize(), QIcon.Normal, QIcon.On)
        self.toolBox_2.addItem(self.page_2, icon42, u"\u7ed8\u56fe")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 120, 120))
        self.verticalLayout_13 = QVBoxLayout(self.page_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.textBrowser_3 = QTextBrowser(self.page_6)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.verticalLayout_13.addWidget(self.textBrowser_3)

        icon43 = QIcon()
        icon43.addFile(u":/Mainico/ico/20200511-103820.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_2.addItem(self.page_6, icon43, u"\u8bbe\u7f6e")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 120, 120))
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.plainTextEdit = QPlainTextEdit(self.page_5)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font2)
        self.plainTextEdit.setStyleSheet(u"")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)

        self.verticalLayout_10.addWidget(self.plainTextEdit)

        icon44 = QIcon()
        icon44.addFile(u":/Mainico/ico/20200511-105454.ico", QSize(), QIcon.Normal, QIcon.On)
        self.toolBox_2.addItem(self.page_5, icon44, u"\u66f4\u65b0")

        self.verticalLayout_9.addWidget(self.toolBox_2)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_9.addWidget(self.label)

        icon45 = QIcon()
        icon45.addFile(u":/Mainico/ico/20200511-105510.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon45, "")

        self.verticalLayout_17.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setFont(font)
        MainWindow.setStatusBar(self.statusBar)
#if QT_CONFIG(shortcut)
        self.byteSizeLabel.setBuddy(self.byteSizeComboBox)
        self.stopBitsLabel.setBuddy(self.stopBitsComboBox)
        self.bpsLabel.setBuddy(self.bpscomboBox)
        self.parityLabel.setBuddy(self.parityComboBox)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        self.bpscomboBox.currentTextChanged.connect(MainWindow.bpsChanged)
        self.byteSizeComboBox.currentTextChanged.connect(MainWindow.byteSizeChanged)
        self.parityComboBox.currentTextChanged.connect(MainWindow.parityChanged)
        self.stopBitsComboBox.currentTextChanged.connect(MainWindow.stopBitsChanged)
        self.sendHexCheckBox.clicked.connect(MainWindow.setSendHex)
        self.enterSendCheckBox.clicked.connect(MainWindow.setEnterSend)
        self.showHexCheckBox.clicked.connect(MainWindow.setShowHex)
        self.showSendMsgBox.clicked.connect(MainWindow.setShowSendMsg)
        self.DTR_RadioButton.clicked.connect(MainWindow.setDTR)
        self.RTS_RadioButton.clicked.connect(MainWindow.setRTS)
        self.sendTimeSpinBox.valueChanged.connect(MainWindow.autoSendTimeChanged)
        self.sendLineBreak.clicked.connect(MainWindow.setLineBreak)
        self.lineBreakComboBox.currentIndexChanged.connect(MainWindow.LineBreakChanged)
        self.searchSerialButton.clicked.connect(MainWindow.searchPort)
        self.serialListWidget.itemDoubleClicked.connect(MainWindow.portListDoubleClicked)
        self.autoConnectCheckBox.clicked.connect(MainWindow.setAutoConnect)
        self.autoConnectLineEdit.textChanged.connect(MainWindow.autoConnectChanged)
        self.pushButton_2.clicked.connect(MainWindow.streamFlameSet)
        self.cutFrameCheckBox.clicked.connect(MainWindow.setAutoCut)
        self.sendTimeRadioButton.clicked.connect(MainWindow.setAutoSend)
        self.serialListWidget.itemClicked.connect(MainWindow.portListClicked)
        self.openSerialButton.clicked.connect(MainWindow.connectSerial)
        self.cleanMsgButton.clicked.connect(MainWindow.clearRecvBox)
        self.saveMsgButton.clicked.connect(MainWindow.saveRecvBox)
        self.showMsgButton.clicked.connect(MainWindow.isShowMsg)
        self.sendBox.textChanged.connect(MainWindow.sendBoxTextChange)
        self.sendButton.clicked.connect(MainWindow.sendMsg)
        self.pushButton_5.clicked.connect(MainWindow.add_multi_send)
        self.pushButton_6.clicked.connect(MainWindow.delete_multi_send)
        self.cmdToolButton.clicked.connect(MainWindow.openSetCmdWin)
        self.tabWidget.currentChanged.connect(MainWindow.tabChanged)
        self.mainLeftWidget.currentChanged.connect(MainWindow.changeMode)
        self.decodeComboBox.currentTextChanged.connect(MainWindow.setDecode)
        self.PathButton.clicked.connect(MainWindow.setDataDir)
        self.openPathButton.clicked.connect(MainWindow.openDataDir)

        self.tabWidget.setCurrentIndex(0)
        self.mainLeftWidget.setCurrentIndex(0)
        self.bpscomboBox.setCurrentIndex(7)
        self.toolBox.setCurrentIndex(2)
        self.toolBox.layout().setSpacing(0)
        self.toolBox_2.setCurrentIndex(0)
        self.toolBox_2.layout().setSpacing(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5c0f\u667a\u4e32\u53e3\u8c03\u8bd5\u5668", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.byteSizeLabel.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4f4d", None))
        self.stopBitsLabel.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4f4d", None))
        self.parityComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.parityComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Even", None))
        self.parityComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Mark", None))
        self.parityComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Odd", None))
        self.parityComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Names", None))
        self.parityComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Space", None))

#if QT_CONFIG(tooltip)
        self.parityComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c\u4f4d", None))
#endif // QT_CONFIG(tooltip)
        self.bpscomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1800", None))
        self.bpscomboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2400", None))
        self.bpscomboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"4800", None))
        self.bpscomboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"9600", None))
        self.bpscomboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"19200", None))
        self.bpscomboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"38400", None))
        self.bpscomboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"57600", None))
        self.bpscomboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"115200", None))
        self.bpscomboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"230400", None))
        self.bpscomboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"460800", None))
        self.bpscomboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"921600", None))
        self.bpscomboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"<\u81ea\u5b9a\u4e49>", None))

#if QT_CONFIG(tooltip)
        self.bpscomboBox.setToolTip(QCoreApplication.translate("MainWindow", u"115200\u4ee5\u4e0a\u9700\u8bbe\u5907\u652f\u6301", None))
#endif // QT_CONFIG(tooltip)
        self.bpscomboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"115200", None))
        self.bpsLabel.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
        self.parityLabel.setText(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c\u4f4d", None))
        self.byteSizeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.byteSizeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"6", None))
        self.byteSizeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"7", None))
        self.byteSizeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"8", None))

#if QT_CONFIG(tooltip)
        self.byteSizeComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4f4d", None))
#endif // QT_CONFIG(tooltip)
        self.byteSizeComboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"5", None))
        self.stopBitsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.stopBitsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1.5", None))
        self.stopBitsComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

#if QT_CONFIG(tooltip)
        self.stopBitsComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4f4d", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.openSerialButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u8fde\u63a5CH340", None))
#endif // QT_CONFIG(tooltip)
        self.openSerialButton.setText("")
#if QT_CONFIG(tooltip)
        self.sendHexCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5341\u516d\u8fdb\u5236\u6570\u636e", None))
#endif // QT_CONFIG(tooltip)
        self.sendHexCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001HEX", None))
#if QT_CONFIG(tooltip)
        self.enterSendCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ec5\u5bf9\u5355\u6761\u53d1\u9001\u6709\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.enterSendCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u56de\u8f66\u53d1\u9001", None))
#if QT_CONFIG(tooltip)
        self.showHexCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5341\u516d\u8fdb\u5236\u6570\u636e", None))
#endif // QT_CONFIG(tooltip)
        self.showHexCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793aHEX", None))
#if QT_CONFIG(tooltip)
        self.showSendMsgBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ec5\u5bf9\u5355\u6761\u53d1\u9001\u6709\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.showSendMsgBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u53d1\u9001", None))
        self.sendTimeRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u65f6\u53d1\u9001", None))
#if QT_CONFIG(tooltip)
        self.sendTimeSpinBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u6700\u592720000ms", None))
#endif // QT_CONFIG(tooltip)
        self.sendTimeLabel.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.sendLineBreak.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6362\u884c", None))
#if QT_CONFIG(shortcut)
        self.sendLineBreak.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.lineBreakComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\\r\\n (CRLF)", None))
        self.lineBreakComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\\r (CR)", None))
        self.lineBreakComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\\n (LF)", None))

#if QT_CONFIG(tooltip)
        self.autoConnectCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u65f6\u81ea\u52a8\u67e5\u627e\u8bbe\u5907", None))
#endif // QT_CONFIG(tooltip)
        self.autoConnectCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8fde\u63a5", None))
#if QT_CONFIG(tooltip)
        self.autoConnectLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u5173\u952e\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.autoConnectLineEdit.setText(QCoreApplication.translate("MainWindow", u"CH340", None))
#if QT_CONFIG(tooltip)
        self.cutFrameCheckBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.cutFrameCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u65ad\u5e27", None))
        self.showLabel1_3.setText(QCoreApplication.translate("MainWindow", u"\u5e27\u901f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" \u6d41\u4e0e\u5e27\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.RTS_RadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"RTS/CTS\u6d41\u63a7\u5f00\u5173", None))
#endif // QT_CONFIG(tooltip)
        self.RTS_RadioButton.setText(QCoreApplication.translate("MainWindow", u"RTS", None))
#if QT_CONFIG(tooltip)
        self.DTR_RadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u786c\u4ef6DSR/DTR\u6d41\u63a7\u5f00\u5173", None))
#endif // QT_CONFIG(tooltip)
        self.DTR_RadioButton.setText(QCoreApplication.translate("MainWindow", u"DTR", None))
#if QT_CONFIG(tooltip)
        self.searchSerialButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u5217\u51fa\u53ef\u7528\u4e32\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.searchSerialButton.setText(QCoreApplication.translate("MainWindow", u" \u641c\u7d22\u4e32\u53e3", None))
        self.mainLeftWidget.setTabText(self.mainLeftWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u4e32\u53e3", None))
        self.mainLeftWidget.setTabText(self.mainLeftWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u7f51\u7edc", None))
#if QT_CONFIG(tooltip)
        self.cleanMsgButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u4fe1\u606f\u7f13\u5b58", None))
#endif // QT_CONFIG(tooltip)
        self.cleanMsgButton.setText("")
#if QT_CONFIG(tooltip)
        self.saveMsgButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4fe1\u606f\n"
"Alt + S", None))
#endif // QT_CONFIG(tooltip)
        self.saveMsgButton.setText("")
#if QT_CONFIG(tooltip)
        self.showMsgButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u663e\u793a\u4fe1\u606f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.showMsgButton.setText("")
#if QT_CONFIG(tooltip)
        self.showMsgButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u663e\u793a\u4fe1\u606f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.showMsgButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.showMsgButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u663e\u793a\u4fe1\u606f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.showMsgButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.showMsgButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u663e\u793a\u4fe1\u606f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.showMsgButton_4.setText("")
        self.receiveBox.setDocumentTitle("")
        self.receiveBox.setPlainText("")
#if QT_CONFIG(tooltip)
        self.toolBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.sendBox.setPlainText("")
#if QT_CONFIG(tooltip)
        self.sendButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
#endif // QT_CONFIG(tooltip)
        self.sendButton.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u5355\u6761\u53d1\u9001", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"\u591a\u6761\u53d1\u9001", None))
        self.selectLabel_2.setText(QCoreApplication.translate("MainWindow", u"@ ", None))
        self.cmdSendLabel.setText("")
#if QT_CONFIG(tooltip)
        self.cmdToolButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u6307\u4ee4\u96c6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.cmdToolButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u6307\u4ee4\u96c6", None))
#endif // QT_CONFIG(whatsthis)
        self.cmdToolButton.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"\u6a21\u62df\u7ec8\u7aef", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main), QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Draw), QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4fdd\u5b58\u8def\u5f84", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5b57\u4f53", None))
#if QT_CONFIG(tooltip)
        self.fontComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5168\u5c40\u5b57\u4f53", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f", None))
#if QT_CONFIG(tooltip)
        self.formSpinBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5168\u5c40\u5b57\u4f53\u5927\u5c0f", None))
#endif // QT_CONFIG(tooltip)
        self.decodeLabel.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u7f16\u7801", None))
        self.decodeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"UTF-8", None))
        self.decodeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"GBK", None))
        self.decodeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"BIG5", None))
        self.decodeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.decodeComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"GB2312", None))

#if QT_CONFIG(tooltip)
        self.PathButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u8def\u5f84", None))
#endif // QT_CONFIG(tooltip)
        self.PathButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pathLabel.setText("")
#if QT_CONFIG(tooltip)
        self.openPathButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6570\u636e\u5b58\u653e\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.openPathButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c40\u8bbe\u7f6e", None))
        self.showLegend.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u56fe\u4f8b   ", None))
        self.mousePosBox.setText(QCoreApplication.translate("MainWindow", u"\u6807\u8bc6\u9f20\u6807\u4f4d\u7f6e", None))
        self.pointShowBox.setText(QCoreApplication.translate("MainWindow", u"\u9876\u70b9\u6807\u6ce8", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe\u8bbe\u7f6e\uff08\u6682\u4e0d\u53ef\u7528\uff09", None))
        self.gridBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u6805\u683c", None))
        self.antialiasCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u6297\u952f\u9f7f  ", None))
#if QT_CONFIG(tooltip)
        self.showXYBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u5e95\u90e8\u5750\u6807\u663e\u793a", None))
#endif // QT_CONFIG(tooltip)
        self.showXYBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5750\u6807", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"@Version Beta-1.2.0", None))
        self.updateLabel.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c\u66f4\u65b0\uff08\u6682\u4e0d\u53ef\u7528\uff09", None))
#if QT_CONFIG(tooltip)
        self.updateButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u66f4\u65b0", None))
#endif // QT_CONFIG(tooltip)
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"  \u68c0\u6d4b\u66f4\u65b0  ", None))
#if QT_CONFIG(tooltip)
        self.fastUpdateButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u66f4\u65b0", None))
#endif // QT_CONFIG(tooltip)
        self.fastUpdateButton.setText(QCoreApplication.translate("MainWindow", u"  \u514d\u5b89\u88c5\u66f4\u65b0  ", None))
#if QT_CONFIG(tooltip)
        self.updateCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u68c0\u6d4b\u66f4\u65b0", None))
#endif // QT_CONFIG(tooltip)
        self.updateCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u68c0\u6d4b", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u6253\u5f00\u7f51\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u7f51\u9875\u4e0b\u8f7d [<a href=\"https://github.com/Unarvest/Serial-Debug/releases\"><span style=\" text-decoration: underline; color:#0000ff;\">Github]</span></a><a href=\"https://github.com/Unarvest/Serial-Debug/releases\"><span style=\" color:#0000ff;\"/></a><a href=\"https://github.com/Unarvest/Serial-Debug/releases\"><span style=\" text-decoration: underline; color:#0000ff;\">[</span></a><a href=\"ftp://unarvest.top/pub/\"><span style=\" text-decoration: underline; color:#0000ff;\">\u5907\u7528]</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Setting), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:13pt; font-weight:600;\">\u5e38\u7528\u70ed\u952e\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:13pt;\">Alt + Enter ...... \u53d1\u9001</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:13pt;\""
                        ">Alt + S ............. \u4fdd\u5b58\u6570\u636e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:13pt;\">Alt + C ............ \u6e05\u7a7a\u6570\u636e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:13pt;\">Alt + O ............ \u6253\u5f00/\u5173\u95ed\u4e32\u53e3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:13pt;\">Alt + 1~9 ........ \u591a\u6761\u53d1\u9001</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:13pt;\">---------------------------</span></p>\n"
""
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u8f6f\u4ef6\u663e\u793a\u5f02\u5e38</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u76ee\u524d\u8f6f\u4ef6\u754c\u9762\u7f16\u8f91\u90fd\u662f\u57fa\u4e8e1920x1080\u5206\u8fa8\u7387\uff0c\u7f29\u653e\u6bd4\u4e3a125%\uff0c\u663e\u793a\u5f02\u5e38\u53ef\u5728\u8bbe\u7f6e\u4e2d\u8c03\u6574\u5b57\u4f53\u5927\u5c0f</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:13pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u6211\u7684\u6570\u636e\u4fdd\u5b58\u5728\u54ea\u91cc</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u76ee\u524d\u6240\u6709\u6570\u636e\u9ed8\u8ba4\u4fdd\u5b58\u5728data\u6587\u4ef6\u5939\u4e2d\uff0c\u4e5f\u53ef\u4ee5\u5728\u8bbe\u7f6e\u4e2d\u66f4\u6539\u4fdd\u5b58\u8def\u5f84\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify"
                        "\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u53d6\u6d88\u663e\u793a\u4fe1\u606f\u4f1a\u505c\u6b62\u63a5\u6536\u5417</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u4e0d\u4f1a\uff0c\u91cd\u65b0\u6253\u5f00\u540e\u4f1a\u5c55\u793a\u6240\u6709\u6536\u5230\u7684\u6d88\u606f\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf"
                        "'; font-size:12pt; font-weight:600;\">Q : \u4e3a\u4f55\u4e0d\u80fd\u81ea\u5df1\u9009\u62e9\u4e32\u53e3\u53f7</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u4e32\u53e3\u9009\u62e9\u524d\u5e94\u5148\u70b9\u51fb\u641c\u7d22\u4e32\u53e3\u6309\u94ae\uff0c\u8fd9\u5c06\u4f1a\u5728\u4e0b\u65b9\u5217\u51fa\u6240\u6709\u53ef\u9009\u62e9\u7684\u4e32\u53e3\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u53d1\u9001HEX\u5f00\u542f\u65f6\uff0c"
                        "\u5220\u9664\u6587\u672c\u540e\u51fa\u73b0\u65e0\u6cd5\u6b63\u5e38\u81ea\u52a8\u63d2\u5165\u7a7a\u683c\u95ee\u9898</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u53d1\u9001HEX\u7684\u6587\u672c\u683c\u5f0f\u5316\u4e3a\u8f85\u52a9\u529f\u80fd\uff0c\u51fa\u4e8e\u67d0\u4e9b\u6280\u672f\u95ee\u9898(\u61d2)\uff0c\u8be5\u529f\u80fd\u4f5c\u7528\u8303\u56f4\u6709\u9650\uff0c\u5176\u5b9e\u4e0d\u7ba1\u6709</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">\u6ca1\u6709\u7a7a\u683c\uff0c\u90fd\u4e0d\u5f71\u54cd\u6700\u540e\u7684\u53d1\u9001\uff0c\u7a7a\u683c\u53ea\u662f\u4e3a\u4e86\u65b9\u4fbf\u9605\u8bfb\u800c\u5df2\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empt"
                        "y; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u53d1\u9001HEX\u65f6\uff0c\u5982\u679c\u53d1\u9001\u7684\u662f\u5355\u4e2a\u5b57\u7b26\u4f1a\u62a5\u9519\u5417</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u5355\u4e2a\u5b57\u7b26\u4f1a\u81ea\u52a8\u8865\u96f6\uff0c\u5982\u53d1\u9001F -&gt; 0xF0\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; "
                        "font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u81ea\u52a8\u8fde\u63a5\u5e94\u8be5\u586b\u4ec0\u4e48</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u586b\u9700\u8981\u5f00\u542f\u65f6\u81ea\u52a8\u8fde\u63a5\u7684\u8bbe\u5907\u7684\u5173\u952e\u8bcd, \u5982CH340\u53ef\u4ee5\u5199CH\uff0c\u6216\u8005340\uff0c\u4f46\u4e0d\u53ef\u586b\u5199CHX\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u5feb\u901f\u8fde\u63a5\u548c\u81ea\u52a8\u8fde\u63a5\u540c\u65f6\u52fe\u9009\u65f6\uff0c\u4f1a\u53d1\u751f\u4ec0\u4e48</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u5f00\u542f\u8f6f\u4ef6\u540e\u4f1a\u4f18\u5148\u8fde\u63a5\u6240\u9009\u4e32\u53e3\uff0c\u5931\u8d25\u540e\u624d\u4f1a\u5c1d\u8bd5\u53bb\u81ea\u52a8\u8fde\u63a5\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p></body></html>", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u7ed8\u56fe\u529f\u80fd\u6709\u4ec0\u4e48\u7528</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A :  \u7ed8\u56fe\u529f\u80fd\u53ef\u4ee5\u5c06\u4e32\u53e3\u53d1\u9001\u7684\u53d8\u91cf\u6570\u636e\u8fdb\u884c\u53ef\u89c6\u5316\u5c55\u793a\u3002</span></p>\n"
"<p style=\"-qt-paragra"
                        "ph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u5982\u4f55\u4f7f\u7528\u7ed8\u56fe\u529f\u80fd</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u4f7f\u7528\u7ed8\u56fe\u529f\u80fd\u9700\u6ee1\u8db3\u4e00\u5b9a\u7684\u534f\u8bae\uff0c\u5373: \u6570\u636e\u540d=\u6570\u636e\u91cf\uff1b\u5982Curve=1.23\uff1b\u5176\u4e2d\u7ed3\u5c3e\u7684\uff1b\u4e3a\u622a\u6b62\u7b26</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">\u6570\u636e\u91cf\u4e2d\u95f4\u4e0d\u53ef\u63d2\u5165\u5176\u4ed6\u5b57\u7b26\uff0c\u622a\u6b62\u7b26\u4e3a\u5fc5\u987b\u4e14\u6682\u4e0d\u652f\u6301\u66f4\u6539\u3002\u6ce8\uff1a\u5141\u8bb8\u5b58\u5728\u591a\u4f59\u7a7a\u683c\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u5173\u4e8e\u6807\u7b7e\u7684\u4f5c\u7528</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-s"
                        "ize:12pt;\">A : \u6807\u7b7e\u662f\u66f2\u7ebf\u6240\u5bf9\u5e94\u7684\u53d8\u91cf\u7684\u53d8\u91cf\u540d\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u5173\u4e8e\u6dfb\u52a0\u66f2\u7ebf</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u65b0\u6dfb\u52a0\u7684\u66f2\u7ebf\u9700\u4fdd\u8bc1\u989c\u8272\u548c\u6807\u7b7e\u4e0e\u5df2\u5b58\u5728\u7684\u66f2\u7ebf\u4e0d\u540c\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; m"
                        "argin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u5982\u4f55\u5220\u9664\u66f2\u7ebf</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u5f53\u6240\u9009\u989c\u8272\u6216\u8005\u6240\u586b\u6807\u7b7e\u4e0e\u5df2\u5b58\u5728\u66f2\u7ebf\u4e00\u81f4\u65f6\uff0c\u6dfb\u52a0\u66f2\u7ebf\u6309\u94ae\u5c06\u53d8\u4e3a\u5220\u9664\u66f2\u7ebf\u6309\u94ae\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                        "; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u5173\u4e8e\u9650\u5236\u529f\u80fd</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u9650\u5236\u529f\u80fd\u53ef\u4ee5\u9650\u5236\u6570\u636e\u91cf\uff0c\u9009\u4e2d\u540e\u8fc7\u671f\u6570\u636e\u5c06\u4f1a\u81ea\u52a8\u5220\u9664\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u6682\u505c\u663e\u793a\u4f1a\u5f71\u54cd\u5176\u4ed6\u4fe1\u606f\u63a5\u6536\u5417</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u6682\u505c\u663e\u793a\u53ea\u662f\u505c\u7528\u4e86\u7ed8\u56fe\u529f\u80fd, \u5176\u4ed6\u5185\u5bb9\u4f9d\u7136\u53ef\u4ee5\u6b63\u5e38\u63a5\u6536</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q"
                        " : \u5bfc\u51fa\u56fe\u7247\u540e\uff0c\u56fe\u7247\u4fdd\u5b58\u5728\u54ea\u91cc</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u76ee\u524d\u6240\u6709\u6570\u636e\u9ed8\u8ba4\u4fdd\u5b58\u5728data\u6587\u4ef6\u5939\u4e2d\uff0c\u4e5f\u53ef\u4ee5\u5728\u8bbe\u7f6e\u4e2d\u66f4\u6539\u4fdd\u5b58\u8def\u5f84\u3002</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u6211\u53ef\u4ee5\u5220\u9664\u7f51\u683c\u5417</span></p>\n"
"<p align=\"justi"
                        "fy\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A : \u53ef\u4ee5\u5728\u8bbe\u7f6e\u4e2d\u8c03\u6574</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u62d6\u52a8\u56fe\u5f62\u754c\u9762\u540e\uff0c\u5982\u4f55\u6062\u590d\u6b63\u5e38\u7684\u81ea\u52a8\u663e\u793a\u6a21\u5f0f</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-"
                        "size:12pt;\">A : \u70b9\u51fb\u56fe\u5f62\u754c\u9762\u5de6\u4e0b\u89d2\u7684 A \u56fe\u6807\uff0c\u5373\u53ef\u56de\u5230\u81ea\u52a8\u663e\u793a\u6a21\u5f0f\u3002</span></p></body></html>", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u5173\u4e8e\u91cd\u7f6e\u8bbe\u7f6e</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A :  \u5220\u9664\u8f6f\u4ef6\u6839\u76ee\u5f55\u4e0b\u7684config.json\u5373\u53ef\u91cd\u7f6e</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px;"
                        " margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u5173\u4e8e\u9650\u5236\u7f13\u5b58\u957f\u5ea6</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A :  \u8d85\u8fc7\u9650\u5236\u7684\u5185\u5bb9\u5c06\u81ea\u52a8\u6e05\u9664,\uff0c\u914d\u7f6e\u6b64\u9009\u9879\u53ef\u4ee5\u4f7f\u8f6f\u4ef6\u63a5\u6536\u6548\u7387\u63d0\u9ad8\uff0c \u5efa\u8bae\u503c\u4e3a5000</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'"
                        "\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u5173\u4e8e\u63a5\u6536\u7f16\u7801</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A :  \u9ed8\u8ba4\u4e3aUTF-8, \u652f\u6301\u591a\u79cd\u5e38\u7528\u7f16\u7801</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-"
                        "size:12pt; font-weight:600;\">Q : \u5173\u4e8e\u7ed8\u56fe\u8bbe\u7f6e</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A :  \u82e5\u8bbe\u7f6e\u65e0\u6cd5\u6b63\u5e38\u5de5\u4f5c\uff0c\u53ef\u4ee5\u91cd\u542f\u8f6f\u4ef6</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt; font-weight:600;\">Q : \u5173\u4e8e\u81ea\u52a8\u68c0\u6d4b\u66f4\u65b0</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" font-family:'\u7b49\u7ebf'; font-size:12pt;\">A :  \u5f00\u542f\u540e\u5c06\u4f1a\u5728\u8f6f\u4ef6\u5f00\u542f\u65f6\u81ea\u52a8\u68c0\u6d4b\uff0c\u9ed8\u8ba4\u4e3a\u6bcf\u5f00\u542f\u4e09\u6b21\u8f6f\u4ef6\u68c0\u6d4b\u4e00\u6b21</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\u7b49\u7ebf'; font-size:12pt;\"><br /></p></body></html>", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"--------------------------\n"
"Beta-1.1.5\n"
"-\u4fee\u590d\u66f4\u65b0bug\n"
"--------------------------\n"
"Beta-1.1.4\n"
"-\u6dfb\u52a0\u6a21\u62df\u7ec8\u7aef\u529f\u80fd\n"
"-\u6dfb\u52a0\u53cc\u51fb\u6253\u5f00\u4e32\u53e3\u529f\u80fd\n"
"-\u6dfb\u52a0\u591a\u7ebf\u7a0b\u4e0b\u8f7d\n"
"-\u66f4\u6539\u4e32\u53e3\u53c2\u6570\u5373\u65f6\u751f\u6548\n"
"-\u4fee\u590d\u5f00\u542f\u65f6\u4e32\u53e3\u641c\u7d22\u6846\u4fe1\u606f\u9519\u8bef\n"
"-\u754c\u9762\u6539\u7248\n"
"--------------------------\n"
"Beta-1.1.3\n"
"-\u5168\u65b0\u7684\u66f4\u65b0\u6a21\u5757\n"
"-\u52a0\u5feb\u641c\u7d22\u4e32\u53e3\u901f\u5ea6\n"
"-\u754c\u9762\u6539\u7248\n"
"--------------------------\n"
"Beta-1.1.2\n"
"-\u7ed8\u56fe\u5b57\u7b26\u4e32\u89e3\u6790\u91cd\u5199\n"
"-\u4fee\u590d\u81ea\u52a8\u53d1\u9001bug\n"
"-\u4fee\u590d\u663e\u793a\u6805\u683cbug\n"
"--------------------------\n"
"Beta-1.1.0\n"
"-\u6dfb\u52a0\u5feb\u6377\u952e(Alt + *)\n"
"-\u4fee\u590d\u4e32\u53e3\u610f\u5916\u65ad\u5f00\u540e\u65e0\u6cd5\u518d\u6b21\u8fde"
                        "\u63a5\n"
"--------------------------\n"
"Beta-1.0.1\n"
"-\u4f18\u5316\u754c\u9762\n"
"-\u4f18\u5316\u63d0\u793a\n"
"Beta-1.0.0\n"
"--------------------------\n"
"-\u4f18\u5316\u63d0\u793a\u4fe1\u606f\n"
"-\u4f18\u5316\u4e32\u53e3\u8fde\u63a5\n"
"-\u4f18\u5316\u591a\u7ebf\u7a0b\n"
"-\u4f18\u5316\u754c\u9762\u6846\u67b6\n"
"--------------------------\n"
"\n"
"-\u5386\u53f2\u66f4\u65b0-\n"
"--------------------------\n"
"Alpha 0.54.1\n"
"-\u6dfb\u52a0\u4e32\u53e3\u641c\u7d22\u529f\u80fd\n"
"-\u6dfb\u52a0\u4e32\u53e3\u9009\u62e9\u529f\u80fd\n"
"-\u6dfb\u52a0\u72b6\u6001\u63d0\u793a\n"
"-\u6dfb\u52a0\u6362\u884c\u7b26\n"
"-\u6dfb\u52a0\u663e\u793a\n"
"-\u6dfb\u52a0\u5feb\u901f\u542f\u52a8\n"
"-\u6dfb\u52a0\u53d1\u9001\u63a5\u6536\u8ba1\u6570\n"
"-\u6846\u67b6\u4f18\u5316\n"
"-\u4fee\u4e86\u4e00\u5806bug\n"
"--------------------------\n"
"Alpha 0.54.2\n"
"-\u63d0\u793a\u4fe1\u606f\u4f18\u5316\n"
"-\u6700\u5927\u6700\u5c0f\u5bbd\u5ea6\u4f18\u5316\n"
"-\u4fee\u590dbug:\u6682\u505c\u663e\u793a\u548c\u590d\u9009\u6846\u663e"
                        "\u793a\u9519\u8bef\n"
"-\u4fee\u590dbug:\u53d6\u6d88\u4fdd\u5b58\u6587\u4ef6,\u4f46\u6587\u4ef6\u4ecd\u4fdd\u5b58\n"
"--------------------------\n"
"Alpha 0.55.1\n"
"-\u4f18\u5316\u7a97\u4f53\u5927\u5c0f\u9650\u5236\n"
"-\u79fb\u9664\u4e32\u53e3\u53f7\u9009\u62e9, \u6570\u636e\u5305\u7f16\u8f91\u6846\n"
"-\u4f18\u5316\u7a97\u4f53\u5e03\u5c40\n"
"-\u4e3a\u6253\u5f00\u4e32\u53e3\u6309\u94ae\u6dfb\u52a0\u72b6\u6001\u6307\u793a\n"
"-\u4f18\u5316\u4e32\u53e3\u72b6\u6001\u6807\u5fd7\u4f4d\n"
"--------------------------\n"
"Alpha 0.55.2\n"
"-\u4f18\u5316\u4e32\u53e3\u53f7\u83b7\u53d6\u4ee5\u517c\u5bb9linux\n"
"-\u4f18\u5316\u641c\u7d22\u4e32\u53e3\u63d0\u793a\u4fe1\u606f\n"
"--------------------------\n"
"Alpha 0.55.3\n"
"-\u4f18\u5316\u4e32\u53e3\u4e8c\u6b21\u8fde\u63a5\u901f\u5ea6\n"
"-\u4fee\u590d\u5feb\u901f\u542f\u52a8\u6309\u94ae\u663e\u793a\u9519\u8bef\n"
"-\u4fee\u590d\u4e32\u53e3\u4fe1\u606f\u7f16\u7801\u62a5\u9519\u5bfc\u81f4\u7684\u4e32\u53e3\u65ad\u5f00\n"
"--------------------------\n"
"Alpha 0.56.1\n"
""
                        "-\u6dfb\u52a0\u5b9a\u65f6\u53d1\u9001\u529f\u80fd\n"
"-\u6dfb\u52a0\u56de\u8f66\u53d1\u9001\n"
"-\u4f18\u5316\u5feb\u901f\u8fde\u63a5,\u73b0\u5df2\u4e0d\u4f1a\u9020\u6210\u542f\u52a8\u754c\u9762\u5361\u987f\n"
"-\u4f18\u5316\u63d0\u793a\u4fe1\u606f\n"
"--------------------------\n"
"Alpha 0.56.2\n"
"-\u4fee\u590d\u56de\u8f66\u53d1\u9001\u7a7a\u4fe1\u606f\u62a5\u9519\n"
"--------------------------\n"
"Alpha 0.56.3\n"
"-\u4fee\u590d\u56de\u8f66\u53d1\u9001\u540e\u5149\u6807\u6f02\u79fb\n"
"-\u53d1\u9001\u73b0\u5728\u53ef\u4ee5\u56de\u663e\u51fa\\r\\n\n"
"-\u4f18\u5316\u63d0\u793a\u4fe1\u606f\n"
"--------------------------\n"
"Alpha 0.58.1\n"
"-\u4fee\u590d\u4fe1\u606f\u63a5\u6536\u7a97\u4e0d\u663e\u793a\u4fe1\u606fbug\n"
"-\u6dfb\u52a0\u7ed8\u56fe\u529f\u80fd\n"
"--------------------------\n"
"Alpha 0.58.2\n"
"-\u4fee\u590d\u542f\u52a8\u540e\u65e0\u6cd5\u6b63\u5e38\u8fde\u63a5bug\n"
"--------------------------\n"
"Alpha 0.58.3\n"
"-\u4f18\u5316\u4e32\u53e3\u8fde\u63a5\u540e\u7684\u641c\u7d22\u4e32\u53e3\u529f\u80fd"
                        "\n"
"--------------------------\n"
"Alpha 0.59.1\n"
"-\u4f18\u5316\u5b57\u4f53\n"
"-\u4f18\u5316\u542f\u52a8\u901f\u5ea6\n"
"-\u4f18\u5316\u6846\u67b6\n"
"-\u4f18\u5316\u5728\u4e0d\u540c\u7cfb\u7edf\u7f29\u653e\u4e0b\u7684\u663e\u793a\u6548\u679c\n"
"--------------------------\n"
"Alpha 0.59.2\n"
"-\u4fee\u590d\u4fe1\u606f\u63a5\u6536\u663e\u793a\u4e0a\u4e00\u6761\u4fe1\u606fbug\n"
"--------------------------\n"
"Alpha 0.59.3\n"
"-\u4fee\u590d\u5feb\u901f\u542f\u52a8\u65f6\u5076\u53d1\u7684\u62a5\u9519\n"
"-\u4fee\u590d\u7ed8\u56fe\u6dfb\u52a0\u66f2\u7ebf\u63d0\u793a\u4fe1\u606f\u9519\u8bef\n"
"-\u4f18\u5316\u7ed8\u56fe\u529f\u80fd\u6548\u7387\n"
"-\u6dfb\u52a0\u7ed8\u56fe\u957f\u5ea6\u9650\u5236\u529f\u80fd\n"
"-\u6dfb\u52a0\u80cc\u666f\u989c\u8272\u9009\u62e9\u529f\u80fd\n"
"--------------------------\n"
"Alpha 0.59.4\n"
"-\u6dfb\u52a0\u5bfc\u51fa\u56fe\u7247\u529f\u80fd\n"
"-\u4fee\u590dbug:\u4fe1\u606f\u63a5\u6536\u540e\u5149\u6807\u79fb\u81f3\u5f00\u5934\n"
"--------------------------\n"
"Alpha 0.59.5\n"
""
                        "-\u4fee\u590d\u7ed8\u56fe\u8d85\u51fa\u9650\u5236\u90e8\u5206\u8fd4\u56de\u9650\u5236\u65f6\u4e22\u5931\n"
"--------------------------\n"
"Alpha 0.510.1\n"
"-\u4f18\u5316\u6846\u67b6\n"
"-\u6dfb\u52a0\u4e3b\u9875\u914d\u7f6e\u680f\u6eda\u52a8\n"
"-\u4f18\u5316\u7a97\u4f53\u5927\u5c0f\u9650\u5236\n"
"-\u6dfb\u52a0\u7ed8\u56fe\u533a\u4fe1\u606f\u63d0\u793a\n"
"--------------------------\n"
"Alpha 0.510.2\n"
"-\u6dfb\u52a0\u56fe\u6807\n"
"-\u6dfb\u52a0\u94fe\u63a5\n"
"-\u4f18\u5316\u6392\u7248\n"
"-\u6dfb\u52a0\u53d1\u9001\u591a\u6761\u4fe1\u606f\u6846\n"
"--------------------------\n"
"Alpha 0.511.1\n"
"-\u5c06\u5173\u4e8e\u66f4\u6539\u4e3a\u63d0\u793a\n"
"-\u91cd\u65b0\u6392\u7248\u63d0\u793a\u9875\n"
"-\u6dfb\u52a0\u4e3b\u9875\u3001\u7ed8\u56fe\u7684\u63d0\u793a\u4fe1\u606f\n"
"--------------------------\n"
"Alpha 0.511.2\n"
"-\u4fee\u590d\u672a\u8fde\u63a5\u4e32\u53e3\u65f6\u5b9a\u65f6\u53d1\u9001\u9519\u8bef\n"
"-\u4fee\u590d\u4e32\u53e3\u610f\u5916\u65ad\u8fde\u540e\u5076\u53d1\u7684\u65e0\u6cd5\u518d\u6b21"
                        "\u8fde\u63a5bug\n"
"-\u4f18\u5316\u7a0b\u5e8f\u4f53\u79ef\n"
"-\u4f18\u5316\u663e\u793a\u6548\u679c\n"
"--------------------------\n"
"Alpha 0.511.3\n"
"-\u6dfb\u52a0\u542f\u52a8\u52a8\u753b\n"
"-\u4f18\u5316\u56fe\u6807\n"
"--------------------------\n"
"Alpha 0.512.1\n"
"-\u6dfb\u52a0\u591a\u6761\u53d1\u9001\n"
"-\u6dfb\u52a0\u7ed8\u56fe\u66f2\u7ebf\u6682\u505c\u663e\u793a\u529f\u80fd\n"
"-\u79fb\u9664\u7ed8\u56fe\u66f4\u591a\u8bbe\u7f6e\u529f\u80fd\n"
"-\u4fee\u6539\u7ed8\u56fe\u533a\u63a5\u6536\u6846\u4e3a\u53ea\u8bfb\n"
"-\u4f18\u5316\u63d0\u793a\u4fe1\u606f\n"
"--------------------------\n"
"Alpha 0.516.1\n"
"-\u6dfb\u52a0\u5168\u5c40\u8bbe\u7f6e\n"
"-\u6dfb\u52a0\u7ed8\u56fe\u8bbe\u7f6e\n"
"-\u6dfb\u52a0\u81ea\u52a8\u66f4\u65b0\n"
"-\u6dfb\u52a0\u81ea\u52a8\u68c0\u6d4b\u66f4\u65b0\n"
"-\u6dfb\u52a0\u5168\u5c40\u5b57\u4f53\u8bbe\u7f6e\n"
"--------------------------\n"
"Alpha 0.516.2\n"
"-\u70ed\u4fee\u590d\n"
"--------------------------\n"
"Alpha 0.517.1\n"
"-\u6dfb\u52a0\u4fe1\u606f\u7f16\u7801\u9009\u9879"
                        "\n"
"-\u4f18\u5316\u81ea\u52a8\u66f4\u65b0\n"
"-\u6dfb\u52a0\u8bbe\u7f6e\u56fe\u6807\n"
"--------------------------\n"
"Alpha 0.518.1\n"
"-\u4f18\u5316\u8bbe\u7f6e\u754c\u9762\n"
"-\u6dfb\u52a0\u56fe\u4f8b\u663e\u793a\u8bbe\u7f6e\n"
"-\u4f18\u5316\u63d0\u793a\u4fe1\u606f\n"
"-\u4f18\u5316\u4e3b\u9875\u6846\u67b6\n"
"--------------------------\n"
"Alpha 0.519.1\n"
"-\u4fee\u590d\u53d1\u9001HEX\u6a21\u5f0f\u4e0b, \u975e\u6cd5\u5341\u516d\u8fdb\u5236\u5b57\u7b26\u9020\u6210\u7684\u95ea\u9000\n"
"-\u4fee\u590d\u641c\u7d22\u4e32\u53e3\u62a5\u9519\n"
"-\u4f18\u5316\u53d1\u9001HEX\u529f\u80fd\n"
"-\u6dfb\u52a0\u53d1\u9001\u6846\u5341\u516d\u8fdb\u5236\u4e92\u8f6c\u529f\u80fd\n"
"--------------------------\n"
"Alpha 0.519.2\n"
"-\u4f18\u5316\u68c0\u6d4b\u66f4\u65b0\n"
"-\u4fee\u590d\u4e0b\u8f7d\u9519\u8bef\n"
"-\u4f18\u5316\u542f\u52a8\u901f\u5ea6\n"
"--------------------------\n"
"Alpha 0.519.3\n"
"-\u66f4\u6539\u6253\u5305\u4e3a\u591a\u6587\u4ef6\n"
"-\u6dfb\u52a0\u521b\u5efa\u5feb\u6377\u65b9\u5f0f\n"
"------------"
                        "--------------\n"
"Alpha 0.520.1\n"
"-\u4f18\u5316\u81ea\u52a8\u66f4\u65b0\n"
"--------------------------\n"
"Alpha 0.520.2\n"
"-\u4fee\u590d\u5b9a\u65f6\u53d1\u9001\u4e0e\u56de\u8f66\u53d1\u9001\u51b2\u7a81\n"
"-\u4fee\u590d\u8def\u5f84\u9009\u62e9\u4e3a\u7a7abug\n"
"-\u4fee\u590d\u5b9a\u65f6\u53d1\u9001\u5f00\u542f\u65f6\u65ad\u5f00\u4e32\u53e3\u62a5\u9519\n"
"-\u4fee\u590d\u663e\u793a\u4fe1\u606f\u9519\u8bef\n"
"--------------------------\n"
"Alpha 0.520.3\n"
"-\u4fee\u590dRTS DTR\u5f02\u5e38\n"
"--------------------------\n"
"Alpha 0.521.1\n"
"-\u4fee\u590d\u4e32\u53e3\u72b6\u6001\u663e\u793a\u5f02\u5e38\n"
"-\u66f4\u65b0\u4e32\u53e3\u72b6\u6001\u663e\u793a\u56fe\u7247\n"
"-\u6dfb\u52a0\u7f13\u5b58\u4fe1\u606f\u81ea\u52a8\u4fdd\u5b58\n"
"--------------------------\n"
"Alpha 0.521.2\n"
"-\u4f18\u5316\u6dfb\u52a0\u66f2\u7ebf\u529f\u80fd\n"
"-\u4f18\u5316\u542f\u52a8\u753b\u9762\n"
"-\u4f18\u5316\u7ed8\u56fe\u754c\u9762\n"
"--------------------------\n"
"\u81ea\u5b9a\u4e49\u6570\u636e\u5305\u6682\u4e0d\u53ef\u7528", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7248\u672c \u53d1\u73b0bug\u8bf7\u8054\u7cfb2286107961@qq.com", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u63d0\u793a", None))
    # retranslateUi

